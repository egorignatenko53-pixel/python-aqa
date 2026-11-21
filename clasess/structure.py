import json


response = '{"status": 200, "message": "Success", "is_active": true}'

user = json.loads(response)

print(user["status"])
print(user["message"])
print(user["is_active"])


print()

test_user = {
    "id": 105,
    "username": "alex",
    "role": "manager",
    "is_active": True
}

json_data = json.dumps(test_user)

print(json_data)
print(type(json_data))

print()

user = {
    "id": 201,
    "username": "max",
    "is_active": False
}

json_data = json.dumps(user)
new_user = json.loads(json_data)

print(new_user["username"])
print(new_user["is_active"])
print(type(new_user))

print()

response = '{"status": 200, "message": "Success"'

try:
    data = json.loads(response)
    print(data)
except json.JSONDecodeError:
    print("Некорректный JSON")

print()

responses = [
    '{"status": 200, "message": "Success"}',
    '{"status": 404, "message": "Not Found"}',
    '{"status": 201, "message": "Created"'
]

def parse_response(response):
    try:
        data = json.loads(response)
        return data["status"]
    except json.JSONDecodeError:
        return "Ошибка JSON"

for status in responses:
    result = parse_response(status)
    print(result)


print()

responses = [
    '{"status": 200, "message": "Success"}',
    '{"status": 404, "message": "Not Found"}',
    '{"status": 201, "message": "Created"}'
]

def check_response(response):
    try:
        data = json.loads(response)

        if data["status"] == 200 or data["status"] == 201:
            return "Тест пройден"
        else:
            return "Тест провален"

    except json.JSONDecodeError:
        return "Ошибка JSON"
    
for stat in responses:
    result = check_response(stat)
    print(result)