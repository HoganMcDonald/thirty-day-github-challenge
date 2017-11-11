# Thirty Day GitHub Challenge

I built the api, but no front end. It's hosted on an AWS Lambda with open access.

Make a POST request to:
https://3wp6tucn35.execute-api.us-east-1.amazonaws.com/prod/30daygithub

with a request body that looks like this:
{
  "usernames": "hoganmcdonald pete-wildberger",
  "days": "5"
}

Separate usernames with a space and you will get results back for each person you listed. However, because the api is scraping each users web page, a large list could result in a lot of latency. the Lambda will time out at a certain point. I could allocate more resources to it, but not for free.

response should look like:

[
  {
    \"user\": \"hoganmcdonald\",
    \"total_commits\": 78,
    \"days_active\": 18,
    \"percentage_active\": 0.4
  },
  {
    \"user\": \"pete-wildberger\",
    \"total_commits\": 146,
    \"days_active\": 32,
    \"percentage_active\": 0.7111111111111111
  }
]

## instructions for challenge

1. Fork this repository
2. Use React to create a project that allows input of a GitHub username (e.g. lukeschlangen) and returns their:
  - Percentage of last 30 days with a contribution (green square)
  - Streak (number of days in a row) with a green square
3. I haven't solved this. It's a real problem I have. Don't know if a solution exists... good luck!

## Hard Mode

Allow a user to check starting from a specific day (not just today).

## Resources

How to get a hold of the data you need:

- Lecture from graduation day: [https://github.com/PrimeAcademy/betelgeuse-introduction-to-react](https://github.com/PrimeAcademy/betelgeuse-introduction-to-react)
- Example React Repo with Server: [https://github.com/PrimeAcademy/betelgeuse-react-postgres-crd-app](https://github.com/PrimeAcademy/betelgeuse-react-postgres-crd-app)
- How to retreive and parse the data on the server (aka, why we can't use the normal GitHub API for this) on Stack Overflow: [https://stackoverflow.com/questions/46881235/github-rate-limiting-preventing-return-of-user-commit-history](https://stackoverflow.com/questions/46881235/github-rate-limiting-preventing-return-of-user-commit-history)
- How to make request directly in React (kind of hacky) on Stack Overflow: [https://stackoverflow.com/questions/47027256/react-axios-cheerio-parsing-of-github-response](https://stackoverflow.com/questions/47027256/react-axios-cheerio-parsing-of-github-response)
