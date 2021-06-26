from django.urls import path

from .views import IndexView, ExoplanetListView

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "list/",
        ExoplanetListView.as_view(),
        name="list",
    ),
]
