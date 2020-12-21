with open('1000counts.txt', 'r') as f:
    raw_counts = f.readlines()
    counts = [x.replace('https://gateway.gofundme.com/web-gateway/v1/feed/', '').replace('/counts', '') for x in
              raw_counts]

with open('1000htmls.txt', 'r') as f:
    raw_htmls = f.readlines()
    htmls = [x.replace('https://www.gofundme.com/f/', '') for x in raw_htmls]

diff_found = False

for index in range(0, 1000):
    count = counts[index]
    html = htmls[index]
    if count != html:
        print('difference at: {count} and {html}'.format(count=counts[index], html=htmls[index]))
        diff_found = True

if not diff_found:
    print('They are the same.')
