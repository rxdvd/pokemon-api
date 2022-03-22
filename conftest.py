import pytest
import app
from controllers import pokemon

@pytest.fixture
def api(monkeypatch):
    test_pokemon = [
        {'id': 1, 'name': 'Test Cat 1', 'age': 7},
        {'id': 2, 'name': 'Test Cat 2', 'age': 4}
    ]
    # This is assuming the data is being imported and saved as pokemon inside of controllers/pokemon.py
    monkeypatch.setattr(pokemon, "pokemon", test_pokemon)
    api = app.app.test_client()
    return api
