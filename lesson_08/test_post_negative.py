import requests

id = "0b19c315-9095-439c-8898-00410d007809"


# создать проект без авторизации
def test_create_project_neg():

    data = {
        'title': "Cool_School"
    }

    headers = {
        "Content-Type": "application/json"
        }

    after = requests.post("https://ru.yougile.com/api-v2/projects",
                          json=data, headers=headers)
    assert after.status_code == 401
