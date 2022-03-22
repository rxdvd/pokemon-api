import pytest
import app
from controllers import pokemons


@pytest.fixture
def api(monkeypatch):
    test_pokemon = [{"id": 1,
                     "name": "Bulbasaur",
                     "type": ["Grass",
                              "Poison"],
                     "description": "Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun’s rays, the seed grows progressively larger.",
                     "height": "0.7 m",
                     "weight": "6.9 kg"},
                    {"id": 2,
                     "name": "Ivysaur",
                     "type": ["Grass",
                              "Poison"],
                     "description": "There is a bud on this Pokémon’s back. To support its weight, Ivysaur’s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it’s a sign that the bud will bloom into a large flower soon.",
                     "height": "1 m",
                     "weight": "13 kg"},
                    {"id": 3,
                     "name": "Venusaur",
                     "type": ["Grass",
                              "Poison"],
                     "description": "There is a large flower on Venusaur’s back. The flower is said to take on vivid colors if it gets plenty of nutrition and sunlight. The flower’s aroma soothes the emotions of people.",
                     "height": "2 m",
                     "weight": "100 kg"},
                    ]
    # This is assuming the data is being imported and saved as pokemon inside
    # of controllers/pokemon.py
    monkeypatch.setattr(pokemons, "pokemons", test_pokemon)
    api = app.app.test_client()
    return api
