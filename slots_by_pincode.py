import requests
import datetime
import json
import easygui

pincode=easygui.enterbox('Enter Pincode: ')

browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
t1=[]

#showing slots for next 5 days
for i in range(0,5):
	date=datetime.datetime.today() + datetime.timedelta(days=i)
	date=date.strftime("%d-%m-%Y")
	response=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(pincode,date),headers=browser_header)
	# print(response.status_code)
	json_data=json.loads(response.text)
	# print(json_data)
	print('-------------------------------------------------------------------')
	print("Date: ",date)
	print('-------------------------------------------------------------------')
	# print(json_data)
	if len(json_data['sessions'])==0:
		print("\nSlots Not Available\n")
		continue
	for slots in json_data['sessions']:
		print("\nCenter ID: "+str(slots['center_id']) +'\n' 
			+ "Name: "+str(slots['name']) +'\n' 
			+ "Address: "+str(slots['address']) +'\n' 
			+ "State Name: "+str(slots['state_name']) +'\n' 
			+ "District Name: "+str(slots['district_name']) +'\n' 
			+ "Pincode: "+str(slots['pincode']) +'\n' 
			+ "Opening time: "+str(slots['from']) +'\n' 
			+ "Closing Time: "+str(slots['to']) +'\n' 
			+ "fee type: "+str(slots['fee_type']) +'\n' 
			+ "fee: "+str(slots['fee']) +'\n'
			+ "Available Capacity: "+str(slots['available_capacity']) +'\n' 
			+ "Min Age Limit: "+str(slots['min_age_limit']) +'\n' 
			+ "Vaccine: "+str(slots['vaccine'])+ '\n')

		slot = {'Center ID:': str(slots['center_id']), 'Name': str(slots['name']), 'Address':str(slots['address']), 'State Name:':str(slots['state_name']), 'District Name:':str(slots['district_name']) , 'Pincode:':str(slots['pincode']) , 'Opening time:':str(slots['from']), 'Closing Time:':str(slots['to']),  'fee type:':str(slots['fee_type']), 'fee:':str(slots['fee']), 'Available Capacity: ':str(slots['available_capacity']), 'Min Age Limit:':str(slots['min_age_limit']), 'Vaccine:':str(slots['vaccine'])}
		t1.append(slot)

		print("\nTimings:")
		for i in slots['slots']:
			print(i,'\n')

i=0
for i in range(1, len(t1)):
        print(t1[i])
        print("\n\n")


