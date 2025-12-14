import review_service
from unittest.mock import patch

def test_check_user_exists_success():
    """
    Unit-тест проверяет функцию check_user_exists
    при успешном ответе UserService.

    Реальный HTTP-запрос не выполняется.
    Ответ внешнего сервиса подменяется мок-объектом.
    """
    with patch("review_service.requests.get") as mock_get:
        mock_get.return_value.status_code = 200

        result = review_service.check_user_exists(1)

        assert result is True


def test_check_user_exists_not_found():
    """
    Unit-тест проверяет поведение функции,
    если пользователь не найден во внешнем сервисе.
    """
    with patch("review_service.requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        result = review_service.check_user_exists(999)

        assert result is False


def test_check_user_exists_connection_error():
    """
    Unit-тест проверяет обработку исключения
    при ошибке соединения с UserService.
    """
    with patch("review_service.requests.get", side_effect=Exception):
        result = review_service.check_user_exists(1)

        assert result is False
