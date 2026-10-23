import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.product_model import serialize_product

@pytest.mark.parametrize("product, esperado", [
    (
        {
            "_id": "1",
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13,
            "available": False,
            "ingredients": ["ingrediente_1", "ingrediente_2"]
        },
        {
            "id": "1",
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13,
            "available": False,
            "ingredients": ["ingrediente_1", "ingrediente_2"]
        }
    ),
    (
        {
            "_id": "1",
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13
        },
        {
            "id": "1",
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13,
            "available": True,
            "ingredients": []
        }
    ),
    (
        {
            "_id": 123,
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13,
            "available": False,
            "ingredients": ["ingrediente_1", "ingrediente_2"]
        },
        {
            "id": "123",
            "name": "Exemplo produto",
            "description": "Descrição do produto exemplo",
            "category": "Categoria",
            "price": 13,
            "available": False,
            "ingredients": ["ingrediente_1", "ingrediente_2"]
        }
    )

])

def test_serialize_product_parametrizado(product, esperado):
    resultado = serialize_product(product)
    assert resultado == esperado

@pytest.mark.parametrize("entrada",[
    None,
    "string",
    123,
    []
])

def test_serialize_user_parametrizado_excecao(entrada):
    with pytest.raises(AttributeError):
        serialize_product(entrada)