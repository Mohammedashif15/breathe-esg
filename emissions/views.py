from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord


@api_view(['GET'])
def get_emissions(request):

    try:

        data = EmissionRecord.objects.values(

            'id',
            'source_type',
            'activity_type',
            'scope',
            'quantity',
            'unit',
            'normalized_unit',
            'emission_factor',
            'co2e',
            'is_suspicious',
            'review_status',
            'locked_for_audit',
            'created_at'

        )

        return Response({
            "status": "success",
            "count": len(data),
            "data": list(data)
        })

    except Exception as e:

        return Response({
            "status": "error",
            "message": str(e)
        }, status=500)


@api_view(['GET'])
def suspicious_records(request):

    try:

        data = EmissionRecord.objects.filter(
            is_suspicious=True
        ).values(

            'id',
            'activity_type',
            'scope',
            'quantity',
            'unit',
            'normalized_unit',
            'co2e'

        )

        return Response({
            "status": "success",
            "count": len(data),
            "data": list(data)
        })

    except Exception as e:

        return Response({
            "status": "error",
            "message": str(e)
        }, status=500)


@api_view(['POST'])
def update_review(request):

    try:

        emission_id = request.data.get(
            'id'
        )

        review_status = request.data.get(
            'review_status'
        )

        locked = request.data.get(
            'locked_for_audit',
            False
        )

        emission = EmissionRecord.objects.get(
            id=emission_id
        )

        emission.review_status = review_status
        emission.locked_for_audit = locked
        emission.save()

        return Response({
            "status": "success",
            "message":
            "Review updated"
        })

    except Exception as e:

        return Response({
            "status": "error",
            "message": str(e)
        }, status=500)