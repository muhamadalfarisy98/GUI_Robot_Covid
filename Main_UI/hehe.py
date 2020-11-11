import json

# {"kirim": [{"No_laci": "4","Tujuan":"LSKK"    } ] }

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })


with open('/home/faris/Desktop/pyQt/Main_UI/data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('/home/faris/Desktop/pyQt/Main_UI/data.json', 'r') as outfile:
    data=json.load(outfile)

for p in data['people']:
    print('Name: ' + p['name'])
    print('Website: ' + p['website'])
    print('From: ' + p['from'])
    print('')
  