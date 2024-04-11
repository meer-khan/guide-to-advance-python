import requests

data = {
    'value1': 'abc',
    'value2': 123
}

response = requests.post('http://localhost:5000/process-json-data', json=data)









# * receiveParameters Route
# There are two ways you can pass parameters, 
# 1- the first is to directly add it to the URL and 
# 2- the second is to add it in a JSON object.


url = 'http://localhost:5000'

response = requests.get(url+'/receiveParameters?name=Rahul&age=22')
print(response.json())


response = requests.get(url+'/receiveParameters',
params = {
  'name': 'Rahul',
  'age': 22
  }
)
print(response.json())

'''
OUTPUT
{'data': {'age': '22', 'name': 'Rahul'}}
{'data': {'age': '22', 'name': 'Rahul'}}
'''





# * receiveFormData Route
data = {
  'name': 'Shahmeer',
  'age': 24
}
print("Request to /receiveFormData")
formResponse = requests.post(
  url+'/receiveFormData',
  data=data,
  headers= {
    'Content-Type': 'application/x-www-form-urlencoded'
  })
print(formResponse.json())








# * receiveJson Route

import json

print("Request to /receiveJson")
jsonData={
  'name': 'Shahmeer Khan',
  'age': 24
}
jsonResponse = requests.post(
  url+'/receiveJson',
  json=json.dumps(jsonData)
)
print(jsonResponse.json())






# * receiveFile Route
# Depending on if you open it using mode r or rb , the code you wrote to create the endpoint will change.
print("Request to /receiveFile ")
with open('sampleTextFile.txt','r') as f:
  fileResponse = requests.post(
    url+'/receiveFile',
    files={
      'textFile': f 
    }
  )
print(fileResponse.json())