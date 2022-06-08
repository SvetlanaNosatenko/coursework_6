from django.http import Http404
from rest_framework import permissions
from ads.models import Comment
from ads.models import Ad


class CommentsAdPermission(permissions.BasePermission):
    message = 'Adding or changing ads, comments for non admin or non user not allowed.'

    def has_permission(self, request, view):

        if request.user.role == "admin":
            return True

        try:
            entity_1 = Comment.objects.get(pk=view.kwargs["pk"])

        except Comment.DoesNotExist:
            raise Http404

        try:
            entity_2 = Ad.objects.get(pk=view.kwargs["pk"])

        except Ad.DoesNotExist:
            raise Http404

        if entity_1.author_id == request.user.id:
            return True

        if entity_2.author_id == request.user.id:
            return True
        return False
