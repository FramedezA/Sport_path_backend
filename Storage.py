import json
data = {
    'response': {
        'class': 'поля',
        'items': [{
            'name': 'футбольно поле',
            'id': 111111,
            'point': 'lan,lon'
        }, {
            'name': 'баскетбольное поле',
            'id': 222222,
            'point': 'lan,lon'
        }, {
            'name': 'Волейбольное поле',
            'id': 333333,
            'point': 'lan,lon'
        }, {


        }]
    }
}
json_data = json.dumps(data)
with open('data.json', 'w') as file:
    file.write(json_data)
with open('data.json', 'r') as file:
    json_data = file.read()
    data = json.loads(json_data)
    print(data)

class storage