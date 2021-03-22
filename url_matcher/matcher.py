import json

campaign_counter = 0
campaigns = {}


def find_match(url, counts):
    for count in counts:
        if count['url'] == url:
            matched = count
            counts.remove(count)
            return matched


print("Reading JSONs...")
with open('test_sites.json', 'r') as file1:
    with open('test_counts.json', 'r') as file2:
        counts = json.load(file2)
        sites = json.load(file1)
        print("Done.")

        print("Start matching campaigns...")
        for site in sites:
            url = site['url']
            count = find_match(url, counts)
            campaign_counter = campaign_counter + 1
            campaigns[campaign_counter] = {}
            campaigns[campaign_counter]['html'] = site
            campaigns[campaign_counter]['counts'] = count
        print("Done.")

        print('Writing campaigns...')
        with open('campaigns.txt', 'w') as file3:
            for index in range(1, len(campaigns)):
                file3.write(json.dumps(campaigns[index]) + '\n')
        print("Done.")