import json

import requests as requests
from Phase5.utils.json_set import JsonSet

cc = "Victor_Myasnikov"
p_key = "AQAPYTHON"
issue_type = "Bug"
prio = "Low"
base_url = "http://jira.hillel.it:8080"
api_issue = base_url + "/rest/api/2/issue/"
headers = {'Content-Type': 'application/json'}
created_issues_list = []

j = JsonSet()


class RestFlow:

    def post_issue(self, summary, project_key=p_key, issue_type=issue_type, prio=prio, user=cc, passwd=cc):
        resp = requests.post(api_issue, data=json.dumps(j.json_create_update(project_key, summary,
                                                                             issue_type, prio)), headers=headers,
                             auth=(user, passwd))
        if resp.status_code == 400:
            message_resp = resp.json().get('errors').get('summary')
            return [resp.status_code, message_resp]
        else:
            created_issues_list.append(resp.json().get('id'))
            return resp.status_code

    def delete_issue(self, user=cc, passwd=cc):
        response_code = []
        for issue_id in created_issues_list:
            resp = requests.delete(api_issue + str(issue_id), auth=(user, passwd))
            response_code.append(resp.status_code)
        return response_code

    def post_issues(self, count, summary, project_key=p_key, issue_type=issue_type, prio=prio, user=cc, passwd=cc):
        for i in range(count):
            self.post_issue(summary + str(i), project_key, issue_type, prio, user, passwd)