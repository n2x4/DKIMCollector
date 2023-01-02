import sys 
import datetime
import json
import eml_parser
import re
import pydig

def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

# read the file name from the command line
file_name = sys.argv[1]

# read the email file
with open(file_name, 'rb') as fhdl:
  raw_email = fhdl.read()

ep = eml_parser.EmlParser()
parsed_eml = ep.decode_email_bytes(raw_email)

# extract the email header
header = parsed_eml['header']


# extract the value of the "DKIM-Signature" field
dkim_signature = header["header"]["dkim-signature"]

# Split the data by ";" and loop through the resulting list
for dkim_string in dkim_signature:
  for item in dkim_string.split(";"):
    # Split the item by "=" and assign the first element to the key and the second element to the value
    key, *value = item.split("=")
    value = "=".join(value)
    # If the key is "d", print the value (domain)
    if key.strip() == "d":
        #print the domain detected and store in dkimdomain variable
        dkimdomain = value.strip()
        print(dkimdomain)
    # If the key is "s", print the value (selector)
    if key.strip() == "s":
        #print the selector detected and store in selector variable
        selector = value.strip()
        print(selector)

#dig the selector
dnsquery = pydig.query(selector + "._domainkey." + dkimdomain, 'TXT')

for item in dnsquery:
  if "p=" in item:
    p_index = item.index("p=")
    p_value = item[p_index+2:]
    print(p_value)
