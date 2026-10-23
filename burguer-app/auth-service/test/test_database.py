import pytest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

#O OBJETIVO DE MOCKAR AQUI SERIA SIMULAR ESSA CONEXÃO NO BANCO:
#Cria a conexão com o banco de dados MongoDB
# client = MongoClient(os.getenv("MONGO_URI"))
# Seleciona o banco de dados
# db = client["burguer_app_db"]

def test_get_db():
    #patch permite que seja feita a simulação do comportamento de um objeto
    with patch("pymongo.MongoClient") as mock_client:
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db

        from config.database import get_db

        with patch("config.database.client", mock_client.return_value):
            db_instance = get_db()
            assert db_instance is not None

    