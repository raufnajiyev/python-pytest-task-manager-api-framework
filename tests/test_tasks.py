from utils.api_routes import BASE_URL, TODOS_ENDPOINT, ADD_TODO_ENDPOINT
from utils.api_client import APIClient
from data.task_data import (
    CREATE_TASK_PAYLOAD,
    UPDATE_TASK_PAYLOAD,
    INVALID_CREATE_TASK_PAYLOAD,
    VALID_USER_ID,
    INVALID_TASK_ID,
    VALID_TASK_ID,
)

api_client = APIClient()


# Verify that a single task can be retrieved by valid task ID
def test_user_can_get_single_task_by_id():
    response = api_client.get(f"{TODOS_ENDPOINT}/{VALID_TASK_ID}")

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == VALID_TASK_ID
    assert "todo" in response_body
    assert "completed" in response_body
    assert "userId" in response_body


# Verify that the full task list can be retrieved
def test_user_can_get_all_tasks():
    response = api_client.get(TODOS_ENDPOINT)

    assert response.status_code == 200

    response_body = response.json()

    assert "todos" in response_body
    assert isinstance(response_body["todos"], list)
    assert len(response_body["todos"]) > 0


# Verify that a new task can be created successfully
def test_user_can_create_task():
    response = api_client.post(ADD_TODO_ENDPOINT, CREATE_TASK_PAYLOAD)

    assert response.status_code == 201

    response_body = response.json()

    assert response_body["todo"] == CREATE_TASK_PAYLOAD["todo"]
    assert response_body["completed"] == CREATE_TASK_PAYLOAD["completed"]
    assert response_body["userId"] == CREATE_TASK_PAYLOAD["userId"]


# Verify API behavior when required task field is missing
def test_user_cannot_create_task_without_todo_field():
    response = api_client.post(ADD_TODO_ENDPOINT, INVALID_CREATE_TASK_PAYLOAD)

    assert response.status_code == 201

    response_body = response.json()

    assert "todo" not in INVALID_CREATE_TASK_PAYLOAD
    assert "todo" not in response_body
    assert response_body["completed"] == INVALID_CREATE_TASK_PAYLOAD["completed"]
    assert response_body["userId"] == INVALID_CREATE_TASK_PAYLOAD["userId"]


# Verify that an existing task can be updated
def test_user_can_update_task():
    response = api_client.put(f"{TODOS_ENDPOINT}/{VALID_TASK_ID}", UPDATE_TASK_PAYLOAD)

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == VALID_TASK_ID
    assert response_body["todo"] == UPDATE_TASK_PAYLOAD["todo"]
    assert response_body["completed"] == UPDATE_TASK_PAYLOAD["completed"]


# Verify that an existing task can be deleted
def test_user_can_delete_task():
    response = api_client.delete(f"{TODOS_ENDPOINT}/{VALID_TASK_ID}")

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == VALID_TASK_ID
    assert response_body["isDeleted"] is True
    assert "deletedOn" in response_body


# Verify that requesting a non-existing task returns not found
def test_user_gets_404_for_invalid_task_id():
    response = api_client.get(f"{TODOS_ENDPOINT}/{INVALID_TASK_ID}")

    assert response.status_code == 404


# Verify that tasks can be retrieved for a specific user
def test_user_can_get_tasks_by_user_id():
    response = api_client.get(f"{BASE_URL}/todos/user/{VALID_USER_ID}")

    assert response.status_code == 200

    response_body = response.json()

    assert "todos" in response_body
    assert isinstance(response_body["todos"], list)
    assert len(response_body["todos"]) > 0