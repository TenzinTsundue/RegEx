import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

"""
Output:
<_sre.SRE_Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
<_sre.SRE_Match object; span=(25, 53), match='corey.schafer@university.edu'>
<_sre.SRE_Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>
"""