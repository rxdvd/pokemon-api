import json
from wsgiref import headers


class TestAPICases():
    def test_home_route(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_index_route(self, api):
        res = api.get('/pokemon')
        assert res.status == '200 OK'
        assert len(res.json) == 3
        assert res.json[2]['name'] == 'Venusaur'

    def test_get_pokemon(self, api):
        res = api.get('/pokemon/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Ivysaur'

    def test_get_pokemon_404(self, api):
        res = api.get('/pokemon/4')
        assert res.status == '404 NOT FOUND'
        assert "no pokemon with id 4" in res.json['message']

    def test_post_pokemon(self, api):
        mock_data = json.dumps(
            {
                "name": "test pokemon",
                "type": [
                    "fire", ],
                "description": "A massive test pokemon",
                "height": "122 m",
                "weight": "1000 kg"},
        )
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/pokemon', data=mock_data, headers=mock_headers)
        assert res.status == '201 CREATED'
        assert res.json['id'] == 4
        assert res.json['name'] == 'test pokemon'

    def test_post_pokemon(self, api):
        mock_data = json.dumps(
            {
                "type": [
                    "fire", ],
                "description": "A massive test pokemon",
                "height": "122 m",
                "weight": "1000 kg"},
        )
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/pokemon', data=mock_data, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert 'needs a name' in res.json['message']
