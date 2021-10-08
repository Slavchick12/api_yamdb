from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from reviews.models import Review
from .serializers import CommentSerializer, ReviewSerializer
from .pagination import ReviewsPagination, CommentsPagination
from .permissions import AdminOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = ReviewsPagination
    
    def get_permissions(self):
        if self.action == 'update':
            raise PermissionDenied('Do not allow PUT request')
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = CommentsPagination

    def get_permissions(self):
        if self.action == 'update':
            raise PermissionDenied('Do not allow PUT request')
        return super().get_permissions()

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs['review_id'])
        serializer.save(author=self.request.user, review=review)
