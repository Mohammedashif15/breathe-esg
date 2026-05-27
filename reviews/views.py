from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from emissions.models import EmissionRecord
from .models import Review


class ReviewCreateView(APIView):

    def post(self, request):

        emission_id = request.data.get(
            'emission_id'
        )

        analyst_name = request.data.get(
            'analyst_name'
        )

        comments = request.data.get(
            'comments',
            ''
        )

        emission = EmissionRecord.objects.get(
            id=emission_id
        )

        # Auto suspicious check
        review_status = 'PENDING'

        if emission.co2e > 10000:
            review_status = 'SUSPICIOUS'

        review = Review.objects.create(
            emission=emission,
            analyst_name=analyst_name,
            comments=comments,
            status=review_status
        )

        return Response({
            "message": "Review created",
            "review_id": review.id,
            "status": review.status
        })


class ReviewActionView(APIView):

    def post(self, request):

        review_id = request.data.get(
            'review_id'
        )

        action = request.data.get(
            'action'
        )

        review = Review.objects.get(
            id=review_id
        )

        if review.status == 'LOCKED':
            return Response({
                "error": "Record locked"
            }, status=400)

        if action == 'approve':
            review.status = 'APPROVED'

        elif action == 'reject':
            review.status = 'REJECTED'

        elif action == 'lock':
            review.status = 'LOCKED'

        else:
            return Response({
                "error": "Invalid action"
            }, status=400)

        review.save()

        return Response({
            "message": "Review updated",
            "status": review.status
        })


class ReviewListView(APIView):

    def get(self, request):

        reviews = Review.objects.all().order_by(
            '-created_at'
        )

        data = []

        for r in reviews:
            data.append({
                "id": r.id,
                "emission_id": r.emission.id,
                "analyst": r.analyst_name,
                "status": r.status,
                "comments": r.comments,
                "reviewed_at": r.reviewed_at
            })

        return Response(data)