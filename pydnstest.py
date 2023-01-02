import pydig
import dns.resolver

selector = "20210112"
dkimdomain = "gmail.com"

dnsquery = pydig.query(selector + "._domainkey." + dkimdomain, 'TXT')
print(dnsquery)

print()
print ("Testing domain", dkimdomain, "for DKIM record with selector", selector, "...")
try:
  test_dkim = dns.resolver.resolve(selector + '._domainkey.' + dkimdomain , 'TXT')
  for dns_data in test_dkim:
    if 'DKIM1' in str(dns_data):
      print ("  [PASS] DKIM record found  :",dns_data)
except:
  print ("  [FAIL] DKIM record not found.")
