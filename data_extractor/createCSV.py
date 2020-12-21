import json
from DataCleaner import DataCleaner
import pandas as pd

table = pd.read_csv('template.csv')

differences = 0

# Creating table
print('Creating table...')
with open('1000sites.json', 'r') as htmls:
    with open('1000counts.json', 'r') as counts:
        htmls_list = json.load(htmls)
        counts_list = json.load(counts)
        for index in range(0, 997):
            try:
                cleaner = DataCleaner(htmls_list[index], counts_list[index])
                row = cleaner.get_dictionary()
                table = table.append(row, ignore_index=True)
            except Exception as e:
                print(e)


print('Done with {errors} differences'.format(errors=differences))

# Exporting
print('Exporting table...')
table.to_csv('998campaigns.csv')
print('Done.')