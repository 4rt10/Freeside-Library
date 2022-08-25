#!/usr/bin/env python3

import mysql.connector as sql
import getpass


"""
GetPass will be replaced with an updated env file. This is a bunch of tests atm.
"""


# Test DB connectivity
library = sql.connect(
    host = "localhost",
    user = input("Username: "),
    password = getpass.getpass()
)
print(library)
