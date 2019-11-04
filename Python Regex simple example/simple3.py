import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

"""
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

"""
"""
Output:
google.com
coreyms.com
youtube.com
nasa.gov
"""

matches = pattern.finditer(urls)

for match in matches:
     print(match.group(2))

"""
Output:
google
coreyms
youtube
nasa
"""