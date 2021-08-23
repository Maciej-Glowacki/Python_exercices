import re

pattern = re.compile(r"[A-Za-z0-9$%#@!]{8,}")

password = 'sdkhkhds!@kjsd@'
password2 = 'ksd*&'

check = pattern.fullmatch(password)
check2 = pattern.fullmatch(password2)

print(check)
print(check2)