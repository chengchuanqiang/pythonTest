import re

test = 'python is the best language , pretty good !'
p = re.findall('p+', test)
print(p)
