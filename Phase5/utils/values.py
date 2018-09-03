
def v_dict():
    base_url = "http://jira.hillel.it:8080"
    values_dict = {}
    values_dict.update({'cc': 'Victor_Myasnikov'})
    values_dict.update({'wc': 'Victor_Myasnikov2'})
    values_dict.update({'auth_url': base_url + '/secure/RapidBoard.jspa?projectKey=AQAPYTHON'})
    values_dict.update({'issues_url': base_url + '/projects/AQAPYTHON/issues/'})
    values_dict.update({'my_issues': base_url + '/projects/AQAPYTHON/issues/?filter=myopenissues'})
    return values_dict
