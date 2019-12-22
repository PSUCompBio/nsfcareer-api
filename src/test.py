#!/usr/bin/env python3
# A Test python script to add on features like html template generation etc
# import argparse
import sys
from yattag import Doc
from yattag import indent
import numpy as np
import os


doc, tag, text = Doc().tagtext()

arr = ["http://localhost:5005/simulation/results/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZV9pZCI6IkdfNEYtX3pHIiwiaWF0IjoxNTc3MDMwNTk4fQ.xsC7OVZMnCU9G06wB4PykK9uVMSp1bI4JWKU7KPdLrU/G_4F-_zG",
"http://localhost:5005/simulation/results/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZV9pZCI6InpWeUxEU0ttIiwiaWF0IjoxNTc3MDIzMzgwfQ.NCjJ559nFnaPVsDsPyeNRWXDLIl1Zq5Ue8d6-clpr6k/zVyLDSKm",
"http://localhost:5005/simulation/results/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbWFnZV9pZCI6IjlrWnVMZE1iQyIsImlhdCI6MTU3NzAyMzM4MH0.9UNkK5qxe88OSKGQuf8Au7n1KOMBF68urHuRpOdsI58/9kZuLdMbC"]

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('body'):
        for i in arr:
            with tag('iframe', src = i, width = '100%', height = "500px"):
                text("")


# for i in arr:
#     with tag('iframe', src = i, width = '100%', height = "60px"):
#         text("")

result = indent(doc.getvalue())
print(result)

try:
    os.mkdir("test")
except OSError:
    print ("Creation of the directory %s failed")
else:
    print ("Successfully created the directory %s ")
    file= open("test/my.html","w")
    file.write(result)
    file.close()

        # parser = argparse.ArgumentParser(description='Utility package to generate simulation data')
        # parser.add_argument('--filename', default=None, type=str, help="Path to sensor file")
        # parser.add_argument('--user', default=None, type=str, help="You account username")
        # parser.add_argument('--password', default=None, type=str, help="You account Password")
        #
        #
        # args = parser.parse_args()
        # if (args.user  == None or args.password == None or args.filename == None):
        #     parser.print_help()
        #     sys.exit(0)
        # else:
        #     print("HELLO");
        # print(args.user, args.password, args.filename)
