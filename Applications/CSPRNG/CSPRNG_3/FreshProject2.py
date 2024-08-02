import os
import string
import secrets

# Define the length of the random string
length = 10

# Generate a string of random bytes
random_bytes = os.urandom(length)

# Convert the random bytes to a string
string_list = []
for i in range(10):
    random_string = ''.join([secrets.choice(string.ascii_letters + string.digits) for n in range(length)])
    string_list.append(random_string)

print(string_list)
