import os, random, string, pyperclip, time

input('Press enter to generate a random password...')
print('A new password will now be generated...')

time.sleep(1)
length = 15
chars = string.ascii_letters + string.digits + '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~")'
random.seed = (os.urandom(1024))
pwd = ''.join(random.choice(chars) for i in range(length))
pyperclip.copy(pwd)
print (pwd)
print('This password is now copied to your clipboard!\nPress Ctl + V to paste the new password.')

time.sleep(5)
