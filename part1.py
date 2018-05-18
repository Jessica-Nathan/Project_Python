import requests
import json
apikey='Basic ODQxZTJhMjA2Yjc1NDczY2ExMTM0ZTA5ZjMxYmE3Nzc6YmZlMGQ1ZjA4ZjY3NDdlZDg0NzdhY2U0ZWM3NDQ0YjQ='
header={'Authorization' :apikey,'Content-Type':'application/x-www-form-urlencoded'}
oid=requests.get("https://management.api.umbrella.com/v1/organizations/",headers=header)
oid=oid.json()
orgid=oid[0]["organizationId"]
print("The organisation Id is {}" .format(orgid))







