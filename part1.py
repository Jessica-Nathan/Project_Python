import requests
import json
apikey='Basic ODQxZTJhMjA2Yjc1NDczY2ExMTM0ZTA5ZjMxYmE3Nzc6YmZlMGQ1ZjA4ZjY3NDdlZDg0NzdhY2U0ZWM3NDQ0YjQ='
header={'Authorization' :apikey,'Content-Type':'application/x-www-form-urlencoded'}
oid=requests.get("https://management.api.umbrella.com/v1/organizations/",headers=header)
oid=oid.json()
orgid=str(oid[0]["organizationId"])
print("The organisation Id is {}" .format(orgid))
print(" ")

def List_Network_devices():
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/",headers=header)
	list_dev=list_devices.json()
	print("The list of Network Devices of the Organisation") 
	return list_dev

print(List_Network_devices())
print(" ")
	


def create_network_devices():

	body_net=	{"name": "1995",
		"model":"summa",
		"macAddress":"0123456789ab",
		"label":"Label1",
		"serialNumber":"12345a",
		"tag":"your tag"
	}
	body_post=requests.post("https://management.api.umbrella.com/v1/organizations/"+orgid+"/networkdevices",json.dumps(body_net), headers=header)
	body_post=body_post.json()
	return body_post 

print(create_network_devices())

	

def  List_policies():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/150384748/policies", headers=header)
	list_pol=list_policies.json()
	print("The policy implemented by the Organisation")
	print(" ")
	return list_pol
 
print(List_policies())






