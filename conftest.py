"""
    fixtures para tests
"""
import pytest
from django.contrib.auth.models import User
from users.models import Customer


@pytest.fixture(
    scope="session"
)  # scope="session" -> con session NO se ejecuta para cada test, se ejecuta para toda la session, se puede configurar para un determinado modulo
def fixture_1():
    print("Desde fixture_1 antes return")
    yield 3  # retorna valor y cuenta ejecuciones
    print("Desde fixture_1 despues yield")


@pytest.fixture(scope="session")
def fixture_2():
    return 2


@pytest.fixture()
def customer_factory(db):
    def crear_customer(
        _username="fafa",
        _first_name: str = "name",
        _last_name: str = "lastNAME",
    ):
        user = User(username=_username)
        customer = Customer(
            usuario=user,
            first_name=_first_name,
            last_name=_last_name,
        )
        return customer

    return crear_customer


@pytest.fixture
def crear_customer_2(customer_factory):
    customer = customer_factory("username.homer", "Homer", "Simpson")
    return customer
