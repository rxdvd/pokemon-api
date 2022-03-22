import json


class TestAPICases():
    def test_home_route(self, api):
        res = api.get('/')
        assert res.status == '200 OK'

    def test_index_route(self, api):
        res = api.get('/pokemon')
        assert res.status == '200 OK'
        assert len(res.json) == 3
        assert res.json[2]['name'] == 'Venusaur'

    def test_get_pokemon(self,api):
        res = api.get('/pokemon/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Ivysaur'

    def test_get_pokemon_404(self, api):
        res = api.get('/pokemon/4')
        assert res.status == '404 NOT FOUND'
        assert "no pokemon with id 4" in res.json['message']
