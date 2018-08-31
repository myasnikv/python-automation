from pageobjects.login_page import LoginPage
from pageobjects.issue_page import IssuePage
from utils.rest_utils import RestFlow
from utils.driver import _driver

cc = "Victor_Myasnikov"
wc = "Victor_Myasnikov2"
base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=AQAPYTHON"
issues_url = base_url + "/projects/AQAPYTHON/issues/"
my_issues = base_url + "/projects/AQAPYTHON/issues/?filter=myopenissues"


class TestSearchIssue:
    web = _driver()
    rest = RestFlow()
    login_page = LoginPage(web)
    issue_page = IssuePage(web)

    def setup_class(self):
        self.rest.post_issues(2, "VM Search")
        self.web.get(issues_url)
        self.login_page.login_jira(cc, cc)

    def test_search_issues5(self):
        assert self.issue_page.search_issues("VM") == 2

    def test_search_issues1(self):
        assert self.issue_page.search_issues("VM Search0") == 1

    def test_search_issues_none(self):
        assert self.issue_page.search_issues("abracadabra") == 0

    def teardown_class(self):
        self.rest.delete_issue()
        self.web.close()
