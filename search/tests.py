import pytest
from django.urls import reverse


@pytest.fixture
def upload_csv_or_list(client):
    return client.get(reverse("upload_csv_or_list"))


@pytest.mark.django_db
class TestUploadCSVOrListView:
    def test_should_return_301_status_code(self, upload_csv_or_list):
        assert upload_csv_or_list.status_code == 301

    def test_should_return_correctly_url(self, upload_csv_or_list):
        assert upload_csv_or_list.url == "upload/"
