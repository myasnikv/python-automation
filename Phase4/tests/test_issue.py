from pageobjects.login_page import LoginPage
from pageobjects.issue_page import IssuePage
from utils.driver import _driver

cc = "Victor_Myasnikov"

base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=AQAPYTHON"
issues_url = base_url + "/projects/AQAPYTHON/issues/"
my_issues = base_url + "/projects/AQAPYTHON/issues/?filter=myopenissues"


class TestCreateIssue:
    web = _driver()
    login_page = LoginPage(web)
    issue_page = IssuePage(web)

    def setup_class(self):
        self.web.get(issues_url)
        self.login_page.login_jira(cc, cc)

    def test_create_issue_empty_summary(self):
        assert self.issue_page.create_issue("", "Blocker", "Victor Myasnikov", True) is False

    def test_create_issue_long_summary(self):
        assert self.issue_page.create_issue("x" * 256, "Blocker", "Victor Myasnikov", False) is False

    def test_create_issue(self):
        assert self.issue_page.create_issue("Selenium New Issue", "Blocker", "Victor Myasnikov", False) is True
        self.web.get(my_issues)

    def test_update_issue(self):
        self.issue_page.open_issue_in_list("Selenium New Issue")
        assert self.issue_page.update_issue("Selenium New Issue Updated", "Low", "Vladimir Berezhnoy") is True

    def teardown_class(self):
        self.web.close()
