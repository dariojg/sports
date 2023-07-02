import datetime
import pytest
from django.contrib.auth.models import User
from users.models import Customer


@pytest.fixture
def crear_customer(db):
    user = User(username="fixture.username", first_name="test name", last_name="test last")
    user.save()
    customer = Customer(usuario=user, fecha_nacimiento=datetime.datetime.now())
    return customer


@pytest.mark.django_db
def test_crear_customer(crear_customer):
    customer = crear_customer
    customer.save()
    print(customer.usuario)
    assert customer.usuario.username == "fixture.username"
