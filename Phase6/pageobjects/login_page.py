import allure
from selenium.webdriver.common.by import By
from Phase6.pageobjects.base import BasePage

login_id = 'login-form-username'
password_id = 'login-form-password'
submit_button = 'login-form-submit'
login_error = ".aui-message.error"
create_issue_id = "create_link"


class LoginPage(BasePage):

    @allure.step
    def get_title(self):
        return self.driver.title

    @allure.step
    def login_jira(self, login, password):
        self.type_to_elem(login_id, By.ID, login)
        self.type_to_elem(password_id, By.ID, password)
        self.click_elem(submit_button, By.ID)
        return self.presence_of_element(create_issue_id, By.ID)
