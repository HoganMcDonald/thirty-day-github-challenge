from bs4 import BeautifulSoup as soup
import requests
import json


print('Loading function')


# def lambda_handler(event, context):
def lambda_handler(event):
    res = {}
    users = event["usernames"].split(' ')

    for user in users:
        base_url = 'https://github.com/{}'.format(user)
        response = requests.get(base_url)

        page_soup = soup(response.text, 'html.parser')
        weeks = page_soup.findAll()

        days = 30
        while days >= 0:

            days -= 1

    return json.dumps(res)


lambda_handler({"usernames": "hoganmcdonald pete-wildberger"})
