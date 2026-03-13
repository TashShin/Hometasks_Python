import requests


base_url = "https://ru.yougile.com/api-v2"
api_key = "ПОДСТАВИТЬ ВЕРНОЕ ЗНАЧЕНИЕ"
not_exist_id = 123456789


# Создание проекта

def test_create_pos():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask1",
        "users": {
            "ccf108cf-c1fb-43f5-9ccb-11be3ce521f3": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    assert project_id is not None

    # Удаление созданного проекта
    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_create_neg():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project = {
        "title": "",
        "users": {
            "ccf108cf-c1fb-43f5-9ccb-11be3ce521f3": "admin"
        }
    }
    resp = requests.post(f"{base_url}/projects", json=project, headers=headers)
    assert resp.status_code == 400
    assert resp.json()["message"][0] == "title should not be empty"

# Изменение проекта


def test_update_pos():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask1",
        "users": {
            "ccf108cf-c1fb-43f5-9ccb-11be3ce521f3": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    update_project = {
        "title": "Lesson08"
    }
    resp_put = requests.put(
        f"{base_url}/projects/{project_id}",
        json=update_project, headers=headers)
    assert resp_put.status_code == 200
    resp_get = requests.get(
        f"{base_url}/projects/{project_id}", headers=headers)
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == "Lesson08"

    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_update_neg():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project = {
        "title": "Python",
        "users": {
            "ccf108cf-c1fb-43f5-9ccb-11be3ce521f3": "admin"
        }
    }
    resp = requests.put(
        f"{base_url}/projects/{not_exist_id}", json=project, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["message"] == "Проект не найден"


# Получить по ID

def test_get_id_pos():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    project_body = {
        "title": "Hometask",
        "users": {
            "ccf108cf-c1fb-43f5-9ccb-11be3ce521f3": "admin"
        }
    }
    resp = requests.post(
        f"{base_url}/projects", json=project_body, headers=headers)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    resp_get = requests.get(
        f"{base_url}/projects/{project_id}", headers=headers)
    assert resp_get.status_code == 200
    assert resp_get.json()["title"] == "Hometask"
    assert resp_get.json()["id"] == project_id

    requests.put(
        f"{base_url}/projects/{project_id}",
        json={"deleted": True}, headers=headers)


def test_get_id_neg():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    resp_get = requests.get(
        f"{base_url}/projects/{not_exist_id}", headers=headers)
    assert resp_get.status_code == 404
    assert resp_get.json()["message"] == "Проект не найден"
