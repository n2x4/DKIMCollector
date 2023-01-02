import pydig
import dns.resolver

selector = "20210112"
dkimdomain = "gmail.com"

dnsquery = pydig.query(selector + "._domainkey." + dkimdomain, 'TXT')
print(dnsquery)

dnsquery2 = dns.resolver.resolve(selector + "._domainkey." + dkimdomain, 'TXT')
