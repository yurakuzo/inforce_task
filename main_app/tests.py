import calendar
from datetime import date
from auth_app.models import Employee
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from auth_app.tests import create_employee
from .models import Menu, Restaurant


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


@pytest.mark.django_db
class TestMenuViewSet:
    def test_list_menus(self, api_client):
        response = api_client.get('/restaurant-api/menus/')

        assert response.status_code == 200

    def test_create_menu(self, api_client, create_employee):
        data = {
            'title': 'New Menu',
            'day': 'Mo',
            'price': 10,
            'description': 'Some description'
        }
        api_client.force_authenticate(user=create_employee('Test User'))

        response = api_client.post('/restaurant-api/menus/', data, format='json')

        assert response.status_code == 201
        assert Menu.objects.filter(title='New Menu').exists()


@pytest.mark.django_db
class TestRestaurantViewSet:
    def test_list_restaurants(self, api_client):
        response = api_client.get('/restaurant-api/restaurants/')

        assert response.status_code == 200


@pytest.mark.django_db
class TestTodayMenuList:
    def test_today_menu_list(self, api_client):
        menu = Menu.objects.create(title='Menu 1', day=calendar.day_name[date.today().weekday()][:2], price=107)
        response = api_client.get('/restaurant-api/menus/today')

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Menu 1'
