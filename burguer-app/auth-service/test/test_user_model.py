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
        "email": "teste@exemplo.com"
    }
    resultado = serialize_user(user) 
    esperado = {
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado

def test_serialize_user_vazio():

    user = {}
    resultado = serialize_user(user) 
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado

def test_serialize_user_inteiro(): #já que espera um dicionário chave-valor
    with pytest.raises(AttributeError):
        serialize_user(12345)

def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("string de teste") 

def test_serialize_user_lista():
    with pytest.raises(AttributeError):
        serialize_user([]) 

def test_serialize_user_none():
    with pytest.raises(AttributeError):
        serialize_user(None) 

def test_serialize_user_inesperado(): #nao da erro apesar dos valores errados
    user={
        "email": 12345,
        "name": ["Nome inesperado", "Outro nome"],
        "address": {"rua": "123 exemplo"},
        "role": True
    }

    resultado = serialize_user(user)
    esperado={
            "email": 12345,
            "name": ["Nome inesperado", "Outro nome"],
            "address": {"rua": "123 exemplo"},
            "role": True
    }

def test_serialize_user_dict_none(): #nao da erro apesar dos valores errados
    user={
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    resultado = serialize_user(user)
    esperado = {
            "email": None,
            "name": None,
            "address": None,
            "role": None
    }
