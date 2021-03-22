import json
from DataCleaner import DataCleaner
import pandas as pd

table = pd.read_csv('template.csv')

differences = 0

# Creating table
print('Creating table...')
with open('campaigns.txt', 'r') as file:
    campaigns = file.readlines()
    for campaign in campaigns:
        html = json.loads(campaign)['html']
        counts = json.loads(campaign)['counts']
        if not counts or not html:
            continue
        cleaner = DataCleaner(html, counts)
        row = cleaner.get_dictionary()
        table = table.append(row, ignore_index=True)

print('Done with {errors} differences'.format(errors=differences))

# Exporting
print('Exporting table...')
table.to_csv('test_campaigns.csv')
print('Done.')
