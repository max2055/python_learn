import pyperclip, re
text = pyperclip.paste()
phoneRegex = re.compile(r'''
        (\(\+86\))?
        (\s)?
        (\d{3})
        (\s|-|\.)?
        (\d{4})
        (\s|-|\.)?
        (\d{4})
        ''', re.VERBOSE)

matches = []
for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[2], groups[4], groups[6]])
        matches.append(phoneNum)
'''
text:
(+86) 18117132051
18117132052
181 1713 2053
181-1713-2054
'''
if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
else:
        print('No phone numbers or email addresses found.')
