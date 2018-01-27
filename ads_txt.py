import requests
import time
import os

url_dest = input("Enter a url (domain.com) to check for ads.txt: ")
sep = os.linesep + "*" * 79

print("Checking %s for ads.txt" % url_dest)
t_start = time.time()

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

