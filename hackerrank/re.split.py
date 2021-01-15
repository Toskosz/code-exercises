#import re

# entries = re.split("\n+", text)

#s = input()
#regex_pattern = r""	# Do not delete 'r'.
p1 = ','
p2 = '.'
#x = re.split(p1, s)
#x= re.split(p2,x)
#print(x)



regex_pattern = r"\,|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))