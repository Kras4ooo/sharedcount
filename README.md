sharedcount
===========

This is a small library that link returns filed by attendance reported by the following social networks: Facebook, Twitter and Linkedin. How can use the library: 

```
from shared_count import SharedCount 
counters = SharedCount ('http://www.example.com'). get_counts () 

facebook = counters ['Facebook'] [['normalized_url'], ['commentsbox_count'], ['click_count'], ['url'], ['total_count'], ['comment_count'], ['like_count'], ['comments_fbid'], ['share_count']]
twitter = counters ['Twitter'] [['count'], ['url']]
linkedin = counters ['Linkedin'] [['count'], ['url'], ['fCntPlusOne'], ['fCnt']]
```
