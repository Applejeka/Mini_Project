import pytest
from unittest.mock import MagicMock, patch
from password_manager import add_data, delete_data
from psycopg2 import sql

@pytest.fixture
def mock_connect_db():
    with patch('password_manager.connect_db') as mock:
        yield mock

# Проверка на создание нового пользователя
def test_add_data(mock_connect_db):
    mock_conn = MagicMock()
    mock_connect_db.return_value = mock_conn

    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    username = "1234"
    password = "1234"

    add_data(mock_connect_db, username, password)

    # Проверяем, что курсор был создан и execute был вызван с правильными параметрами
    mock_conn.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(
        sql.SQL('INSERT INTO users (username, password) VALUES (%s, %s)'),
        (username, password)
    )
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()

def test_add_data_no_username_or_password(mock_connect_db):
    # Проверяем, что ничего не происходит, если логин или пароль отсутствуют
    add_data(mock_connect_db, "", "")
    mock_connect_db.assert_not_called()

# Проверка удаления логина и пароля
def test_delete_data(mock_connect_db):
    mock_conn = MagicMock()
    mock_connect_db.return_value = mock_conn

    username = "1234"
    password = "1234"

    # Настраиваем курсор для возврата правильного пароля
    mock_cursor = mock_conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchone.return_value = (password,)

    delete_data(mock_connect_db, username, password)

    # Проверяем, что курсор был создан и данные были удалены
    mock_conn.cursor.assert_called_once()
    mock_cursor.execute.assert_any_call(
        sql.SQL('SELECT password FROM users WHERE username = %s'),
        (username,)
    )
    mock_cursor.execute.assert_any_call(
        sql.SQL('DELETE FROM users WHERE username = %s'),
        (username,)
    )
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()

# Проверка на неправильный пароль
def test_delete_data_incorrect_password(mock_connect_db):
    # Настраиваем заглушку для подключения к базе данных
    mock_conn = MagicMock()
    mock_connect_db.return_value = mock_conn

    username = "test_user"
    password = "wrong_password"

    # Настраиваем курсор для возврата неправильного пароля
    mock_cursor = mock_conn.cursor.return_value.__enter__.return_value
    mock_cursor.fetchone.return_value = ("correct_password",)

    delete_data(mock_connect_db, username, password)

    # Проверяем, что удаление не произошло
    mock_cursor.execute.assert_called_once_with(
        sql.SQL('SELECT password FROM users WHERE username = %s'),
        (username,)
    )
    mock_conn.commit.assert_not_called()
    mock_conn.close.assert_called_once()

if __name__ == "__main__":
    pytest.main()
