from bs4 import BeautifulSoup as soup
import requests
import json


print('Loading function')


def lambda_handler(event, context):
    res = []
    users = event["usernames"].split(' ')

    for user in users:
        res_current = {
            "user": user,
            "total_commits": 0,
            "days_active": 0,
            "percentage_active": 0
        }
        base_url = 'https://github.com/{}'.format(user)
        response = requests.get(base_url)

        page_soup = soup(response.text, 'html.parser')
        weeks = page_soup.findAll('rect', {'class': 'day'})
        print(weeks[-1])

        day_max = -1 * int(event["days"])
        day = -1
        while day != day_max:
            # days active
            if weeks[day]['fill'] != '#ebedf0':
                res_current["days_active"] += 1
            # total commits
            res_current["total_commits"] += int(weeks[day]["data-count"])
            day -= 1
        res_current["percentage_active"] = res_current["days_active"] / int(event["days"])
        res.append(res_current)
    print(res)
    return json.dumps(res)


# lambda_handler({"usernames": "hoganmcdonald pete-wildberger", "days": "5"}, 'context')
