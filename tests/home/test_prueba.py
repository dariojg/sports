import pytest

# pytest -rP -> detalle de errores
# pytest -m "marca1"


@pytest.mark.skip(reason="probando skip anottation")
def test_prueba1():
    assert 1 == 1


@pytest.mark.marca1  # marca1 declarada en pytest.ini  para ejecutar tests solo de marca1 -> pytest -m "marca1"
def test_prueba2():
    assert 1 == 1


@pytest.mark.marca1  # marca1 declarada en pytest.ini  para ejecutar tests solo de marca1 -> pytest -m "marca1"
def test_prueba3():
    assert 2 == 2


@pytest.fixture(scope="session")  # scope="session" -> con session NO se ejecuta para cada test, se ejecuta para toda la session, se puede configurar para un determinado modulo
def fixture_1():
    print("Desde fixture_1 antes return")
    yield 3  # retorna valor y cuenta ejecuciones
    print("Desde fixture_1 despues yield")


# @pytest.fixture(scope="session")
# def fixture_2():
#     return 2


@pytest.mark.marca1 
def test_prueba4(fixture_2):
    variable = fixture_2
    assert variable == 2


def test_prueba5():
    assert 25 == 25
