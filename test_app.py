import json

class TestAPICases():
    def test_home_route(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
    
    def test_index_route(self, api):
        res = api.get('/pokemon')
        assert res.status == '200 OK'
        assert len(res.json) == 3
        assert res.json[2].name == 'Venusaur'

