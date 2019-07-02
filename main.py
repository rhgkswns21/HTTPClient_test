import requests

url = 'http://111.93.235.82:3105'

#HTTP API to add new entity details     #Add entity details
# r = requests.post(url + '/Identity/entities',
#                   None,
#                   {"entityId": "353041080777777","entityType": "GATEWAY",
#                    "entityCategory": "SHM","entityModel": "API_TEST",
#                    "friendlyName": "API_TEST","lastModifiedDate": "2019-05-27",
#                    "version": "1.0","blocked": "false","panId": "0x7777"})

#HTTP API to download entity private key file   #Download entity private key
# r = requests.get(url + '/Identity/entities/353041080777777/keyfile')

#HTTP API to download (GET) entity Certificate file #Download entity certificate
# r = requests.get(url + '/Identity/entities/353041080777777/certfile')

#HTTP API to get the list of entities   #Get the list of entities
# r = requests.get(url + '/Identity/entities')

# HTTP API to update entity details #Update entity details
# r = requests.put(url + '/Identity/entities/353041080777777',
#                  None,
#                  {"entityId": "353041080777777", "entityType": "GATEWAY",
#                     "entityCategory": "SHM", "entityModel": "TEST_API",
#                     "friendlyName": "API_TEST", "lastModifiedDate": "2019-05-27",
#                     "version": "1.0", "blocked": "false", "panId": "0x7777"})

#HTTP API to delete entity details  #Delete entity details
# r = requests.delete(url + '/Identity/entities/353041080777777')

# HTTP API to block entity  #Block entity details
# r = requests.put(url + '/Identity/entities/353041080777777/block')

# HTTP API to unblock entity    #Unblock entity details
# r = requests.put(url + '/Identity/entities/353041080777777/unblock')

# HTTP API to fetch (GET) entity details    #Get the entity details
# r = requests.get(url + '/Identity/entities/353041080777777')

# HTTP API to publish/update the device book (list of nodes connected) of a gateway     #Update the Devicebook
# r = requests.post(url + '/Identity/entities/353041080777777/devicebook',
#                   None,
#                   [{
#                     "entityId": "353041080777777",
#                     "devEUI": "7981"
#                   },
#                   {
#                     "entityId": "353041080777777",
#                     "devEUI": "697"
#                   }])

# HTTP API to fetch/GET the device book of a gateway    #Get the Devicebook
# r = requests.get(url + '/Identity/entities/353041080777777/devicebook')

# HTTP API to add new Sensor Node   #Add new sensor node
# r = requests.post(url + '/Identity/nodes',
#                  None,
#                  {
#                      "devEUI": "d1213",
#                      "deviceCategory": "SHM",
#                      "appEUI": "a112",
#                      "appKey": "a122",
#                      "deviceAddress": "18933",
#                      "nwkSKey": "nw12343",
#                      "appSKey": "qwerty",
#                      "devNonce": "43211",
#                      "appNonce": "12341"
#                  })

# HTTP API to update Sensor Node details    #Update new sensor node
# r = requests.put(url + '/Identity/nodes/d1213',
#                  None,
#                  {
#                      "devEUI": "d1213",
#                      "deviceCategory": "SHM",
#                      "appEUI": "d112",
#                      "appKey": "d122",
#                      "deviceAddress": "18933",
#                      "nwkSKey": "nw12343",
#                      "appSKey": "qwerty",
#                      "devNonce": "43211",
#                      "appNonce": "12341"
#                  })

# HTTP API to remove a Sensor Node  #Delete new sensor node
# r = requests.delete(url + '/Identity/nodes/d1213')

# HTTP API to GET the details of a Sensor Node  #Get new sensor node
# r = requests.get(url + '/Identity/nodes/d1213')

# HTTP API to GET the list of Sensor Nodes  #Get list of sensor nodes
# r = requests.get(url + '/Identity/nodes')

# HTTP API to GET security info of a gateway    #Get security info of gateway
# r = requests.get(url + '/Identity/entities/353041080777777/securityinfo')

