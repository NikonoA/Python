import requests

id = "b0740066-7cb8-44f0-afab-f93d42595c9d"
token = "vWFWZZ0VTGum3U+zQq0Qwf9snHW+mfJ2lGtKQfYP8kELuiLWTiu3-Korcht8tsQn"


def test_change_project():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    changes = {
        "title": "Tututu"
    }
    resp = requests.put("https://ru.yougile.com/api-v2/projects/"+id,
                        headers=headers, json=changes)
    assert resp.status_code == 200
