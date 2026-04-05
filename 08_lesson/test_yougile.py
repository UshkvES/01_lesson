from YougileApi import YougileApi
import pytest

TOKEN = 'ptRJDBJ2sf9BDBPLsOD1kIYvWYwY5zipJibKdXm5uENNuzRBy6OZMkaUDlN7Ndvh'

api = YougileApi("https://yougile.com", token=TOKEN)


@pytest.mark.positive
def test_create_project_positive():
    title = "Python_Ushkv"
    result = api.create_project(title)

    assert "id" in result
    project_id = result["id"]

    get_result = api.get_project(project_id)
    assert get_result["title"] == title


@pytest.mark.negative
def test_create_project_negative():
    result = api.create_project("")

    assert "error" in result or "message" in result or "detail" in result


@pytest.mark.positive
def test_update_project_positive():
    create_result = api.create_project("Старое название")
    project_id = create_result["id"]

    new_title = "Новое название"
    api.update_project(project_id, title=new_title)

    get_result = api.get_project(project_id)
    assert get_result["title"] == new_title


@pytest.mark.negative
def test_update_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    result = api.update_project(fake_id, title="Новое название")

    assert "error" in result or "message" in result or "detail" in result


@pytest.mark.positive
def test_get_project_positive():
    title = "Python_Ushkv_GET"
    create_result = api.create_project(title)
    project_id = create_result["id"]

    result = api.get_project(project_id)

    assert result["id"] == project_id
    assert result["title"] == title


@pytest.mark.negative
def test_get_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    result = api.get_project(fake_id)

    assert "error" in result or "message" in result or "detail" in result
