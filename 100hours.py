import requests
import json
import time
import os

now_epoch = int(time.time())
start_epoch = 1640995200 # 00:00:00 1st Jan 2022
end_epoch = 1672531199 # 23:59:59 31st Dec 2022

percentage_through_year = (now_epoch - start_epoch) / (end_epoch - start_epoch) * 100

database_id = os.environ.get('NOTION_DATABASE_ID')
api_key = os.environ.get('NOTION_API_KEY')

url = f'https://api.notion.com/v1/databases/{database_id}/query'

payload = {"page_size": 500}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json",
    "Authorization": api_key
}

response = requests.request("POST", url, json=payload, headers=headers)

goal_data = json.loads(response.text)
values = [percentage_through_year]
# this is gross and I'm sorry
values.append(goal_data["results"][0]["properties"]["Duration (Minutes)"]["rollup"]["number"])
values.append(goal_data["results"][0]["properties"]["Completion"]["formula"]["number"] * 100)
values.append(goal_data["results"][1]["properties"]["Duration (Minutes)"]["rollup"]["number"] * 2)
values.append(goal_data["results"][1]["properties"]["Completion"]["formula"]["number"] * 100 * 2)
values.append(goal_data["results"][2]["properties"]["Duration (Minutes)"]["rollup"]["number"])
values.append(goal_data["results"][2]["properties"]["Completion"]["formula"]["number"] * 100)
values.append(goal_data["results"][5]["properties"]["Duration (Minutes)"]["rollup"]["number"])
values.append(goal_data["results"][5]["properties"]["Completion"]["formula"]["number"] * 100)
values.append(goal_data["results"][4]["properties"]["Duration (Minutes)"]["rollup"]["number"])
values.append(goal_data["results"][4]["properties"]["Completion"]["formula"]["number"] * 100)
values.append(goal_data["results"][3]["properties"]["Duration (Minutes)"]["rollup"]["number"])
values.append(goal_data["results"][3]["properties"]["Completion"]["formula"]["number"] * 100)

with open('content/100-hours.md', 'r') as page:
    pageText = page.read()
    pageText = pageText.replace(
        'hours: []', f'hours: {values}')
with open('content/100-hours.md', 'w') as page:
    page.write(pageText)
