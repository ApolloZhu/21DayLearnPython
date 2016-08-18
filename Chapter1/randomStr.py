import string,random

output = ''
characters = ''.join((string.ascii_letters, string.digits))
for i in range(6):
    output += random.choice(characters)
print(output)
