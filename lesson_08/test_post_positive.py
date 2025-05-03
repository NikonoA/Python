import requests

id = "0b19c315-9095-439c-8898-00410d007809"
token = "vWFWZZ0VTGum3U+zQq0Qwf9snHW+mfJ2lGtKQfYP8kELuiLWTiu3-Korcht8tsQn"


# создать компанию
def test_create_project_pos():

    data = {
        'title': "Cool_School"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }

    after = requests.post("https://ru.yougile.com/api-v2/projects",
                          json=data, headers=headers)
    assert after.status_code == 201
