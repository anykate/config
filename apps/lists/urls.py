from django.urls import path, include
from rest_framework_nested import routers
from .views import ListViewSet, ListItemViewSet

router = routers.SimpleRouter()
router.register('', ListViewSet)

lists_router = routers.NestedSimpleRouter(router, '', lookup='list')
lists_router.register('list-items', ListItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lists_router.urls)),
]
