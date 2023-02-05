import json,requests
import pytest
from flask import Flask
from main import app,db



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_market_data(client):
     response = client.get('api/v3/markets/summaries',content_type='application/json')
     data = json.loads(response.get_data(as_text=True))
     print("data",data)
     assert response.status_code == 200
     assert data['message'] == 'markets data received'
     assert data['result'] is not None
     
     


    

def test_get_market_by_id(client):
    response = client.get('/api/v3/markets/ltc-btc/summary',content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data is not None
    #data = response.json()
    assert "high" in data
    assert "low" in data
    assert "percentChange" in data
    assert "quoteVolume" in data
    assert "symbol" in data
    assert "updatedAt" in data
    assert "volume" in data
    assert type(data["high"]) == str
    assert type(data["low"]) == str
    assert type(data["percentChange"]) == str
    assert type(data["quoteVolume"]) == str
    assert type(data["symbol"]) == str
    assert type(data["updatedAt"]) == str
    assert type(data["volume"]) == str

    assert data["symbol"] == "LTC-BTC"
    

