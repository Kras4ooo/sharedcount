import urllib
import urllib2

import json

class SharedCount(object):
    def __init__(self, url):
        self.url = url

    def get_counts(self):
        dict_counts = {
                        'Facebook': self.get_facebook_count(),
                        'Twitter': self.get_twitter_count(),
                        'Linkedin': self.get_linkedin_count(),
                      }
        return dict_counts

    def get_linkedin_count(self):
        query = "http://www.linkedin.com/countserv/count/share?url=%s&format=json" % urllib.quote(self.url)
        return json.loads(urllib2.build_opener().open(query).read())

    def get_google_plus_count(self):
        query = "http://cdn.api.twitter.com/1/urls/count.json?url=%s" %  urllib.quote(self.url)
        return json.loads(urllib2.build_opener().open(query).read())

    def get_twitter_count(self):
        query = "http://cdn.api.twitter.com/1/urls/count.json?url=%s" %  urllib.quote(self.url)
        return json.loads(urllib2.build_opener().open(query).read())

    def get_facebook_count(self):
        fql = "SELECT url, normalized_url, share_count, like_count, comment_count, " \
		"total_count, commentsbox_count, comments_fbid, click_count FROM " \
		"link_stat WHERE url = '%s'" % self.url

        query = "https://api.facebook.com/method/fql.query?format=json&query=%s" % urllib.quote(fql)
        return json.loads(urllib2.build_opener().open(query).read())[0]
