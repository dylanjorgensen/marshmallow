'''
 in the context of data storage, serialization is the process of translating data structures or object state into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and reconstructed later in the same or another computer environment
'''


'''
- Python provides built-in JSON libraries to encode and decode JSON.
- In Python 2.5, the simplejson module is used, whereas in Python 2.7

- The object datastructure, in Python, consists of lists and dictionaries nested inside each other. The object datastructure allows one to use python methods (for lists and dictionaries) to add, list, search and remove elements from the datastructure.
'''

import json

#
# To encode a data structure to JSON, use the "dumps" method.
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)  # This method takes an object and returns a String:
print(type(json_string))


'''
- Python supports a Python proprietary data serialization method called pickle (and a faster
alternative called cPickle).

You can use it exactly the same way.
'''
import cPickle
pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
print cPickle.loads(pickled_string)
print(type(pickled_string))