import json


def open_file(file):
    with open(file) as f:
        return (json.load(f))[0]


class DataCleaner:
    def __init__(self, html_file, counts_file):
        # self.html_jsn = open_file(html_file)
        # self.counts_jsn = open_file(counts_file)['counts']
        if html_file.get('url') == counts_file.get('url'):
            self.html_jsn = html_file
            self.counts_jsn = counts_file['counts']
        else:
            raise Exception("AssertionError at {url}".format(url=html_file.get('url')))

    # GETTERS
    def get_json(self):
        return self.html_jsn

    def get_title(self):
        jsn = self.get_json()['data']
        title = jsn.get('fund_name')
        return title

    def get_category(self):
        jsn = self.get_json()
        category = jsn.get('category')
        return category

    def get_category_url(self):
        jsn = self.get_json()
        url = 'https://www.gofundme.com' + jsn.get('category_URL')
        return url

    def get_goal(self):
        jsn = self.get_json()['data']
        goal = jsn.get('goal_amount')
        return goal

    def get_raised(self):
        jsn = self.get_json()['data']
        raised = jsn.get('current_amount')
        return raised

    def get_currency(self):
        jsn = self.get_json()['data']
        currency = jsn.get('currencycode')
        return currency

    def get_country(self):
        jsn = self.get_json()['data']
        country = jsn.get('location').get('country')
        return country

    def get_city(self):
        jsn = self.get_json()['data']
        city = jsn.get('location').get('city')
        return city

    def get_description(self):
        jsn = self.get_json()['data']
        description = jsn.get('fund_description')
        return description

    def get_creation_date(self):
        jsn = self.get_json()['data']
        creation_date = jsn.get('created_at')
        return creation_date

    def get_organizer(self):
        jsn = self.get_json()['data']
        business = jsn.get('business').get('name')
        team = jsn.get('team').get('name')
        charity = jsn.get('charity').get('name')
        partner = jsn.get('partner').get('name')
        organizer = {
            'first_name': jsn.get('user_first_name'),
            'last_name': jsn.get('user_last_name'),
            'charity': charity,
            'business': business,
            'team': team,
            'partner': partner,
        }
        return organizer

    def get_beneficiary(self):
        jsn = self.get_json()['data']
        if not jsn.get('has_beneficiary'):
            beneficiary = ''
        else:
            beneficiary = {'first_name': jsn.get('beneficiary').get('first_name'),
                           'last_name': jsn.get('beneficiary').get('last_name'),
                           }
        return beneficiary

    ## from Counts
    def get_total_photos(self):
        total_photos = self.counts_jsn.get('total_photos')
        return total_photos

    def get_total_comm_photos(self):
        total_community_photos = self.counts_jsn.get('total_community_photos')
        return total_community_photos

    def get_total_donations(self):
        total_donations = self.counts_jsn.get('total_donations')
        return total_donations

    def get_total_unique_donors(self):
        total_unique_donors = self.counts_jsn.get('total_unique_donors')
        return total_unique_donors

    def get_amount_raised_unattributed(self):
        amount_raised_unattributed = self.counts_jsn.get('amount_raised_unattributed')
        return amount_raised_unattributed

    def get_total_donations_unattributed(self):
        number_of_donations_unattributed = self.counts_jsn.get('number_of_donations_unattributed')
        return number_of_donations_unattributed

    def get_hearts(self):
        hearts = self.counts_jsn.get('campaign_hearts')
        return hearts

    def get_shares(self):
        shares = self.counts_jsn.get('social_share_total')
        return shares

    def get_dictionary(self):
        jsn = self.get_json()
        dictionary = {
            'Date and Time (YY-MM-DD)': jsn.get('data_date'),
            'URL': jsn.get('url'),
            'Title': self.get_title(),
            'Category': self.get_category(),
            'Category URL': self.get_category_url(),
            'Goal': self.get_goal(),
            'Raised': self.get_raised(),
            'Currency': self.get_currency(),
            'Country': self.get_country(),
            'City': self.get_city(),
            'Description': self.get_description(),
            'Creation_date (YY-MM-DD)': self.get_creation_date(),
            'Organizers': self.get_organizer(),
            'No. of photos': self.get_total_photos(),
            'No. of community photos': self.get_total_comm_photos(),
            'No. of donations': self.get_total_donations(),
            'No. of unique donors': self.get_total_unique_donors(),
            'Amount raised unattributed': self.get_amount_raised_unattributed(),
            'No. of donations unattributed': self.get_total_donations_unattributed(),
            'No. of campaign hearts': self.get_hearts(),
            'No. of social media shares': self.get_shares(),
        }
        return dictionary

# feed_campaign_charity_id
# feed_campaign_is_charity


# organizers
# feed_campaign_profile_url
# feed_campaign_user_first_name
# feed_campaign_user_last_name
# feed_campaign_is_business
# feed_campaign_is_team
# feed_campaign_is_partner

# beneficiary
# feed_campaign_has_beneficiary (if NOT organizer)
# feed_campaign_beneficiary_is_placeholder_bene ??
