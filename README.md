# WebVulnScannerScripts

## script check_reflected_xss

Tested on DVWA App
for now security level low 
```
# Script will as for user input
python3 check_reflected_xss.py 

python3 check_reflected_xss.py --url "http://localhost/vulnerabilities/xss_r" --param_value "name" --cookie_name "PHPSESSID" --cookie_value "db2rictlo4rv5ngi2m45qt4jc2" --security_name "security" --security_value "low" --show_response_text 


python3 check_reflected_xss.py --url "http://localhost/vulnerabilities/xss_s" --param_value "mtxMessage" --cookie_name "PHPSESSID" --cookie_value "db2rictlo4rv5ngi2m45qt4jc2" --security_name "security" --security_value "low"
```
