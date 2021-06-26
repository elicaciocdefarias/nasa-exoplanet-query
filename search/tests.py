import pytest
import inspect
import search.handlers
import numpy as np
from pathlib import PurePosixPath
from search.models import Exoplanet
from search.handlers import (
    HandleExoplanetArchive,
)

from search.helpers import get_next_five_pages


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
    return response.context["page_obj"]


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
        assert object_list[0] == exoplanet

    def test_should_return_queryset_with_1_exoplante_with_correct_name(
        self,
        exoplanet,
        object_list,
    ):
        db_item = object_list[0]
        assert db_item.pl_name == exoplanet.pl_name


@pytest.fixture
def handle_exoplanet_archive():
    handle_exoplanet_archive = HandleExoplanetArchive()
    return handle_exoplanet_archive


@pytest.fixture
def records(handle_exoplanet_archive):
    records = handle_exoplanet_archive.read().normalize().records()
    return records


class TestHandleExoplanetArchive:
    def test_should_exists(self):
        members = [class_name for class_name, _ in inspect.getmembers(search.handlers)]
        assert "HandleExoplanetArchive" in members

    def test_should_have_file_property_type_pure_path(
        self,
        handle_exoplanet_archive,
    ):
        assert isinstance(handle_exoplanet_archive.file, PurePosixPath)

    def test_should_have_property_dataframe_other_than_none(
        self, handle_exoplanet_archive
    ):
        handle_exoplanet_archive.read()
        assert handle_exoplanet_archive.dataframe is not None

    def test_should_have_only_contains_correct_values(
        self,
        handle_exoplanet_archive,
    ):
        handle_exoplanet_archive.read().normalize()
        values = handle_exoplanet_archive.dataframe.isna().values

        result = list(set(np.all(values, axis=0)))
        assert result[0] == False

    def test_should_return_list(
        self,
        records,
    ):

        assert isinstance(records, list)

    def test_should_return_not_empty_list(
        self,
        records,
    ):
        assert len(records) != 0

    def test_should_contains_dicts_in_the_list(
        self,
        records,
    ):
        first_element = records[0]
        assert isinstance(first_element, dict)


class TestHelpersExoplanetListView:
    def test_should_return_list_five_number_starting_current_page_number(self):
        current_page = 3
        last_page = 10
        expected = [3, 4, 5, 6, 7]

        next_five_pages = get_next_five_pages(current_page, last_page)

        assert next_five_pages == expected

    def test_should_return_list_four_number_starting_current_page_number(self):
        current_page = 7
        last_page = 10
        expected = [7, 8, 9, 10]

        next_five_pages = get_next_five_pages(current_page, last_page)

        assert next_five_pages == expected

    def test_should_return_list_three_number_starting_current_page_number(self):
        current_page = 8
        last_page = 10
        expected = [8, 9, 10]

        next_five_pages = get_next_five_pages(current_page, last_page)

        assert next_five_pages == expected
