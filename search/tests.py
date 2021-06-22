import pytest

import csv
import tempfile
from search.models import Exoplanet
from search.handlers import HandleFile


class TestIndexView:
    def test_should_return_correct_status_code_when_url_accessed(self, client):
        response = client.get("")
        assert response.status_code == 200


@pytest.fixture
def exoplanet(client):
    planet = Exoplanet.objects.create(
        pl_name="11 Com b",
        hostname="11 Com ",
    )
    return planet


@pytest.fixture
def object_list(client):
    response = client.get("/list/")
    return response.context["object_list"]


@pytest.mark.django_db
class TestListView:
    def test_should_return_correct_status_code_when_url_accessed(
        self,
        client,
    ):
        response = client.get("/list/")
        assert response.status_code == 200

    def test_should_return_empty_queryset_when_database_empty(
        self,
        object_list,
    ):
        assert len(object_list) == 0

    def test_should_return_queryset_with_1_exoplanet(
        self,
        exoplanet,
        object_list,
    ):
        assert len(object_list) == 1

    def test_should_return_queryset_elements_correctly(
        self,
        exoplanet,
        object_list,
    ):
        assert object_list.first() == exoplanet

    def test_should_return_queryset_with_1_exoplante_with_correct_name(
        self,
        exoplanet,
        object_list,
    ):
        db_item = object_list.first()
        assert db_item.pl_name == exoplanet.pl_name


@pytest.fixture
def tmp_file():
    tmpfile = tempfile.NamedTemporaryFile(mode="w", delete=False)
    lines_total = 98
    columns = [0] * 92
    with open(tmpfile.name, "w") as f:
        writer = csv.writer(f)
        for _ in range(lines_total):
            writer.writerow(columns)
    return tmpfile


class TestUploadView:
    def test_should_return_correct_status_code_when_url_accessed(self, client):
        response = client.get("/upload/")
        assert response.status_code == 200

    def test_should_return_false_if_file_type_is_not_csv(
        self,
        tmp_file,
    ):
        with open(tmp_file.name, "rb") as f:
            handleFile = HandleFile(f)
            assert handleFile.is_type_csv() is False

    def test_should_return_true_if_number_column_correct(
        self,
        tmp_file,
    ):
        with open(tmp_file.name, "rb") as f:
            handle_file = HandleFile(f)
            assert handle_file.structure_is_valid() is True

    def test_should_return_instance_list(
        self,
        tmp_file,
    ):
        with open(tmp_file.name, "rb") as f:
            handle_file = HandleFile(f)
            assert isinstance(handle_file.records(), list)

    def test_should_return_list_not_empty(
        self,
        tmp_file,
    ):
        with open(tmp_file.name, "rb") as f:
            handle_file = HandleFile(f)
            handle_file.is_type_csv()
            handle_file.structure_is_valid()
            assert len(handle_file.records()) != 0

    def test_should_first_element_is_type_dict(self, tmp_file):
        with open(tmp_file.name, "rb") as f:
            handle_file = HandleFile(f)
            handle_file.is_type_csv()
            handle_file.structure_is_valid()
            first_record = handle_file.records()[0]
            assert isinstance(first_record, dict)
