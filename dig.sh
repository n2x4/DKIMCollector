dig selector._domainkey.yourdomain txt | sed -n '/IN TXT/{N;s/.*p=\([^;]*\).*/\1/;p}' | sed -n '1p'
