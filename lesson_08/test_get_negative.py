import requests

id = "97eebfff-5b8e-4900-9a07-39f965946d70"
token = "vWFWZZ0VTGum3U+zQq0Qwf9snHW+mfJ2lGtKQfYP8kELuiLWTiu3-Korcht8tsQn"


def test_get_project_pos():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    resp = requests.get("https://ru.yougile.com/api-v2/projects/"+id,
                        headers=headers)
    assert resp.json()["title"] == "Cool__School"
    assert resp.json()["timestamp"] == 1845767518930
