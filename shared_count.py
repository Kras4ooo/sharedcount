import urllib
import urllib2

from bs4 import BeautifulSoup

import json

class SharedCount(object):
    def __init__(self, url):
        self.url = url

    def get_counts(self):
        dict_counts = {
                        'Facebook': self.get_facebook_count(),
                        'Twitter': self.get_twitter_count(),
                        'Linkedin': self.get_linkedin_count(),
                        'Google': self.get_google_count(),
                        'BufferShare': self.get_buffer_share_count(),
                       #TODO: 'Pinterest': self.get_pinterest_count(),
                      }
        return dict_counts

    def get_linkedin_count(self):
        query = "http://www.linkedin.com/countserv/count/share?url=%s&format=json" % urllib.quote(self.url)
        return self.to_json(query)

    def get_google_plus_count(self):
        query = "http://cdn.api.twitter.com/1/urls/count.json?url=%s" %  urllib.quote(self.url)
        return self.to_json(query)

    def get_twitter_count(self):
        query = "http://cdn.api.twitter.com/1/urls/count.json?url=%s" %  urllib.quote(self.url)
        return self.to_json(query)

    def get_facebook_count(self):
        fql = "SELECT url, normalized_url, share_count, like_count, comment_count, " \
		"total_count, commentsbox_count, comments_fbid, click_count FROM " \
		"link_stat WHERE url = '%s'" % self.url

        query = "https://api.facebook.com/method/fql.query?format=json&query=%s" % urllib.quote(fql)
        return self.to_json(query)[0]

    def get_google_count(self):
        query = "https://plusone.google.com/_/+1/fastbutton?url=%s" % urllib.quote(self.url)
        response = urllib2.urlopen(query)
        soup = BeautifulSoup(response.read())
        data = soup.find(id="aggregateCount").text
        count = {"share_count": data}
        return json.loads(json.dumps(count))

    def get_buffer_share_count(self):
        query = "https://api.bufferapp.com/1/links/shares.json?url=%s" % urllib.quote(self.url)
        return self.to_json(query)

    def get_pinterest_count(self):
        query = "https://api.pinterest.com/v1/urls/count.json?callback=jsonp&url=%s" % urllib.quote(self.url)
        return self.to_json(query)

    def to_json(self, query):
        return json.loads(urllib2.build_opener().open(query).read())