# files = open("C:/Users/ko/Desktop/test.csv")
# f = open('c:/Users/ko/Desktop/test.csv', 'rb')
# print(f.readline())
# f.close()
# HTTP API to add bulk entities from CSV file                                                       / Please Check
# r = requests.post('http://18.232.187.34:3105/Identity/entities/addBulk', files=f)
# files.close()

# HTTP API to add bulk end nodes from CSV file                                                      / Please Check
# r = requests.post('http://18.232.187.34:3105/Identity/nodes/addBulk')

# HTTP API to renew an entity certificate       #Renew entity certificate
# r = requests.post(url + '/Identity/entities/353041080777777/renew')

# HTTP API to add/update the GPS location of a Gateway entity   #Update GPS location of gateway entity
# r = requests.post(url + '/Identity/entities/353041080777777/location', None,
#                   {
#                     "entityId": "353041080777777",
#                     "latitude": 101.2345,
#                     "longitude": 123.523167
#                   })

# HTTP API to GET the GPS location of a Gateway entity  #Get GPS location of gateway entity
# r = requests.get(url + '/Identity/entities/353041080777777/location')

# HTTP API to add/update the GPS location of an end node    #Update GPS location of gateway node
# r = requests.post(url + '/Identity/nodes/697/location', None,
#                  {
#                     "devEUI": "697",
#                     "latitude": 123.456789,
#                     "longitude": 12.123456
#                  })

# HTTP API to GET the GPS location of an End Node   #Get GPS location of gateway node
# r = requests.get(url + '/Identity/nodes/697/location')

# HTTP API to download (GET) ROOT CA Certificate file   #Get ROOT CA certificate
# r = requests.get(url + '/Identity/entities/ca/certfile')

# HTTP API to get the list of entities by category  #Get list of entities by category
# r = requests.get(url + '/Identity/entities/category/SHM')

# HTTP API to add new Network details   #Add network details
# r = requests.post(url + '/Identity/networks', None,
#                   {
#                       "panId": "0x1234",
#                       "bandwidth": 2,
#                       "spreadFactor": 7,
#                       "ack": "true",
#                       "retryCount": 3,
#                       "power": 13,
#                       "channel": 2
#                   })

# # HTTP API to get the list of networks    #Get list of networks details
# r = requests.get(url + '/Identity/networks')

# HTTP API to get the details of a network  #Get network details
# r = requests.get(url + '/Identity/networks/0x1234')

# HTTP API to DELETE the details of a network   #Delete network details
# r = requests.delete(url + '/Identity/networks/0x1234')

# HTTP API to Update Network details    #Update network
# r = requests.put(url + '/Identity/networks/0x1234', None,
#                  {
#                     "panId": "0x1234",
#                     "bandwidth": 2,
#                     "spreadFactor": 7,
#                     "ack": "true",
#                     "retryCount": 3,
#                     "power": 10,
#                     "channel": 2
#                  })

# HTTP API to add/update Configuration for an entity    #Add/Update configuration for entity
# r = requests.post(url + '/Identity/entities/353041080777777/config',  None,
#                   {
#                     "entityId": "353041080777777",
#                     "role": 1,
#                     "ownId": "0x0000",
#                     "netAddr": 0,
#                     "simPin": "1234",
#                     "apn": "iijmobile.biz",
#                     "simUser": "mobile.iij",
#                     "simPassword": "iij",
#                     "preload": 5,
#                     "duration": 30,
#                     "useSSL": "false",
#                     "lowPowerMode": "false",
#                     "syncTime": 5
#                   })

# HTTP API to GET configuration for an entity   #Get configuration for entity
# r = requests.get(url + '/Identity/entities/353041080777777/config')

# HTTP API to GET configuration for an entity   #Get configuration for entity(device side)
# r = requests.get(url + '/Identity/entities/353041080777777/configuration')

# HTTP API to get the list of entities for given PAN Id #Get the list of entities for given PAN Id
# r = requests.get(url + '/Identity/entities/panid/0x7777')

# HTTP API to get the list of master entities for given PAN Ids #Get the list of master entities for given PAN Id
# r = requests.post(url + '/Identity/entities/master', None,
#                  {
#                      "panIds":["0x1234", "0x0006", "0x7777"]
#                  })



print('r : ', r)
print('r.text : ', r.text)
# print('r.json : ', r.json())