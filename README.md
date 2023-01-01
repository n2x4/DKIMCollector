# DKIMCollector
Preserving historical DKIM records for future analysis 

selectorextract.py contains the python code to extract the selector record from an email header 

dig.sh contains the command for querying DNS for the DKIM public key (found from the selectorextract.py) for a given domain
