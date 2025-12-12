# tests/test_endpoints.py

import pytest
import requests

BASE_URL = "http://localhost:5002"

def test_create_review_missing_fields():
    response = requests.post(f"{BASE_URL}/reviews", json={})
    assert response.status_code == 400
    assert response.json()["error"] == "Missing fields"

def test_create_and_get_review():
    # Создаем отзыв (предполагаем, что UserService запущен и есть user_id=1)
    payload = {"user_id": 1, "text": "Отлично!", "rating": 5}
    response = requests.post(f"{BASE_URL}/reviews", json=payload)
    assert response.status_code == 201
    review = response.json()
    review_id = review["id"]

    # Получаем отзыв по id
    response = requests.get(f"{BASE_URL}/reviews/{review_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Отлично!"
    assert data["rating"] == 5
