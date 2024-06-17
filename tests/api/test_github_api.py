import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api_client):
    user = github_api_client.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api_client):
    r = github_api_client.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api_client):
    r = github_api_client.search_repo("become-qa-auto")
    assert r["total_count"] > 0
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api_client):
    r = github_api_client.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api_client):
    r = github_api_client.search_repo("s")
    assert r["total_count"] != 0
