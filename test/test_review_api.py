import json
import review_service
from unittest.mock import patch


app = review_service.app

def test_create_review_success():
    """
    Компонентный тест POST /reviews.

    Проверяется:
    - корректная обработка входных данных
    - создание отзыва
    - корректный HTTP-статус ответа

    Проверка существования пользователя подменяется мок-объектом.
    """
    with app.test_client() as client:
        with patch("review_service.check_user_exists", return_value=True):
            response = client.post(
                "/reviews",
                data=json.dumps({
                    "user_id": 1,
                    "text": "Good product",
                    "rating": 5
                }),
                content_type="application/json"
            )

            assert response.status_code == 201
            data = response.get_json()
            assert data["user_id"] == 1
            assert data["rating"] == 5


def test_create_review_missing_fields():
    """
    Компонентный тест проверяет обработку запроса
    с отсутствующими обязательными полями.
    """
    with app.test_client() as client:
        response = client.post(
            "/reviews",
            data=json.dumps({
                "user_id": 1
            }),
            content_type="application/json"
        )

        assert response.status_code == 400


def test_create_review_user_not_found():
    """
    Компонентный тест проверяет поведение сервиса,
    если пользователь не существует.
    """
    with app.test_client() as client:
        with patch("review_service.check_user_exists", return_value=False):
            response = client.post(
                "/reviews",
                data=json.dumps({
                    "user_id": 999,
                    "text": "Test",
                    "rating": 3
                }),
                content_type="application/json"
            )

            assert response.status_code == 404


def test_get_review_success():
    """
    Компонентный тест GET /reviews/{id}.

    Проверяется, что ранее созданный отзыв
    может быть получен по идентификатору.
    """
    with app.test_client() as client:
        with patch("review_service.check_user_exists", return_value=True):
            create_response = client.post(
                "/reviews",
                data=json.dumps({
                    "user_id": 2,
                    "text": "Nice",
                    "rating": 4
                }),
                content_type="application/json"
            )

            review_id = create_response.get_json()["id"]

            get_response = client.get(f"/reviews/{review_id}")

            assert get_response.status_code == 200
            assert get_response.get_json()["id"] == review_id


def test_get_review_not_found():
    """
    Компонентный тест проверяет корректный ответ,
    если отзыв с указанным ID не найден.
    """
    with app.test_client() as client:
        response = client.get("/reviews/9999")

        assert response.status_code == 404
