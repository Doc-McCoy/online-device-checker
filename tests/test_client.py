import unittest
from client.client import app


class TestClient(unittest.TestCase):
    """
    Testa a classe client, que ficará no Raspbery (ou outro dispositivo
    na rede doméstica que se deseja monitorar)
    """
    def setUp(self):
        """
        Provê um client de testes do próprio flask
        """
        self.client = app.test_client()

    def test_register_client(self):
        """
        Testa o método que registra um client no server, para que
        o mesmo seja verificado periodicamente.
        """
        pass

    def test_check(self):
        """
        Testa se o client está respondendo a request que verifica
        se ele está online
        """
        expected_response = {'status': 'online'}
        response = self.client.get('/check')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), expected_response)
