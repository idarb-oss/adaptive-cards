from adaptivecards.actions import OpenUrl, Submit


def test_open_url_action():
    action = OpenUrl(url="https://localhost:8000")

    assert action.type == "Action.OpenUrl"
    assert action.url == "https://localhost:8000"


def test_submit_action():
    action = Submit()

    assert action.type == "Action.Submit"
    assert action.data == None
    assert action.associated_inputs == None
