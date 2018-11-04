import json

with open('metadata.json', 'r') as f:
    distros_dict = json.load(f)
kiosk = []
allStations = []
dict = {}
#print(distros_dict['features'])
for i in (distros_dict['features']):
    #print(i)
    temp = []
    #temp.append(i['geometry']['coordinates'])
    #allStations.append(i['properties']['name'])
    #kiosk.append(i['properties']['kioskId'])
    dict[i['properties']['kioskId']] = i['properties']['name']
    #temp.append(i['properties']['bikesAvailable'])
    #allStations.append(temp)
print(dict)
# print("{", end="")
# for x in range(0, len(allStations)):
#     print(str(x) + ": '" + allStations[x].replace("'", "") + "', ", end="")
# print("}", end="")


# [COORDINATES, NAME, BIKES AVAILABLE]

# file = 'checkExcel.txt'
#
# f = open(file, 'r')
# a = []
# for line in f:
#     a.append(int(line))
#
# a = list(set(a))
# for aa in kiosk:
#     if aa not in a:
#         print(aa)
#
# for aa in a:
#     if aa not in kiosk:
#         print("            " + str(aa))