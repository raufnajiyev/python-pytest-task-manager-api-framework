CREATE_TASK_PAYLOAD = {
    "todo": "Learn API automation with Pytest",
    "completed": False,
    "userId": 1
}

UPDATE_TASK_PAYLOAD = {
    "todo": "Updated task title",
    "completed": True
}

INVALID_CREATE_TASK_PAYLOAD = {
    "completed": False,
    "userId": 1
}

VALID_USER_ID = 1
INVALID_TASK_ID = 999999
VALID_TASK_ID = 1