from search.models import Exoplanet
import pytest


@pytest.fixture
def exoplanet(client):
    planet = Exoplanet.objects.create(
        pl_name="11 Com b",
        hostname="11 Com ",
    )
    return planet


class TestIndexView:
    def test_should_return_correct_status_code_when_url_accessed(self, client):
        response = client.get("")
        assert response.status_code == 200


@pytest.mark.django_db
class TestListView:
    def test_should_return_correct_status_code_when_url_accessed(self, client):
        response = client.get("/list/")
        assert response.status_code == 200

    def test_should_return_empty_queryset_when_database_empty(self, client):
        response = client.get("/list/")
        assert len(response.context["object_list"]) == 0

    def test_should_return_queryset_with_1_exoplanet(
        self,
        client,
        exoplanet,
    ):
        response = client.get("/list/")
        assert len(response.context["object_list"]) == 1

    def test_should_return_queryset_elements_correctly(
        self,
        client,
        exoplanet,
    ):
        response = client.get("/list/")
        assert response.context["object_list"].first() == exoplanet

    def test_should_return_queryset_with_1_exoplante_with_correct_name(
        self,
        client,
        exoplanet,
    ):
        response = client.get("/list/")
        assert response.context["object_list"].first().pl_name == exoplanet.pl_name


class TestUploadView:
    def test_should_return_correct_status_code_when_url_accessed(self, client):
        response = client.get("/upload/")
        assert response.status_code == 200
