name = "Egor"
age = 21 
role = "Manual QA"

print(name)
print(age)
print(role)




bug_status = "Open"
print(bug_status)
bug_status = "In Progress"
print(bug_status)
bug_status = "Closed"
print(bug_status)


test_name = "Login Test"
response_code = 200 
execution_time = 1.5
is_passed = True

print(type(test_name))
print(type(response_code))
print(type(execution_time))
print(type(is_passed))



total_tests = 50 
passed_tests = 42
failed_tests = total_tests - passed_tests

print(failed_tests)




total_tests = 80
passed_tests = 68
failed_tests = total_tests - passed_tests
pass_rate = passed_tests / total_tests * 100 

print(failed_tests)
print(pass_rate)



status_code = 401
if status_code == 200:
    print("Тест пройден")
else:
    print("Тест провален")



status_code = 500
if status_code == 200:
    print("Успешно")
elif status_code == 400:
    print("Ошибка клиента")
elif status_code == 500:
    print("Ошибка сервера")
else:
    print("Неизвестный статус")



status_code = 200
response_time = 2.5
if status_code == 200 and response_time < 2:
    print("Тест пройден")
else:
    print("Тест провален")



status_code = 201
if status_code == 200 or status_code ==201:
    print("Регистрация успешна")
else:
    print("Ошибка регистрации")




status_code = 201
response_time = 1.8
token_received = True
if (status_code == 200 or status_code == 201 ) and response_time < 2 and token_received == True:
    print("Авторизация успешна")
else:
    print("Ошибка авторизации")



for i in range(1,8):
    print(i)





status_codes = [200, 201, 400, 200, 500, 201]
for status in status_codes:
    if status == 200 or status == 201:
        print("Тест пройден")
    else:
        print("Тест провален")






status_codes = [200, 201, 400, 500, 200, 201, 404, 200]
passed_tests = 0 
failed_tests = 0 
for status in status_codes:
    if status == 200 or status == 201:
        passed_tests += 1
    else:
        failed_tests += 1


print(passed_tests)
print(failed_tests)

print()


status_codes = [200, 201, 400, 200, 500, 201, 200, 404, 201, 200]
passed_tests = 0 
failed_tests = 0 
total_tests = len(status_codes)
for status in status_codes:
    if status == 200 or status == 201:
        passed_tests += 1 
    else:
        failed_tests += 1

pass_rate = passed_tests / total_tests * 100 
print(total_tests)
print(passed_tests)
print(failed_tests)
print(pass_rate)


print()

status_codes = [200, 404, 201, 500, 403, 200]
print(status_codes[0])
print(status_codes[3])
print(status_codes[-1])

print()


status_codes = [200, 404, 500]
status_codes[1] = 201 
status_codes.append(403)
status_codes.remove(500)

print(status_codes)

print()


allowed_statuses = [200, 201, 204]
status_codes = [200, 400, 201, 500, 204, 404]
for status in status_codes:
    if status in allowed_statuses:
       print("Тест пройден")
    else:
       print("Тест провален")



print()

blocked_users = ["alex", "max", "ivan"]
users = ["egor", "alex", "anna", "max", "petr"]
for user in users:
    if user not in blocked_users:
        print("Доступ разрешён")
    else:
        print("Доступ запрещён")

print()

user = {
"id": 101,
"username": "egor",
"age" : 21,
"is_active" : True
}

print(user["username"])
print(user["age"])
print(user["is_active"])



print()

user = {
    "id": 101,
    "username": "egor",
    "age": 21,
    "is_active": False
}

user["is_active"] = True
user["age"] = 22
user["role"] = "admin"
print(user)



print()

user = {
    "id": 105,
    "username": "alex",
    "role": "manager",
    "is_active": True,
    "is_blocked": False
}
if (user["role"] == "admin" or user["role"] == "manager") and user["is_active"] == True and user["is_blocked"] == False:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")



print()

users = [
    {"username": "egor", "is_active": True},
    {"username": "alex", "is_active": False},
    {"username": "anna", "is_active": True},
    {"username": "max", "is_active": False}
]
for user in users:
    if user["is_active"] == True:
        print("Пользователь активен")
    else:
        print("Пользователь неактивен")



print

users = [
    {"username": "egor", "is_active": True},
    {"username": "alex", "is_active": False},
    {"username": "anna", "is_active": True},
    {"username": "max", "is_active": False},
    {"username": "ivan", "is_active": True},
    {"username": "petr", "is_active": True}
]
active_count = 0 
inactive_count = 0 
for user in users:
    if user["is_active"]:
        active_count +=1
    else:
        inactive_count += 1

print(active_count)
print(inactive_count)



print()

user = {
    "id": 101,
    "username": "egor",
    "email": "egor@example.com"
}

print(user.get("username"))
print(user.get("email"))
print(user.get("phone","Телефон не указан"))



print()

def check_status(status_code):
    if status_code == 200 or status_code == 201:
        print("Тест пройден")
    else:
        print("Тест провален")

check_status(200)
check_status(404)
check_status(201)

print()
def is_successful(status_code):
    if status_code == 200 or status_code == 201:
        return True
    else:
        return False

result1 = is_successful(200)
result2 = is_successful(404)
result3 = is_successful(201)

print(result1)
print(result2)
print(result3)


print()
def double(number):
    return number * 2
result = double(5)
print(result)


print()
def check_api(status_code, response_time):
    if (status_code == 200 or status_code == 201) and response_time < 2:
        return True
    else:
        return False
result1 = check_api(200, 1.5)
result2 = check_api(201, 2.5)
result3 = check_api(400, 1.0)

print(result1)
print(result2)
print(result3)


print()

status_codes = [200, 404, 201, 500, 200]

def is_successful(status_code):
    if status_code == 200 or status_code == 201:
        return True
    else:
        return False

results = []

for status in status_codes:
    result = is_successful(status)
    results.append(result)

print(results)

print()

status_codes = [200, 404, 201, 500, 200]
def is_successful(status_code):
    if status_code == 200 or status_code == 201:
        return True
    else:
        return False
results = []
passed = 0 

for status in status_codes:
    result = is_successful(status)
    results.append(result)
    if result == True:
        passed +=1
print(results)
print(passed)

print()
status_codes = [200, 404, 201, 500, 200, 403]
def is_successful(status_code):
    if status_code == 200 or status_code == 201:
        return True
    else:
        return False
    
passed = 0 
failed = 0 

for status in status_codes:
    result = is_successful(status)
    if result == True:
        passed +=1
    else:
        failed +=1
print("Passed:", passed)
print("Failed:", failed)

print()
status_codes = [200, 404, 201, 500, 200, 403]
def get_test_results(status_codes):
    passed = 0 
    failed = 0 
    for status in status_codes:
        result = get_test_results(status)
        if status == 200 or status == 201:
            passed += 1 
        else:
            failed += 1
    return passed , failed
    
        