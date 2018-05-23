import requests
import json
import sys
apikey='Basic ODQxZTJhMjA2Yjc1NDczY2ExMTM0ZTA5ZjMxYmE3Nzc6YmZlMGQ1ZjA4ZjY3NDdlZDg0NzdhY2U0ZWM3NDQ0YjQ='
header={'Authorization' :apikey,'Content-Type':'application/json'}
oid=requests.get("https://management.api.umbrella.com/v1/organizations/",headers=header)
oid=oid.json()
orgid=str(oid[0]["organizationId"])
print("The organisation Id is {}" .format(orgid))
print(" ")


def list_Network_devices():
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/",headers=header)
	list_dev=list_devices.json()
	print("The list of Network Devices of the Organisation")
	print("=============================================================================================================================")
	print(" ")
	n=1
	for i in list_dev:
		print("Device#",n)
		n+=1
		for j in i.items():
			dev=str(j).replace(",", ":")	
			print(dev)
		print("\n")
	return list_dev
device_names=list_Network_devices()

	
'''name,model,macAddress,label,serialnumber,tag=input('Enter The name, model,macAdd, label serialnum and tag to create a new network device').split()

def create_network_devices(name,model,macAddress,label,serialnumber,tag):


	body_net={
		"name": name,
		"model":model,
		"macAddress":macAddress,
		"label":label,
		"serialNumber":serialnumber,
		"tag":tag
	}
	body_post=requests.post("https://management.api.umbrella.com/v1/organizations/"+orgid+"/networkdevices",json.dumps(body_net), headers=header)
	body_post=body_post.json()
	return body_post 

print(create_network_devices(name,model,macAddress,label,serialnumber,tag))'''

def  List_policies():
        list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/" +orgid +"/networkdevices/"+originId+"/policies", headers=header)
        list_pol=list_policies.json()
        print("The policy implemented by the Organisation")
        print(" ")
        return list_pol


device_choose=input("Enter the name of the network device to which you want to view the policy for:")
for i in device_names:
	if i["name"]==device_choose:
		dict1=i
		originId=str(dict1["originId"])
		print(List_policies())
		break
	
else:
	print(" {} device does not exist in this organisation".format(device_choose)) 

def update_network_device(name):
	update_net=requests.patch("https://management.api.umbrella.com/v1/organizations/" +orgid+"/networkdevices/"+originId, json.dumps(body_update),headers=header)
	update_net=update_net.json()
	return update_net
		
 
device_update=input("Enter the name of the network device you want to update:")

for i in device_names:
	if i["name"]==device_update:
		dictn=i 
		originId=str(dictn["originId"])
		name=input('Enter the updated Device name')
		body_update={"name":name}
		print(update_network_device(name))
		break
else:
	print(" {} device does not exist in this organisation".format(device_update))


def delete_network_device(del_device):
	del_network=requests.delete("https://management.api.umbrella.com/v1/organizations/"+orgid+"/networkdevices/" +originId,headers=header)
	return del_network


prompt=input('Do you wish to delete a network device from this organisation ? Yes-y and No-n')

if prompt=='y': 
	del_device=input("Enter the name of the network device you want to delete:")
	for i in device_names:
		if i["name"]==del_device:
			dictm=i
			originId=str(dictm["originId"])
			print(delete_network_device(del_device))
			print("Thanks for using Cicso Umbrella API")
			break
	else:
		print(" {} device does not exist in this organisation".format(prompt))
		sys.exit()
else:
	print("Thanks for using Cicso Umbrella API")



	
