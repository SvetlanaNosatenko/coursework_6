from rest_framework import viewsets
from ads.models import Ad
from ads.serializers import AdListSerializer
from ads.models import Comment
from ads.serializers import CommentSerializer
from ads.serializers import AdDetailSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from ads.permissions import CommentsAdPermission


class AdListViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdListSerializer

    def get_permissions(self):
        permission_classes = (AllowAny, )
        if self.action in ["retrieve"]:
            permission_classes = (AllowAny, )
        elif self.action in ["create", "update", "partial_update", "destroy", "me"]:
            permission_classes = (CommentsAdPermission, )
        return tuple(permission() for permission in permission_classes)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(
        detail=False,
        methods=[
            "get",
        ],
    )
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_pk']
        user = self.request.user
        serializer.save(ad_id=ad_id, author=user)

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'], author=self.request.user).all()

    def get_permissions(self):
        permission_classes = (AllowAny, )
        if self.action in ["retrieve"]:
            permission_classes = (AllowAny, )
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (CommentsAdPermission, )
        return tuple(permission() for permission in permission_classes)

