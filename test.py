from shared_count import SharedCount

import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.example.com'
        self.counters = SharedCount(self.url).get_counts()

    def test_facebook(self):
        facebook_res = self.counters['Facebook']
        self.assertTrue(type(facebook_res) is dict)

    def test_twitter(self):
        twitter_res = self.counters['Twitter']
        self.assertTrue(type(twitter_res) is dict)

    def test_linkedin(self):
        linkedin_res = self.counters['Linkedin']
        self.assertTrue(type(linkedin_res) is dict)

    def test_google_plus(self):
        google_plus_res = self.counters['Google']
        self.assertTrue(type(google_plus_res) is dict)

    def test_buffer_share(self):
        buffer_share_res = self.counters['BufferShare']
        self.assertTrue(type(buffer_share_res) is dict)

if __name__ == '__main__':
    unittest.main()
