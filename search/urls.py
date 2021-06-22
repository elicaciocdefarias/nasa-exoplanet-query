from django.urls import path

from .views import IndexView, ExoplanetUploadView, ExoplanetListView

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "upload/",
        ExoplanetUploadView.as_view(),
        name="upload",
    ),
    path(
        "list/",
        ExoplanetListView.as_view(),
        name="list",
    ),
]
