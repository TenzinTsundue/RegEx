import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'(Mr.?s?|Ms)\.?\s\w+')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

"""
Output:
<_sre.SRE_Match object; span=(217, 228), match='Mr. Schafer'>
<_sre.SRE_Match object; span=(229, 237), match='Mr Smith'>
<_sre.SRE_Match object; span=(238, 246), match='Ms Davis'>
<_sre.SRE_Match object; span=(247, 260), match='Mrs. Robinson'>
<_sre.SRE_Match object; span=(261, 266), match='Mr. T'>

// In VsCode to run (cntr + alt + N) Key with Code Runncer extensions installed
"""