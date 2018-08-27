import json

import requests as requests
from project.json_fixtures import *

cc = "Victor_Myasnikov"
wc = "Victor_Myasnikov2"
p_key = "AQAPYTHON"
issue_type = "Bug"
prio = "Low"
summary = ["VM Issue1", "VM Issue2", "VM Issue3", "VM Issue4", "VM Issue5"]
base_url = "http://jira.hillel.it:8080"
auth_url = base_url + "/secure/RapidBoard.jspa?projectKey=AQAPYTHON"
api_issue = base_url + "/rest/api/2/issue/"
api_search = base_url + "/rest/api/2/search"
search_5 = "VM"
search_1 = "issue1"
search_none = "abracadabra"
updated_summary = "VM Issue1 Updated"
error_no_summ = "You must specify a summary of the issue."
error_255_summ = "Summary must be less than 255 characters."
headers = {'Content-Type': 'application/json'}
created_issues = []

j = JsonSet()


class LoginFlow:

    def login(self, username, password):
        resp = requests.get(auth_url, auth=(username, password))
        return [resp.status_code, resp.headers.get("X-Seraph-LoginReason")]


class RestFlow:

    def post_issue(self, summary, project_key=p_key, issue_type=issue_type, prio=prio, user=cc, passwd=cc):
        resp = requests.post(api_issue, data=json.dumps(j.json_create_update(project_key, summary,
            issue_type, prio)), headers=headers, auth=(user, passwd))
        if resp.status_code == 400:
            message_resp = resp.json().get('errors').get('summary')
            return [resp.status_code, message_resp]
        else:
            created_issues.append(resp.json().get('id'))
            return resp.status_code

    def search_issue(self, issue, start=0, max=10, user=cc, passwd=cc):
        resp = requests.post(api_search, data=json.dumps(j.json_search(issue, start, max)), headers=headers,
                             auth=(user, passwd))
        return [resp.status_code, resp.json().get('total')]

    def update_issue(self, id, summary, prio=prio, project_key=p_key, issue_type=issue_type, user=cc, passwd=cc):
        resp = requests.put(api_issue + str(id), data=json.dumps(j.json_create_update(project_key, summary,
            issue_type, prio)), headers=headers, auth=(user, passwd))
        return resp.status_code

    def delete_issue(self, user=cc, passwd=cc):
        response_code = []
        for issue_id in created_issues:
            resp = requests.delete(api_issue + str(issue_id), auth=(user, passwd))
            response_code.append(resp.status_code)
        return response_code

