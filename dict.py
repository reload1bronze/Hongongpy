dictionary = {
    'name': '7D 건조 망고',
    'type': '당절임',
    'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
    'origin': '필리핀'
}

print('name:', dictionary['name'])
print('type: ' + dictionary['type'])

dictionary['name'] = '호랑이'

del dictionary['origin']

print(dictionary)

value = dictionary.get('neme')
print(value)

for key in dictionary:
    print(dictionary[key])
