import requests
import json
apikey='Basic ODQxZTJhMjA2Yjc1NDczY2ExMTM0ZTA5ZjMxYmE3Nzc6YmZlMGQ1ZjA4ZjY3NDdlZDg0NzdhY2U0ZWM3NDQ0YjQ='
header={'Authorization' :apikey,'Content-Type':'application/x-www-form-urlencoded'}
oid=requests.get("https://management.api.umbrella.com/v1/organizations/",headers=header)
oid=oid.json()
orgid=str(oid[0]["organizationId"])
print("The organisation Id is {}" .format(orgid))


def List_Network_devices():
	print (header)
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid +"/networkdevices/ ",headers=header)
	list_devices=list_devices.json()
	return list_devices

print(List_Network_devices())
	







