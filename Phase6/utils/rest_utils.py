import json

import requests as requests
from Phase6.utils.json_set import JsonSet

cc = "Victor_Myasnikov"
p_key = "AQAPYTHON"
issue_type = "Bug"
prio = "Low"
base_url = "http://jira.hillel.it:8080"
api_issue = base_url + "/rest/api/2/issue/"
headers = {'Content-Type': 'application/json'}
created_issue_id = []
j = JsonSet()


class RestFlow:

    def post_issue(self, summary, project_key=p_key, issue_type=issue_type, prio=prio, user=cc, passwd=cc):
        resp = requests.post(api_issue, data=json.dumps(j.json_create_update(project_key, summary, issue_type, prio)),
                             headers=headers, auth=(user, passwd))
        created_issue_id.append(resp.json().get('id'))
        return resp

    def update_issue(self, id, summary, prio=prio, project_key=p_key, issue_type=issue_type, user=cc, passwd=cc):
        resp = requests.put(api_issue + str(id),
                            data=json.dumps(j.json_create_update(project_key, summary, issue_type, prio)),
                            headers=headers, auth=(user, passwd))
        return resp

    def delete_issues(self, user=cc, passwd=cc):
        response_code = []
        for issue_id in created_issue_id:
            resp = requests.delete(api_issue + str(issue_id), auth=(user, passwd))
            response_code.append(resp.status_code)
        return response_code

    def delete_issue(self, id, user=cc, passwd=cc):
        resp = requests.delete(api_issue + str(id), auth=(user, passwd))
        return resp

    def post_issues(self, count, summary, project_key=p_key, issue_type=issue_type, prio=prio, user=cc, passwd=cc):
        for i in range(count):
            self.post_issue(summary + str(i), project_key, issue_type, prio, user, passwd)
