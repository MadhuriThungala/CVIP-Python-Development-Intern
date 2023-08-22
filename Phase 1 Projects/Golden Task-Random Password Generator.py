import random
Symbols="!@#$%^&*_,./"
Numbers="1234567890"
Lowercase_letters="abcdefghijklmnopqrstuvwxyz"
Uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string=Symbols+Numbers+Lowercase_letters+Uppercase_letters
length=10
Password="".join(random.sample(string,length))
print("Generated random password is:"+Password)
