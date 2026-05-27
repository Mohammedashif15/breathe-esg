import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DataSource, RawRecord
from emissions.models import EmissionRecord

from .utils import (
    detect_scope,
    normalize_unit,
    detect_suspicious
)


@api_view(['GET', 'POST'])
def upload_csv(request):

    if request.method == 'GET':
        return Response({
            "message": "Use POST request to upload CSV"
        })

    try:
        file = request.FILES.get('file')
        source_type = request.data.get('source_type')

        if not file:
            return Response({"error": "File missing"}, status=400)

        if not source_type:
            return Response({"error": "Source type missing"}, status=400)

        # Reset pointer safely
        file.seek(0)

        # Read CSV safely
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except Exception:
            file.seek(0)
            df = pd.read_csv(file, encoding='latin1')

        # Clean columns
        df.columns = df.columns.str.strip().str.lower()

        required_columns = ['activity_type', 'quantity', 'unit']

        missing = [c for c in required_columns if c not in df.columns]

        if missing:
            return Response({
                "error": "Missing columns",
                "missing": missing,
                "columns_found": list(df.columns)
            }, status=400)

        # Create datasource FIRST
        datasource = DataSource.objects.create(
            source_type=source_type,
            uploaded_file=file
        )

        processed = 0
        failed = 0

        for _, row in df.iterrows():
            try:
                # Save raw record
                RawRecord.objects.create(
                    source=datasource,
                    raw_json=row.to_dict()
                )

                # SAFE quantity conversion
                try:
                    quantity = float(row.get('quantity', 0) or 0)
                except:
                    quantity = 0

                unit = str(row.get('unit', '')).strip()
                activity_type = str(row.get('activity_type', '')).strip()

                # Normalize
                quantity, normalized_unit = normalize_unit(quantity, unit)

                scope = detect_scope(source_type)
                suspicious = detect_suspicious(quantity)

                emission_factor = 0.5
                co2e = quantity * emission_factor

                # Save emission record
                EmissionRecord.objects.create(
                    source_type=source_type,
                    activity_type=activity_type,
                    scope=scope,
                    quantity=quantity,
                    unit=unit,
                    normalized_unit=normalized_unit,
                    emission_factor=emission_factor,
                    co2e=co2e,
                    is_suspicious=suspicious,
                    review_status='PENDING'
                )

                processed += 1

            except Exception as row_error:
                print("Row failed:", row_error)
                failed += 1
                continue

        return Response({
            "message": "CSV uploaded successfully",
            "rows_processed": processed,
            "rows_failed": failed
        }, status=201)

    except Exception as e:
        return Response({
            "error": str(e)
        }, status=500)