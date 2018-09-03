import allure
import pytest

from pageobjects.login_page import LoginPage
from utils.values import v_dict


@pytest.mark.usefixtures("wd")
class TestLogin:

    def init_login_page(self):
        login_page = LoginPage(self.driver)
        return login_page

    @allure.step("Initial Page Check")
    def test_check_title(self):
        self.driver.get(v_dict().get('auth_url'))
        assert self.init_login_page().get_title() == "Log in - Hillel IT School JIRA"

    @allure.step("Test login with wrong Username")
    def test_login_wrong_username(self):
        assert self.init_login_page().login_jira(v_dict().get('wc'), v_dict().get('cc')) is False

    @pytest.mark.xfail
    @allure.step("Failed\Skipped test for screen-shot creation")
    def test_login_wrong_username_screenshot(self):
        assert self.init_login_page().login_jira(v_dict().get('wc'), v_dict().get('cc')) is True

    @allure.step("Test login with wrong Password")
    def test_login_wrong_password(self):
        assert self.init_login_page().login_jira(v_dict().get('cc'), v_dict().get('wc')) is False

    @allure.step("Test login with correct Credentials")
    def test_login_correct_credentials(self):
        assert self.init_login_page().login_jira(v_dict().get('cc'), v_dict().get('cc')) is True
