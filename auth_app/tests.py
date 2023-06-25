import pytest
from rest_framework.test import APIClient
from main_app.models import Menu
from .models import Employee, Vote


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_employee():
    def _create_employee(full_name):
        return Employee.objects.create(full_name=full_name)

    return _create_employee


@pytest.fixture
def create_menu():
    def _create_menu(title, day, price):
        return Menu.objects.create(title=title, day=day, price=price)

    return _create_menu


@pytest.fixture
def create_vote():
    def _create_vote(user, chosen_menu):
        return Vote.objects.create(user=user, chosen_menu=chosen_menu)

    return _create_vote


@pytest.mark.django_db
class TestVoteViewSet:
    def test_list_votes(self, api_client, create_vote, create_menu, create_employee):
        user1 = create_employee("Victor")
        chosen_menu1 = create_menu("Test Menu 1", 'Su', 123)
        vote1 = create_vote(user=user1, chosen_menu=chosen_menu1)

        response = api_client.get('/auth/votes/', format='json')

        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == vote1.id

    def test_create_vote(self, api_client, create_employee, create_menu):
        user = create_employee("Jane")
        menu = create_menu("Test Menu 3", 'Mo', 511)

        api_client.force_authenticate(user=user)

        data = {"user": user.id, "chosen_menu": menu.id}
        response = api_client.post('/auth/votes/', data=data)

        assert response.status_code == 201

        vote = Vote.objects.get(id=response.json()["id"])
        assert vote.user == user
        assert vote.chosen_menu == menu


@pytest.mark.django_db
class TestEmployeeRegisterViewSet:
    def test_create_employee(self, api_client):

        data = {"full_name": "Jack", "password": "Qwerty1337"}
        response = api_client.post('/auth/register/', data=data)
        assert response.status_code == 201

        employee = Employee.objects.get(full_name=response.json()["full_name"])
        assert employee.full_name == "Jack"


@pytest.mark.django_db
class TestEmployeeViewSet:
    def test_list_employees(self, api_client, create_employee):
        employee1 = create_employee("Jake")

        response = api_client.get('/auth/employees/')
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1
        assert data[0]["id"] == employee1.id
        assert data[0]["full_name"] == "Jake"
