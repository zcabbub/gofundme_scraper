import json

class DataCleaner:

    def __init__(self, file):
        self.file = file
        self.jsn = self._open_file()
        self.campaignJSON = self.jsn['feed']['campaign']

    def _open_file(self):
        with open(self.file) as f:
            return (json.load(f))[0]

    # GETTERS
    def get_json(self):
        return self.jsn

    def get_campaignJSON(self):
        return self.campaignJSON

    def get_title(self):
        jsn = self.get_campaignJSON()
        return jsn.get('fund_name')

    def get_category(self):
        pass

    def get_category_url(self):
        pass

    def get_goal(self):
        pass

    def get_raised(self):
        pass

    def get_currency(self):
        pass

    def get_country(self):
        pass

    def get_city(self):
        pass

    def get_description(self):
        pass

    def get_creation_date(self):
        pass

    def get_organizers(self):
        pass

    def get_beneficiary(self):
        pass

    ## from Counts
    def get_total_photos(self):
        pass

    def get_total_comm_photos(self):
        pass

    def get_total_donations(self):
        pass

    def get_total_unique_donors(self):
        pass

    def get_amount_raised_unattributed(self):
        pass

    def get_total_donations_unattributed(self):
        pass

    def get_hearts(self):
        pass

    def get_shares(self):
        pass

    def get_dictionary(self):
        jsn = self.get_json()
        dictionary = {'Date and Time (YY-MM-DD)': jsn['date_time'],
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
                      'Organizers': self.get_organizers(),
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
# feed_campaign_beneficiary_is_placeholder_bene ??import json

class DataCleaner:

    def __init__(self, file):
        self.file = file
        self.jsn = self._open_file()
        self.campaignJSON = self.jsn['feed']['campaign']

    def _open_file(self):
        with open(self.file) as f:
            return (json.load(f))[0]

    # GETTERS
    def get_json(self):
        return self.jsn

    def get_campaignJSON(self):
        return self.campaignJSON

    def get_title(self):
        jsn = self.get_campaignJSON()
        title = jsn.get('fund_name')
        return title

    def get_category(self):
        jsn = self.get_json()
        category = jsn.get('category_text')
        return category

    def get_category_url(self):
        jsn = self.get_json()
        url = 'https://www.gofundme.com' + jsn.get('category_URL')
        return url

    def get_goal(self):
        jsn = self.get_campaignJSON()
        goal = jsn.get('goal_amount')
        return goal

    def get_raised(self):
        jsn = self.get_campaignJSON()
        raised = jsn.get('current_amount')
        return raised

    def get_currency(self):
        jsn = self.get_campaignJSON()
        currency = jsn.get('currencycode')
        return currency

    def get_country(self):
        jsn = self.get_campaignJSON()
        country = jsn.get('location').get('country')
        return country

    def get_city(self):
        jsn = self.get_campaignJSON()
        city = jsn.get('location').get('city')
        return city

    def get_description(self):
        jsn = self.get_campaignJSON()
        description = jsn.get('fund_description')
        return description

    def get_creation_date(self):
        jsn = self.get_campaignJSON()
        creation_date = jsn.get('created_at')
        return creation_date

    def get_organizer(self):
        jsn = self.get_campaignJSON()
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
        jsn = self.get_campaignJSON()
        if jsn.get('has_beneficiary') == 'false':
            beneficiary = ''
        else:
            beneficiary = {'first_name': jsn.get('beneficiary').get('first_name'),
                           'last_name': jsn.get('beneficiary').get('last_name')
                           }
        return beneficiary

    ## from Counts
    def get_total_photos(self):
        pass

    def get_total_comm_photos(self):
        pass

    def get_total_donations(self):
        pass

    def get_total_unique_donors(self):
        pass

    def get_amount_raised_unattributed(self):
        pass

    def get_total_donations_unattributed(self):
        pass

    def get_hearts(self):
        pass

    def get_shares(self):
        pass

    def get_dictionary(self):
        jsn = self.get_json()
        dictionary = {'Date and Time (YY-MM-DD)': jsn['date_time'],
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