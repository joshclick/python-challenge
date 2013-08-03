# http://www.pythonchallenge.com/pc/def/linkedlist.html

import urllib2
import re

url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
olddest = '12345'
dest = '8022'

for x in range(400):
	response = urllib2.urlopen(url_base + dest).read()
	dest = re.findall(r'\d+', response)[-1]
	print response
