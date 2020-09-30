
import requests
url = 'http://127.0.0.1:8833/api/emp/'


# Testing rest api url  for getting all records from provider app
response = requests.get('http://127.0.0.1:8833/api/emp/')

# Testing Django  url for getting all records form provider app
# response = requests.get('http://127.0.0.1:8833/employee/')

# getting single record
# id = input('Enter any id :')
# response = requests.get('http://127.0.0.1:8833/api/emp/' + id + '/')




# creating new record
payload = {
    'eno': 30,
    'ename' : 'Srinivas',
    'esal' : 35000,
    'eaddr': 'KPHB'
}
# response = requests.post('http://127.0.0.1:8833/api/emp/', data=payload)


# updating single record
payload = {
    'eno': 30,
    'ename' : 'Srini',
    'esal' : 45000,
    'eaddr': 'Maitrivanam'
}

# id = input('Enter any id :')
# response = requests.put('http://127.0.0.1:8833/api/emp/' + id + '/', data=payload)


# deleting single record
# id = input('Enter any id :')
# response = requests.delete('http://127.0.0.1:8833/api/emp/' + id + '/')




# handling the responses to display required messages
if response.status_code==200:
    try:
        print(response.json())
        print('Display all records successfully.')
    except:
        print("Status code is : ", response.status_code)
        print('You are not getting JSON data from provider')

elif response.status_code==201:
    print("Status code is : ", response.status_code)
    print(response.json())
    print(' Record created successfully.')

elif response.status_code==204:
    print("Status code is : ", response.status_code)
    print('Record  deleted successfully')

elif response.status_code==400:
    print("Status code is : ", response.status_code)
    print('Record not creted successfully. Please send valid type data.')

elif response.status_code==404:
    print("Status code is : ", response.status_code)
    print('Record not found')

elif response.status_code==403:
    print('Method not hitting , csrf token missing')

elif response.status_code==500:
    print("Status code is : ", response.status_code)
    print('Server side problems occurs')

else:
    print("Status code is : ", response.status_code)
    print('Some thing wrong.')



