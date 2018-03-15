# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

###################start of standard output ##################################
[+] Hardware information:

[+] CPU:
        - Vendor: GenuineIntel
        - Brand: Intel(R) Core(TM) i5-4590 CPU @ 3.30GHz
        - Version information: 0x306C3
        - Feature bits:
                * 0x100800
                * 0x7FFAFBFF
                * 0xBFEBFBFF
        - Processors: 4

[+] Memory:
        - RAM: 8530001920 (0x1FC6D8000) bytes

[+] Drives:
        - Drive:
                * Vendor:
                * Product ID: Samsung SSD 850 EVO 500GB
                * Product REV: EMT01B6Q
                * Serial number: S21HNSAG300129N
                * Capacity: 500107862016 bytes

[+] Read 3538 bytes of SMBIOS data.
###################end of standard output ##################################


"""

from subprocess import check_output as qx
import json
import requests

cmd = r'genid.x86.exe'
output = qx(cmd)

output = str(output).replace('\\r','').replace('\\n','').replace('\\t','').strip()
'''
level1: [+]
level2: -
level3: *
'''

#process the 1st layer ,which is just '[+]'
layer1 = output.split('[+]')[2:]
#layer1[0] is the 
'''
[
 ' CPU:- Vendor: GenuineIntel- Brand: Intel(R) Core(TM) i5-4590 CPU @ 3.30GHz- Version information: 0x306C3- Feature bits:* 0x100800* 0x7FFAFBFF* 0xBFEBFBFF- Processors: 4',
 ' Memory:- RAM: 8530001920 (0x1FC6D8000) bytes',
 ' Drives:- Drive:* Vendor: * Product ID: Samsung SSD 850 EVO 500GB* Product REV: EMT01B6Q* Serial number: S21HNSAG300129N* Capacity: 500107862016 bytes',
 " Read 3538 bytes of SMBIOS data.'"]
'''
result = {}

for layer in layer1:
    #deal with layer2 with '-'
    layer2 = layer.split('-')
    '''
    [' CPU:',
     ' Vendor: GenuineIntel',
     ' Brand: Intel(R) Core(TM) i5',
     '4590 CPU @ 3.30GHz',
     ' Version information: 0x306C3',
     ' Feature bits:* 0x4100800* 0x7FFAFBFF* 0xBFEBFBFF',
     ' Processors: 4']
    '''
    component_name = layer2[0].replace(':','').strip()
    for layer2_layer in layer2[1:]:
        temp_layer = layer2_layer.split(':')
        if len(temp_layer)==2:
            key,value = temp_layer
            value = value.strip()
            if '*' in value:
                value = [item.strip() for item in value.split('*')[1:]]
        else:
            key = temp_layer[0].replace(':','').strip()
            value = None

        key = key.strip()
        result[component_name+'_'+key] = value
        
r = requests.post("https://hardwareid.herokuapp.com/ids", data=result)
"""

os.system('bash test.bash')
with open('test.txt','r') as f:
    data = f.read()
data_json = json.loads(data)
"""
