from selenium.webdriver.common.by import By
from pageobjects.base import BasePage

login_id = 'login-form-username'
password_id = 'login-form-password'
submit_button = 'login-form-submit'
login_error = ".aui-message.error"


class LoginPage(BasePage):

    def get_title(self):
        return self.driver.title

    def login_jira(self, login, password):
        self.type_to_elem(login_id, By.ID, login)
        self.type_to_elem(password_id, By.ID, password)
        self.click_elem(submit_button, By.ID)

        if "AQAPYTHON" in self.driver.title:
            return True
        else:
            return False
