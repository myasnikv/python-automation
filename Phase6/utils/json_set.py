class JsonSet:

    def json_create_update(self, project_key, summary, issue_type, priority):
        json = {
            "fields": {
                "project":
                    {
                        "key": project_key
                    },
                "summary": summary,
                "description": "",
                "issuetype": {
                    "name": issue_type
                },
                "priority": {
                    "name": priority,
                },
            }
        }
        return json

    def json_search(self, issue_name, start, max_results):
        json = {
            "jql": "summary~" + issue_name,
            "startAt": start,
            "maxResults": max_results
        }
        return json
