import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.product_model import serialize_product

# Retorna todos os campos esperados corretamente.
def test_serialize_product_completo():
    product ={
        "_id": "1",
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13,
        "available": False,
        "ingredients": ["ingrediente_1", "ingrediente_2"]
    }

    resultado = serialize_product(product)

    esperado ={
        "id": "1",
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13,
        "available": False,
        "ingredients": ["ingrediente_1", "ingrediente_2"]
    }

    assert resultado == esperado


# Aplica os valores padrão para os campos opcionais (available e ingredients)
def test_serialize_product_incompleto():
    product ={
        "_id": "1",
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13
    }
    
    resultado = serialize_product(product)

    esperado ={
        "id": "1",
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13,
        "available": True,
        "ingredients": []
    }

    assert resultado == esperado


# Converte corretamente o campo _id para uma string.
def test_serialize_product_conversao_id():
    product ={
        "_id": 123,
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13,
        "available": False,
        "ingredients": ["ingrediente_1", "ingrediente_2"]
    }

    resultado = serialize_product(product)

    esperado ={
        "id": "123",
        "name": "Exemplo produto",
        "description": "Descrição do produto exemplo",
        "category": "Categoria",
        "price": 13,
        "available": False,
        "ingredients": ["ingrediente_1", "ingrediente_2"]
    }

    assert resultado == esperado