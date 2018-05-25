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

print("                                          SECURE AUTHENTICATION & IDENTITY MANAGEMENT                                                        ")
print("\n")
print("````````````=============``````````===========`````````==========`````````===========``````````==========``````````==========```````=========")
print(" 1. list the Network devices\n 2. create a network device\n 3. list the policies of the network\n 4. update a network device\n 5. list the policies of the organization\n 6. Assign a polcy to an identity\n 7. delete a device form the network\n 8. Delete an identity from a Policy\n")
select=input('Enter your corresponding action:')


def devices_list():
	list_devices=requests.get("https://management.api.umbrella.com/v1/organizations/" + orgid + "/networkdevices/",headers=header)
	list_dev=list_devices.json()
	return list_dev

def policies_list():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/"+orgid+"/policies?page=1&limit=100",headers=header)
	list_pol=list_policies.json()
	return list_pol


def identity_policies():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/" +orgid +"/networkdevices/"+originId+"/policies", headers=header)
	list_pol=list_policies.json()
	return list_pol


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


def List_policies():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/" +orgid +"/networkdevices/"+originId+"/policies", headers=header)
	list_pol=list_policies.json()
	print("The policy implemented for the identity")
	print(" ")
	return list_pol


def update_network_device(name):
	update_net=requests.patch("https://management.api.umbrella.com/v1/organizations/" +orgid+"/networkdevices/"+originId, json.dumps(body_update),headers=header)
	update_net=update_net.json()
	return update_net


def list_org_policies():
	list_policies=requests.get("https://management.api.umbrella.com/v1/organizations/"+orgid+"/policies?page=1&limit=100",headers=header)
	list_pol=list_policies.json()
	print("The policy implemented by the Organisation")
	print(" ")
	return list_pol

def assign_policy():
	assign_policy=requests.put("https://management.api.umbrella.com/v1/organizations/"+orgid+"/policies/"+PolicyId+"/identities/"+originId, headers=header)
	return assign_policy


def delete_network_device():
	del_network=requests.delete("https://management.api.umbrella.com/v1/organizations/"+orgid+"/networkdevices/" +originId,headers=header)
	return del_network


def delete_identity_policy():
	del_policy=requests.delete("https://management.api.umbrella.com/v1/organizations/"+orgid+"/policies/"+PolicyId+"/identities/"+originId,headers=header)
	return del_policy 


### OBJECT CREATION ###

device_names=devices_list()
policies_list=policies_list()


### USER INTERFACE CREATION ###

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

elif select=="5":
	print(list_org_policies())

elif select=="6":
	device_assign=input("Enter the Device Name:")
	for i in device_names:
		if i["name"]==device_assign:
			dictz=i
			originId=str(dictz["originId"])
			break
	else:
		print(" {} device does not exist in this organisation".format(device_assign))


	policy_name=input("Enter the policy name:")
	for i in policies_list:
		if i["name"]==policy_name:
			dicto=i
			PolicyId=str(dicto["policyId"])
			print(assign_policy())
			break
	else:
		print(" {} Policy does not exist in this organisation".format(policy_name))


elif select=="7":

	prompt=input('Are you sure you want to delete a network device from this organisation ? Yes-y and No-n')

	if prompt=='y': 
        	del_device=input("Enter the name of the network device you want to delete:")
        	for i in device_names:
                	if i["name"]==del_device:
                        	dictm=i
                        	originId=str(dictm["originId"])
                        	print(delete_network_device())
                        	break
        	else:
                	print(" {} device does not exist in this organisation".format(del_device))
                	sys.exit()
	else:
        	print("Done")



elif select=="8":

	prompt=input('Are you sure you want to delete a network device from a particular Policy? Yes-y and No-n')
	if prompt=='y':
		del_dev=input("Enter the name of the network device:")
		for i in device_names:
			if i["name"]==del_dev:
				dictp=i
				originId=str(dictp["originId"])
				break
		else:
			print(" {} device does not exist in this organisation".format(del_dev))
			sys.exit()
		identity_policies=identity_policies()
		policy_name=input("Enter the policy name:")
		for i in policies_list:
			if i["name"]==policy_name:
				dictl=i
				PolicyId=str(dictl["policyId"])
				print(delete_identity_policy())
				break

		'''for i in identity_policies:
			if i["name"]==policy_name:
				print(delete_identity_policy())
				break
		else:
			print("{} is not applied for the {} identity".format(policy_name,del_dev))'''
					
	else:
                print("Done")






