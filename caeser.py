MAX_KEY_SIZE = 26
def getKey():
 key = 0
 while True:
 print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
 key = int(input())
 if (key >= 1 and key <= MAX_KEY_SIZE):
 return key
def getTranslatedMessage(mode, message, key):
 if mode[0] == 'd':
 key = -key
 translated = ''
 for symbol in message:
 if symbol.isalpha() or symbol.isdigit():
 if symbol.isdigit():
 symbol=str(symbol)
 num = ord(symbol)
 num += key
 if symbol.isupper():
 if num > ord('Z'):
 num -= 26
 elif num < ord('A'):
 num += 26
 elif symbol.islower():
 if num > ord('z'):
 num -= 26
 elif num < ord('a'):
 num += 26
 translated += chr(num)
 else:
 translated += symbol
 return translated