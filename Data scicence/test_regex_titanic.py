import re

urls = ''' https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(2))

text = 'Thayer, Mr. John Borland Jr'

# pattern = re.compile(r'(\w+)\,\s(\w+\.)\s[a-zA-Z]+')
# Nhin text nhan thay Mr. la chu duy nhat co '.' theo sau nen su dung duoc
pattern = re.compile(r'(\w+)\.')
matches = pattern.finditer(text)

for match in matches:
    print(match)
