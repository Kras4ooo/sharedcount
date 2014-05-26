sharedcount
===========

This is a small bookcase that link returns filed by attendance reported by the following social networks: Facebook, Twitter and Linkedin. How can use the library: 

```
from shared_count import SharedCount 
counters = SharedCount ('http://www.example.com'). get_counts () 

facebook = counters ['Facebook'] 
twitter = counters ['Twitter'] 
linkedin = counters ['Linkedin']
```
