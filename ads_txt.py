#!/usr/bin/evn python

import requests
import time
import os

# get a domain from the user

# check if the ads.txt file exists

# if exists get the content and store in a list of format
# partner, id, [DIRECT | RESELLER], (ID)
# # are used for comments
# store comments at top of file as notes
# store end of line comments as notes for that particular patner
# ignore all other comments

url_dest = input("Enter a url (domain.com) to check for ads.txt: ")
sep = os.linesep + "*" * 79

print("Checking %s for ads.txt" % url_dest)
t_start = time.time()

# attempt to find the ads.txt file on the remote server; exit if not found
try:
    requests.get("http://" + url_dest + "/ads.txt")

except requests.exceptions.ConnectionError:
    print("Something didn't quite work")
    exit()

ads_txt = requests.get("http://" + url_dest + "/ads.txt")
t_exec = time.time() - t_start
print("Ok...%s" % sep)
http_info = ads_txt.headers
for item in http_info:
    print(item, ": ", ads_txt.headers[item])

if ads_txt.status_code in([404, 403]):
    print("No ads.txt file found.")
    exit()

print("Call successful with status %s %s" % (ads_txt.status_code, sep))
print("Query took %f seconds. %s" % (t_exec, sep))
ads_txt_list = ads_txt.text.strip().split('\n')
line_num = 1
domain_set = []
for entry in ads_txt_list:
    print(line_num, entry)
    domain_set.append(entry[0])
    line_num += 1

domain_set = set(domain_set)
print("%s\n%d unique domains found in %d lines." % (sep, len(domain_set), line_num))

