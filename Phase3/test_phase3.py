import pytest
from project.jira_req import *

login_case = LoginFlow()
rest = RestFlow()


class TestSuite:

    @pytest.mark.parametrize("response,expected", [
        (login_case.login(cc, wc), [401, "AUTHENTICATED_FAILED"]),
        (login_case.login(wc, cc), [401, "AUTHENTICATED_FAILED"]),
        (login_case.login(cc, cc), [200, "OK"]), ])
    def test_login_positive_negative(self, response, expected):
        assert response == expected

    """ create 5 tickets for further search matching and also checking for the correct status response """

    @pytest.mark.parametrize("response,expected", [
        (rest.post_issue(summary[0]), 201),
        (rest.post_issue(summary[1]), 201),
        (rest.post_issue(summary[2]), 201),
        (rest.post_issue(summary[3]), 201),
        (rest.post_issue(summary[4]), 201)])
    def test_post_issue(self, response, expected):
        assert response == expected

    def test_post_missed_field(self):
        assert rest.post_issue("") == [400, error_no_summ]

    def test_post_long_summary(self):
        assert rest.post_issue("x" * 256) == [400, error_255_summ]

    @pytest.mark.parametrize("response,expected", [
        (rest.search_issue(search_5), [200, 5]),
        (rest.search_issue(search_1), [200, 1]),
        (rest.search_issue(search_none), [200, 0])])
    def test_search_issue(self, response, expected):
        assert response == expected

    def test_update_issue(self):
        assert rest.update_issue(created_issues[0], updated_summary) == 204

    def test_delete_issues(self):
        response = rest.delete_all_issues()
        assert len(response) == 5
        assert response == [204] * 5

    def test_num(self):
        assert rest.re_run_test() == 2
