#! python3
# passman.py - An insecure password locker program
password = {'email':'25@9@1997',
            'facebook':'FacebookcuaVan',
            'apple_id':'246357cN'}

import sys,prompt_toolkit.clipboard.pyperclip
if len(sys.argv) < 2:
    print('Usage: python passman.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # frist command line arg id the account name

if account in password:
    prompt_toolkit.clipboard.pyperclip.copy(password[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('There is no account named'+ account)

