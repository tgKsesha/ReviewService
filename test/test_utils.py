# tests/test_utils.py

#import pytest
#from review_service import check_user_exists
#from ReviewService.review_service import check_user_exists


#def test_check_user_exists():
    # Тест с несуществующим пользователем
   # assert check_user_exists(99999) is False

    # Можно добавить тест с существующим пользователем,
    # если UserService запущен и есть пользователь с id=1
    # assert check_user_exists(1) is True
import pytest
from ReviewService.review_service import check_user_exists

def test_check_user_exists():
    # Тест с несуществующим пользователем
    assert check_user_exists(99999) is False

    # Тест с существующим пользователем
    assert check_user_exists(1) is True
