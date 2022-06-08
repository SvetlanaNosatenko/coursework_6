from django.conf.urls.static import static
from django.urls import include, path


from ads.views import AdListViewSet

from ads.views import CommentViewSet
from rest_framework_nested import routers

ads_router = routers.SimpleRouter()
ads_router.register(r'ads', AdListViewSet, basename="ads")
comments_router = routers.NestedSimpleRouter(ads_router, r'ads', lookup='ad')
comments_router.register(r'comments', CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls)),
]

