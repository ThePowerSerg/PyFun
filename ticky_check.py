#!/usr/bin/env python3

import re
import sys

per_user = {}
error = {}

#with open('/home/student-04-151af174803b/syslog.log', mode='r') as file:
with open('syslog.log', mode='r') as file:
    for line in file.readlines():
        check = re.search(r"INFO", line)
        if check != None:
            message = re.search(r"[A-Z][a-z]+\s[a-z\s]+", line)
            user = re.search(r"\(([^)]+)\)", line)
            if user in per_user:
                per_user[user] += 1
            else:
                per_user[user] = 1
        else:
            print("No match")
file.close()
print(per_user.items)