import pytest
import requests

# Проверка успешного создания поста
def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    new_post = {
        "title": "Test",
        "body": "Test for the task",
        "userId": 1
    }
    response = requests.post(url, json=new_post)

# Проверка на статус-код 201
    assert response.status_code == 201

# Проверка, что ответ содержит правильные данные
    response_data = response.json()
    assert response_data["title"] == new_post["title"]
    assert response_data["body"] == new_post["body"]
    assert response_data["userId"] == new_post["userId"]


# Проверка успешного обновления поста
def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    updated_post = {
        "id": 1,
        "title": "Updated Test Post",
        "body": "This post has been updated",
        "userId": 1
    }

    response = requests.put(url, json=updated_post)

# Проверка на статус-код 200 успешного обновления
    assert response.status_code == 200
    response_data = response.json()

# Проверка, что ответ содержит корректные данные
    assert response_data["id"] == updated_post["id"]
    assert response_data["title"] == updated_post["title"]
    assert response_data["body"] == updated_post["body"]
    assert response_data["userId"] == updated_post["userId"]

def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
# Сначала удаляем пост
    response = requests.delete(url)
# Проверка на статус-код 200 успешного удаления
    assert response.status_code == 200

