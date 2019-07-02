import requests

url = 'http://111.93.235.82:3105'

#HTTP API to add new entity details                                                                         / OK
r = requests.post(url + '/Identity/entities',
                  None,
                  {"entityId": "353041080777777","entityType": "GATEWAY",
                   "entityCategory": "SHM","entityModel": "API_TEST",
                   "friendlyName": "API_TEST","lastModifiedDate": "2019-05-27",
                   "version": "1.0","blocked": "false","panId": "0x7777"})

#HTTP API to download entity private key file                                                               / OK
# r = requests.get('http://111.93.235.82:3105/Identity/entities/353041080777777/keyfile')

#HTTP API to download (GET) entity Certificate file                                                         / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/certfile')

#HTTP API to get the list of entities                                                                       / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities')

# HTTP API to update entity details                                                                         / OK
# r = requests.put('http://18.232.187.34:3105/Identity/entities/353041080777777',
#                  None,
#                  {"entityId": "353041080777777", "entityType": "GATEWAY",
#                     "entityCategory": "SHM", "entityModel": "TEST_API",
#                     "friendlyName": "API_TEST", "lastModifiedDate": "2019-05-27",
#                     "version": "1.0", "blocked": "false", "panId": "0x7777"})

#HTTP API to delete entity details                                                                          / OK
# r = requests.delete('http://18.232.187.34:3105/Identity/entities/353041080777777')

# HTTP API to block entity                                                                                  / OK
# r = requests.put('http://18.232.187.34:3105/Identity/entities/353041080777777/block')

# HTTP API to unblock entity                                                                                / OK
# r = requests.put('http://18.232.187.34:3105/Identity/entities/353041080777777/unblock')

# HTTP API to fetch (GET) entity details                                                                    / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777')

# HTTP API to publish/update the device book (list of nodes connected) of a gateway                         / OK
# r = requests.post('http://18.232.187.34:3105/Identity/entities/353041080777777/devicebook',
#                   None,
#                   [{
#                     "entityId": "353041080777777",
#                     "devEUI": "d1213"
#                   },
#                   {
#                     "entityId": "353041080777777",
#                     "devEUI": "1"
#                   }])

# HTTP API to fetch/GET the device book of a gateway                                                        / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/devicebook')

# HTTP API to add new Sensor Node                                                                           / OK
# r = requests.post('http://18.232.187.34:3105/Identity/nodes',
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

# HTTP API to update Sensor Node details                                                                    / OK
# r = requests.put('http://18.232.187.34:3105/Identity/nodes/d1213',
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

# HTTP API to remove a Sensor Node                                                                          / OK
# # r = requests.delete('http://18.232.187.34:3105/Identity/nodes/d1213')

# HTTP API to GET the details of a Sensor Node                                                              / OK
# r = requests.get('http://18.232.187.34:3105/Identity/nodes/d1213')

# HTTP API to GET the list of Sensor Nodes                                                                  / OK
# r = requests.get('http://18.232.187.34:3105/Identity/nodes')

# HTTP API to GET security info of a gateway                                                                / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/securityinfo')
# \Users\ko\Desktop

# files = open("C:/Users/ko/Desktop/test.csv")
# f = open('c:/Users/ko/Desktop/test.csv', 'rb')
# print(f.readline())
# f.close()
# HTTP API to add bulk entities from CSV file                                                       / Please Check
# r = requests.post('http://18.232.187.34:3105/Identity/entities/addBulk', files=f)
# files.close()

# HTTP API to add bulk end nodes from CSV file                                                      / Please Check
# r = requests.post('http://18.232.187.34:3105/Identity/nodes/addBulk')

# HTTP API to renew an entity certificate                                                                   / OK
# r = requests.post('http://18.232.187.34:3105/Identity/entities/353041080777777/renew')

# HTTP API to add/update the GPS location of a Gateway entity                                               / OK
# r = requests.post('http://18.232.187.34:3105/Identity/entities/353041080777777/location', None,
#                   {
#                     "entityId": "353041080777777",
#                     "latitude": 101.2345,
#                     "longitude": 123.523167
#                   })

# HTTP API to GET the GPS location of a Gateway entity                                                      / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/location')

# HTTP API to add/update the GPS location of an end node                                                    / OK
# r = requests.post('http://18.232.187.34:3105/Identity/nodes/1/location', None,
#                  {
#                     "devEUI": "1",
#                     "latitude": 123.456789,
#                     "longitude": 12.123456
#                  })

# HTTP API to GET the GPS location of an End Node                                                           / OK
# r = requests.get('http://18.232.187.34:3105/Identity/nodes/1/location')

# HTTP API to download (GET) ROOT CA Certificate file                                                       / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/ca/certfile')

# HTTP API to get the list of entities by category                                                          / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/category/SHM')

# HTTP API to add new Network details                                                                       / OK
# r = requests.post('http://18.232.187.34:3105/Identity/networks', None,
#                   {
#                       "panId": "0x1234",
#                       "bandwidth": 2,
#                       "spreadFactor": 7,
#                       "ack": "true",
#                       "retryCount": 3,
#                       "power": 13,
#                       "channel": 2
#                   })

# # HTTP API to get the list of networks                                                                    / OK
# r = requests.get('http://18.232.187.34:3105/Identity/networks')

# HTTP API to get the details of a network                                                                  / OK
# r = requests.get('http://18.232.187.34:3105/Identity/networks/0x0006')

# HTTP API to DELETE the details of a network                                                               / OK
# r = requests.delete('http://18.232.187.34:3105/Identity/networks/0x1234')

# HTTP API to Update Network details                                                                        / OK
# r = requests.put('http://18.232.187.34:3105/Identity/networks/0x1234', None,
#                  {
#                     "panId": "0x1234",
#                     "bandwidth": 2,
#                     "spreadFactor": 7,
#                     "ack": "true",
#                     "retryCount": 3,
#                     "power": 10,
#                     "channel": 2
#                  })

# HTTP API to add/update Configuration for an entity                                                        / OK
# r = requests.post('http://18.232.187.34:3105/Identity/entities/353041080777777/config',  None,
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

# HTTP API to GET configuration for an entity                                                               / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/config')

# HTTP API to GET configuration for an entity                                                               / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/353041080777777/configuration')


# HTTP API to get the list of entities for given PAN Id                                                     / OK
# r = requests.get('http://18.232.187.34:3105/Identity/entities/panid/0x0006')

# HTTP API to get the list of master entities for given PAN Ids                                             / OK
# r = requests.post('http://18.232.187.34:3105/Identity/entities/master', None,
#                  {
#                      "panIds":["0x1234", "0x0006", "0x7777"]
#                  })















print('r : ', r)
print('r.text : ', r.text)
# print('r.json : ', r.json())