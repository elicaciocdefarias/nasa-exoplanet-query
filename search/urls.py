from django.urls import path

from .views import IndexView, UploadCSVOrListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "upload-csv-or-list/",
        UploadCSVOrListView.as_view(),
        name="upload_csv_or_list",
    ),
]
