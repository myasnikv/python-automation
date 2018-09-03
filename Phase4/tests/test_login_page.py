from pageobjects.login_page import LoginPage
from utils.driver import _driver

cc = "Victor_Myasnikov"
wc = "Victor_Myasnikov2"
base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=AQAPYTHON"
issues_url = base_url + "/projects/AQAPYTHON/issues/"
my_issues = base_url + "/projects/AQAPYTHON/issues/?filter=myopenissues"


class TestLogin:
    web = _driver()
    login_page = LoginPage(web)

    def setup_class(self):
        self.web.get(auth_url)

    def test_check_title(self):
        assert self.login_page.get_title() == "Log in - Hillel IT School JIRA"

    def test_login_wrong_username(self):
        assert self.login_page.login_jira(wc, cc) is False

    def test_login_wrong_password(self):
        assert self.login_page.login_jira(cc, wc) is False

    def test_login_correct_credentials(self):
        assert self.login_page.login_jira(cc, cc) is True

    def teardown_class(self):
        self.web.close()
