from unittest import TestCase

from DataCleaner import DataCleaner


class TestDataCleaner(TestCase):
    cleaner = DataCleaner('sites.json', 'counts.json')
    jsn = cleaner.get_json()

    def test__open_file(self):
        pass

    def testIfGetsURL(self):
        url = self.jsn.get('url')
        assert url == 'https://www.gofundme.com/f/angel-yang-cassidy-yang'

    def testIfGetsTitle(self):
        title = self.cleaner.get_title()
        assert title == 'Angel Yang & Cassidy Yang'

    def testIfCategory(self):
        category = self.cleaner.get_category()
        assert category == 'Funerals & Memorials'

    def testIfCategoryURL(self):
        url = self.cleaner.get_category_url()
        assert url == 'https://www.gofundme.com/discover/memorial-fundraiser'

    def testIfGoal(self):
        goal = self.cleaner.get_goal()
        assert goal == 100000

    def testIfRaised(self):
        raised = self.cleaner.get_raised()
        assert raised == 254295

    def testIfCurrency(self):
        currency = self.cleaner.get_currency()
        assert currency == 'USD'

    def testIfCountry(self):
        country = self.cleaner.get_country()
        assert country == 'US'

    def testIfCity(self):
        city = self.cleaner.get_city()
        assert city == 'Naperville, IL'

    def testIfDescription(self):
        description = self.cleaner.get_description()
        assert 'Angel Yang (29) and Cassidy Yang (26)' in description

    def testIfCreationDate(self):
        creation_date = self.cleaner.get_creation_date()
        assert creation_date == '2020-12-10T20:35:54-06:00'

    # Should have more tests for different types of organizers
    def testIfOrganizerIsPerson(self):
        organizer = self.cleaner.get_organizer()
        expected = {'first_name': 'Love',
                    'last_name': 'AngeCassi',
                    'charity': '',
                    'business': '',
                    'team': 'Friends of Yang Family',
                    'partner': '',
                    }
        intersection = set(organizer).intersection(set(expected))

        assert len(intersection) == 6

    def testIfBeneficiary(self):
        beneficiary = self.cleaner.get_beneficiary()
        assert beneficiary == ''

    # Counts tests
    def testIfGetsTotalPhotos(self):
        total_photos = self.cleaner.get_total_photos()
        assert total_photos == 11

    def testIfDictionaryMatches(self):
        dictionary = self.cleaner.get_dictionary()
        expected = {
            'Date and Time (YY-MM-DD)': '2020-12-17 14:48:59.902960',
            'URL': 'https://www.gofundme.com/f/angel-yang-cassidy-yang',
            'Title': 'Angel Yang & Cassidy Yang',
            'Category': 'Funerals & Memorials',
            'Category URL': 'https://www.gofundme.com/discover/memorial-fundraiser',
            'Goal': 100000,
            'Raised': 254295,
            'Currency': 'USD',
            'Country': 'US',
            'City': 'Naperville, IL',
            'Description': "We are extremely saddened to learn that Angel Yang (29) and Cassidy Yang (26) have lost their\u2026 Love AngeCassi needs your support for Angel Yang & Cassidy Yang",
            'Creation_date (YY-MM-DD)': '2020-12-10T20:35:54-06:00',
            'Organizers': {'first_name': 'Love',
                           'last_name': 'AngeCassi',
                           'charity': '',
                           'business': '',
                           'team': 'Friends of Yang Family',
                           'partner': '',
                           },
            'No. of photos': 11,
            'No. of community photos': 2,
            'No. of donations': 2681,
            'No. of unique donors': 2658,
            'Amount raised unattributed': 258025,
            'No. of donations unattributed': 2664,
            'No. of campaign hearts': 2683,
            'No. of social media shares': 786,
        }
