import allure
import pytest

from pageobjects.login_page import LoginPage
from pageobjects.issue_page import IssuePage
from utils.values import v_dict


@pytest.mark.usefixtures("wd", "create_issues")
class TestSearchIssue:

    def init_login_page(self):
        login_page = LoginPage(self.driver)
        return login_page

    def init_issue_page(self):
        issue_page = IssuePage(self.driver)
        return issue_page

    @allure.step("Login and Initial Page Check")
    def test_check_initial_page(self):
        self.driver.get(v_dict().get('auth_url'))
        assert self.init_login_page().login_jira(v_dict().get('cc'), v_dict().get('cc')) is True

    @allure.step("Search 5 issues")
    def test_search_5_issues(self):
        assert self.init_issue_page().search_issues("VM") is 5

    @allure.step("Search 1 issue")
    def test_search_1_issue(self):
        assert self.init_issue_page().search_issues("VM Search0") is 1

    @allure.step("No results in Search")
    def test_search_no_issues(self):
        assert self.init_issue_page().search_issues("abracadabra") is 0
