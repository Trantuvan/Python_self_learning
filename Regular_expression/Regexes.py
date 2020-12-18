import re

# this is a Regexes object
# r/ is a draw string
phoneNumRegexes = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegexes.search('my phone number is 036-915-8125')
print('Phone number found: ', mo.group())


