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
            'id': 22222,
            'point': 'lan,lon'
        }, {
            'name': 'теннисное поле',
            'id': 33333,
            'point': 'lan, lon'
        },{
            'name': 'волейбольное поле',
            'id': 444444,
            'point': 'lan, lon'
        },{
            'name': 'гандбольное поле',
            'id': 55555,
            'point': 'lan,lon'
        },{
            'name': 'хоккейное поле',
            'id': 626626,
            'point': 'lan, lon'
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