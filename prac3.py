import random
import string
size=int(input("enter the size of password: "))
allchar=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(allchar)for i in range(size))
print(password)