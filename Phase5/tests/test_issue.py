import allure
import pytest

from Phase5.pageobjects.login_page import LoginPage
from Phase5.pageobjects.issue_page import IssuePage
from Phase5.utils.values import v_dict


@pytest.mark.usefixtures("wd")
class TestCreateIssue:

    def init_login_page(self):
        login_page = LoginPage(self.driver)
        return login_page

    def init_issue_page(self):
        issue_page = IssuePage(self.driver)
        return issue_page

    @allure.title("Login and Initial Page Check")
    def test_check_initial_page(self):
        self.driver.get(v_dict().get('issues_url'))
        assert self.init_login_page().login_jira(v_dict().get('cc'), v_dict().get('cc')) is True

    @allure.title("Check the ability to create an issue with no summary")
    def test_create_issue_empty_summary(self):
        assert self.init_issue_page().create_issue("", "Blocker", "Victor Myasnikov", True) is False

    @allure.title("Check the ability to create an issue with long summary")
    def test_create_issue_long_summary(self):
        assert self.init_issue_page().create_issue("x" * 256, "Blocker", "Victor Myasnikov", False) is False

    @allure.title("Check the ability to create an issue with correct data")
    def test_create_issue(self):
        assert self.init_issue_page().create_issue("Selenium New Issue", "Blocker", "Victor Myasnikov", False) is True
        self.driver.get(v_dict().get('my_issues'))

    @allure.title("Issue update test")
    def test_update_issue(self):
        self.init_issue_page().open_issue_in_list("Selenium New Issue")
        assert self.init_issue_page().update_issue("Selenium New Issue Updated", "Low", "Vladimir Berezhnoy") is True
