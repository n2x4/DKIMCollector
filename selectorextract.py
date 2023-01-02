import sys
import datetime
import json
import eml_parser
import re
import pydig
import datetime

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
        print("Domain Evaluated - " + dkimdomain)
    # If the key is "s", print the value (selector)
    if key.strip() == "s":
        #print the selector detected and store in selector variable
        selector = value.strip()
        print("Selector DNS - " + selector)

#dig the selector
dnsquery = pydig.query(selector + "._domainkey." + dkimdomain, 'TXT')

#Extract p value only and clean up any quotes or spaces dig adds to the output

for item in dnsquery:
  if "p=" in item:
    p_index = item.index("p=")
    p_value = item[p_index+2:]
    p_value = p_value.strip('"')
    p_value = p_value.replace('" "', '')
    print("DKIM - " + p_value)

#current date
current_date = datetime.date.today()
print(current_date)

#write to file where the filename is the domain and selector and the contents is the DKIM p value
with open (dkimdomain +"_"+ selector, 'w') as f:
  f.write("DKIM - " + p_value)
