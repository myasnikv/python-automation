import allure
import pytest

from Phase6.pageobjects.login_page import LoginPage
from Phase6.pageobjects.issue_page import IssuePage
from Phase6.utils.values import v_dict
from Phase6.utils.rest_utils import *

rest = RestFlow()


@pytest.mark.usefixtures("wd")
class TestCreateIssue:

    def init_login_page(self):
        login_page = LoginPage(self.driver)
        return login_page

    def init_issue_page(self):
        issue_page = IssuePage(self.driver)
        return issue_page

    @allure.title("Create Issue via REST")
    def test_create_issue_rest(self):
        assert rest.post_issue("Phase 6 New Issue", v_dict().get('p_key'), v_dict().get('issue_type'),
                               v_dict().get('prio_low'), v_dict().get('cc'), v_dict().get('cc')).status_code is 201

    @allure.title("Login and Initial Page Check")
    def test_check_initial_page(self):
        self.driver.get(v_dict().get('issues_url'))
        assert self.init_login_page().login_jira(v_dict().get('cc'), v_dict().get('cc')) is True

    @allure.title("Test Created Issue via UI")
    def test_check_issue_ui(self):
        self.init_issue_page().open_issue_in_list("Phase 6 New Issue")
        assert self.init_issue_page().get_issue_fields() == ['Phase 6 New Issue', 'Low']

    @allure.title("Update issue via REST")
    def test_update_issue_rest(self):
        assert rest.update_issue(created_issue_id[0], "Phase 6 New Issue Updated", v_dict().get('prio_block'),
                                 v_dict().get('p_key'), v_dict().get('issue_type'), v_dict().get('cc'),
                                 v_dict().get('cc')).status_code is 204

    @allure.title("Test Created Issue via UI")
    def test_check_issue_ui(self):
        self.init_issue_page().browser_refresh()
        self.init_issue_page().open_issue_in_list("Phase 6 New Issue Updated")
        assert self.init_issue_page().get_issue_fields() == ['Phase 6 New Issue Updated', 'Blocker']

    @allure.title("Delete Issue via REST")
    def test_delete_issue_rest(self):
        assert rest.delete_issue(created_issue_id[0], v_dict().get('cc'), v_dict().get('cc')).status_code is 204
