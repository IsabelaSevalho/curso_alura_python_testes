import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user

def test_serialize_user_completo():
    user = {
        "email": "teste@exemplo.com",
        "name": "Teste usuário",
        "address": "123 Rua Exemplo",
        "role": "admin"
    }
    #definimos uma entrada e com base no comportamento temos que veerificar se a saída foi a mesma esperada
    resultado = serialize_user(user) 
    esperado = {
        "email": "teste@exemplo.com",
        "name": "Teste usuário",
        "address": "123 Rua Exemplo",
        "role": "admin"
    }

    assert resultado == esperado #valida se a condição para que o teste seja validado é atendida

def test_serialize_user_incompleto():
    user = {
        "email": "alura@exemplo.com"
    }

    resultado = serialize_user(user)
    esperado={
        "email": "alura@exemplo.com",
        "name": None,
        "address": None,
        "role": "cliente"

    }

def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("string de teste")