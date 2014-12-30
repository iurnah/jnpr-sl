import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

ask4iptype = 'Enter IP_type: >\nIP_ADDR = 1,\nIP_RANGE = 2,\nIP_SUBNET = 3,\nIP_PORT = 4,\nIP_LIST = 5\n> '
usecase = Object()
IP_type = raw_input(ask4iptype)

if IP_type == '1':
    IP_value = raw_input('Enter IP_values:> ')
    usecase.IP_ADDR = IP_value
    usecase.properties = Object()
    TL = raw_input('Enter threat level:> ')
    usecase.properties.tl = TL
    family = raw_input('Enter threat family:> ')
    usecase.properties.family = family
elif IP_type == '2':
    IP_value = raw_input('Enter IP_values:> ')
    delta = raw_input('Enter delta:> ')
    usecase.IP_RANGE = IP_value + ',' + delta
    usecase.properties = Object()
    TL = raw_input('Enter threat level:> ')
    usecase.properties.tl = TL
    family = raw_input('Enter threat family:> ')
    usecase.properties.family = family
elif IP_type == '3':
    IP_value = raw_input('Enter IP_values:> ')
    subnet = raw_input('Enter subnet:> ')
    usecase.IP_RANGE = IP_value + '/' + subnet
    usecase.properties = Object()
    TL = raw_input('Enter threat level:> ')
    usecase.properties.tl = TL
    family = raw_input('Enter threat family:> ')
    usecase.properties.family = family
elif IP_type == '4':
    IP_value = raw_input('Enter IP_values:> ')
    subnet = raw_input('Enter port:> ')
    usecase.IP_RANGE = IP_value + ':' + subnet
    usecase.properties = Object()
    TL = raw_input('Enter threat level:> ')
    usecase.properties.tl = TL
    family = raw_input('Enter threat family:> ')
    usecase.properties.family = family
elif IP_type == '5':
    IP_value = raw_input('Enter IP_values:> ')
    subnet = raw_input('Enter port:> ')
    usecase.IP_RANGE = IP_value + ':' + subnet
    usecase.properties = Object()
    TL = raw_input('Enter threat level:> ')
    usecase.properties.tl = TL
    family = raw_input('Enter threat family:> ')
    usecase.properties.family = family
else:
    print 'Nothing Go Through!!!'
    
print usecase.toJSON()


