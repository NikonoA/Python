import requests

id = "no_project_id"
token = "vWFWZZ0VTGum3U+zQq0Qwf9snHW+mfJ2lGtKQfYP8kELuiLWTiu3-Korcht8tsQn"


def test_no_id_project():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    changes = {
        "title": "Python"
    }
    resp = requests.put("https://ru.yougile.com/api-v2/projects/"+id,
                        headers=headers, json=changes)
    assert resp.status_code == 404
