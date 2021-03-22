import json

with open('campaigns.txt', 'r') as file:
    campaigns = file.readlines()

    for campaign in campaigns:
        print(json.loads(campaign)['html'])
        break