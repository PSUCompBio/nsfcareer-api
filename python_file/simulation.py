#!/usr/bin/env python3
import json
import requests
import base64
import sys
from datetime import datetime
import numpy as np
import argparse
import os
from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()


# Setting up Argument parsing
parser = argparse.ArgumentParser(description='Utility package to generate simulation data')
parser.add_argument('--filename', default=None, type=str, help="Path to sensor file")
parser.add_argument('--user', default=None, type=str, help="Username")
parser.add_argument('--password', default=None, type=str, help="Password")
parser.add_argument('--endpoint', default=None, type=str, help="Simulation Endpoint")

args = parser.parse_args()

# Checking if arguments are not empty
if (args.filename == None or args.user == None or args.password ==None):
    parser.print_help()
    sys.exit(0)

print("========================================================================");

print()
filename = args.filename
username = args.user
password = args.password
api = args.endpoint

print("========================================================================");
print("| -> Please wait, Uploading Data                                        |");
print("========================================================================");
# Reading file and converting it to base64 format
with open(filename, 'rb') as fd:
    b64data = base64.b64encode(fd.read())
    data = {'upload_file': b64data , 'user_name' : username , 'password' : password}

    print("========================================================================");
    print("| -> Response Received                                                  |");
    print("========================================================================");
    # Calling the api to carry out simulations
    r = requests.post(api, data = data)

    # Logging response
response = json.loads(r.text);
if response["message"] == "success":
    # Iterate over the Image URLS & Write it in File-with timestamp
    print();
    # Using for loop to generate the HTML
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('body'):
            for i in response["image_url"]:
                with tag('iframe', src = i, width = '100%', height = "500px"):
                    text("")

    # Folder name in which file will be stored
    filename = datetime.now().strftime("sr-%Y%m%d-%H%M%S")
    result = indent(doc.getvalue())
    try:
        os.mkdir(filename)
    except OSError:
        print ("Failed to Create Folder to store the html")
    else:
        print("| -> HTML File generated in : " + filename + "/index.html")
        file= open( filename + "/index.html","w")
        file.write(result)
        file.close()
else:
    print(r.text)
print()
print("========================================================================");