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

print(" 1. list the Network devices\n 2.create a network device\n 3. list the policies of the network\n 4.update a network device\n 5. list the policies of the organization\n 6. delete a device form the network\n")
select=input('enter your choice')


def device_names():
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/",headers=header)
	list_dev=list_devices.json()
	return list_dev

def list_Network_devices():
        
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/",headers=header)
	list_dev=list_devices.json()
	print("The list of Network Devices of the Organisation")
	print("=============================================================================================================================")
	print(" ")
	n=1
	for i in list_dev:
		print('\n')
		print("Device#",n)
		n+=1
		for j in i.items():
			dev=str(j).replace(",", ":")	
			print(dev)
	return "" 
	

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


def  List_policies():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/" +orgid +"/networkdevices/"+originId+"/policies", headers=header)
	list_pol=list_policies.json()
	print("The policy implemented by the Organisation")
	print(" ")
	return list_pol


def update_network_device(name):
	update_net=requests.patch("https://management.api.umbrella.com/v1/organizations/" +orgid+"/networkdevices/"+originId, json.dumps(body_update),headers=header)
	update_net=update_net.json()
	return update_net
		

'''def delete_network_device(del_device):
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
	print("Thanks for using Cicso Umbrella API")'''


device_names=device_names()

if select=="1":
	print(list_Network_devices())

elif select=="2":
	name=input('Enter the name to create a new network device')
	model=input('Enter the model to create a new network device')
	macAddress=input('Enter the macAddress to create a new network device')
	label=input('Enter the label to create a new network device')
	serialnumber=input('Enter the serialnumber to create a new network device')
	tag=input('Enter the tag to create a new network device')
	print(create_network_devices(name,model,macAddress,label,serialnumber,tag))


elif select=="3":
	device_choose=input("Enter the name of the network device to which you want to view the policy for:")
	for i in device_names:
		if i["name"]==device_choose:
			dict1=i
			originId=str(dict1["originId"])
			print(List_policies())
			break
	else:
		print(" {} device does not exist in this organisation".format(device_choose)) 

elif select=="4":

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


elif select=="6":

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
