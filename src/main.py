# main file to hold the logic of file parsing in python
# sample resorces to follow : https://pypi.org/project/jsonpath-ng/

from jsonpath_ng import jsonpath, parse
import json
  
# Opening JSON file
f = open('Resources/sample.json')
# returns JSON object as 
# a dictionary
data = json.load(f)
#print(data)

print('---------------------------------------------------')
# Find all the 'id'
jsonpath_expr = parse('$.._id')
for val in jsonpath_expr.find(data):
    # Here the 'val' contains multiple parameters. Our requirement is just the value parameter. Hence we are only printing : val.value
    print(val.value)

print('---------------------------------------------------')
# Find a random single id value (without any condition)
jsonpath_expr_single = parse('$.[5]._id')
for val in jsonpath_expr_single.find(data):
    print(val.value)

print('---------------------------------------------------')
# Find all the 'company' parameters
jsonpath_expr = parse('$..company')
for val in jsonpath_expr.find(data):
    # Here the 'val' contains multiple parameters. Our requirement is just the value parameter. Hence we are only printing : val.value
    print(val.value)

#### For the below section a bug is being raised
#  https://github.com/h2non/jsonpath-ng/issues/113
# print('---------------------------------------------------')
# # Find all the 'id' parameters filtered out w.r.t the selected company
# # desired_company_name = 'GADTRON'
# jsonpath_expr = parse('$[?(@.company=="GADTRON")]._id')
# for val in jsonpath_expr.find(data):
#     # Here the 'val' contains multiple parameters. Our requirement is just the value parameter. Hence we are only printing : val.value
#     print(val.value)

print('---------------------------------------------------')
# Find all the 'tags' parameters
jsonpath_expr = parse('$..tags')
for val in jsonpath_expr.find(data):
    # Here the 'val' contains multiple parameters. Our requirement is just the value parameter. Hence we are only printing : val.value
    print(val.value)















###
#sample val value after parsing the jsonpath expression

''' 
DatumInContext(value='634046f25ed766b0f629858b', path=Fields('_id'), context=DatumInContext(value={'_id': '634046f25ed766b0f629858b', 'index': 9, 'guid': '113658af-4d0a-4111-a999-3dc03ab9cf37', 'isActive': False, 'balance': '$2,768.33', 'picture': 'http://placehold.it/32x32', 'age': 23, 'eyeColor': 'blue', 'name': 'Carissa Kirkland', 'gender': 'female', 'company': 'PYRAMIA', 'email': 'carissakirkland@pyramia.com', 'phone': '+1 (801) 427-3182', 'address': '778 Arkansas Drive, Bancroft, Tennessee, 2899', 'about': 'Commodo qui minim excepteur tempor tempor in veniam labore excepteur excepteur culpa pariatur sint qui. Non consequat est quis cillum sit irure cillum non velit sint tempor commodo. Minim duis non veniam irure duis reprehenderit minim ut. Laborum nostrud incididunt ipsum ea quis veniam. Dolor laborum magna nulla anim voluptate ad id aute ipsum veniam quis est. Sint et id fugiat labore dolor ea aute pariatur exercitation magna laboris anim qui ea. Eiusmod proident sit nostrud sit officia voluptate anim non amet consectetur excepteur ad enim.\r\n', 'registered': '2014-11-08T09:20:58 -06:-30', 'latitude': -86.041677, 'longitude': -119.688441, 'tags': ['amet', 'sint', 'non', 'aliquip', 'consequat', 'amet', 'sunt'], 'friends': [{'id': 0, 'name': 'Mcmahon Miles'}, {'id': 1, 'name': 'Irene Wallace'}, {'id': 2, 'name': 'Stanley Cain'}], 'greeting': 'Hello, Carissa Kirkland! You have 5 unread messages.', 'favoriteFruit': 'strawberry 2'}, path=Index(index=9)
'''



###