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
        if status == 200 or status == 201:
            passed += 1 
        else:
            failed += 1
    return passed , failed
    
a,b = get_test_results(status_codes)

print(a)
print(b)


print()
def is_fast(response_time):
    if response_time < 2 :
        return True
    else:
        return False

response_times = [1.2, 2.5, 0.8, 3.1, 1.9] 
fast = 0
slow = 0 
for time in response_times:
    result = is_fast(time)
    if result:
        fast += 1
    else:
        slow += 1

print("Fast:",fast)
print("Slow:",slow)


print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code, response_time):
    if (status_code == 200 or status_code == 201) and response_time < 2:
        return True
    else:
        return False

passed = 0 
failed = 0 

for response in responses:
    result = check_api(response["status"],response["time"])
    if result:
        passed +=1 
    else:
        failed += 1
print("Passed",passed)
print("Failed:",failed)


print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code,response_time):
    if (status_code == 200 or status_code == 201) and response_time < 2:
            return True
    else:
            return False
results= []
for response in responses:
    result = check_api(response["status"],response["time"])
    results.append(result)

print(results)

print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code,response_time):
    if (status_code == 200 or status_code == 201) and response_time <2:
        return True
    else:
        return False
    
failed_statuses = []

for fail in responses:
    result  = check_api(fail["status"],fail["time"])
    if result == False:
        failed_statuses.append(fail["status"])

print(failed_statuses)

print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code,response_time):
    if (status_code == 200 or status_code == 201) and response_time <2:
        return True
    else:
        return False

failed_responses =[]

for fai in responses:
    result = check_api(fai["status"],fai["time"])
    if result == False:
        failed_responses.append(fai)

print(failed_responses)

print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code,response_time):
    if status_code != 200 and status_code != 201:
        return "Неверный статус"
    elif (status_code == 200 or status_code == 201) and response_time >= 2:
        return "Медленный ответ"
    else:
        return "Тест пройден"
for li in responses:
    result = check_api(li["status"], li["time"])
    print(result)


print()
responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]
def check_api(status_code,response_time):
    if status_code != 200 and status_code != 201:
        return "Неверный статус"
    elif (status_code == 200 or status_code == 201) and response_time >= 2:
        return "Медленный ответ"
    else:
        return "Тест пройден"
    
errors = []

for error in responses:
    result = check_api(error["status"],error["time"])
    if result != "Тест пройден":
        errors.append(result)
print(errors)

print()

responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]

def check_api(status_code,response_time):
    if status_code != 200 and status_code != 201:
        return "Неверный статус"
    elif (status_code == 200 or status_code == 201) and response_time >= 2:
        return "Медленный ответ"
    else:
        return "Тест пройден"

status_errors = 0 
slow_errors = 0

for response in responses:
    result = check_api(response["status"],response["time"])
    if result == "Неверный статус":
        status_errors += 1
    elif result == "Медленный ответ":
        slow_errors += 1

print("Status erorrs:", status_errors)
print("Slow errors:", slow_errors) 

print()

responses = [
    {"status": 200, "time": 1.2},
    {"status": 404, "time": 0.5},
    {"status": 201, "time": 1.8},
    {"status": 200, "time": 2.5},
    {"status": 500, "time": 3.0}
]

def check_api(status_code,response_time):
    if (status_code == 200 or status_code == 201) and response_time < 2:
        return True
    else:
        return False

passed = 0 
failed = 0 

for response in responses:
    result = check_api(response["status"],response["time"])
    if result == True:
        passed += 1 
    else:
        failed += 1


total = passed/len(responses) * 100 

print("Passed:",passed)
print("Failed:",failed)
print("Pass rate:",total)

print()

def calculate_pass_rate(passed,total):
    if total == 0:
        return 0 
    else:
        return passed / total * 100

result1 = calculate_pass_rate(2,5)
result2 =calculate_pass_rate(5, 5)
result3 =calculate_pass_rate(0, 0)

print(result1)
print(result2)
print(result3)

print()
def check_response_time(response_time):
    if response_time < 2 :
        return "Быстрый ответ"
    elif response_time == 2:
        return "Граничное значение"
    else:
        return "Медленный ответ"

result1 = check_response_time(1.9)
result2 = check_response_time(2.0)
result3 = check_response_time(2.1)
result4 = check_response_time(0)

print(result1)
print(result2)
print(result3)
print(result4)


print()

responses = [
    {"status": 200, "time": 1.2},
    {"status": 201, "time": 1.8},
    {"status": 404, "time": 0.6},
    {"status": 200, "time": 2.4},
    {"status": 500, "time": 3.1},
    {"status": 200, "time": 0.9}
]

def check_api(status_code, response_time):
    if (status_code == 200 or status_code == 201) and response_time < 2:
        return True
    else:
        return False

passed = 0 
failed = 0 

failed_responses = []

for response in responses:
    result = check_api(response["status"],response["time"])
    if result:
        passed += 1
    else:
        failed += 1
        failed_responses.append(response)

tota = passed / len(responses) * 100 

print("Passed:",passed)
print("Failed",failed)
print("Pass rate:",tota)
print("Failed responses:",failed_responses)


print()
def parse_status(status_code):

    try:
        number = int(status_code)
        return number 
    except ValueError:
        return "Ошибка преобразования"

result1 = parse_status("200")
result2 = parse_status("400")
result3 = parse_status("error")

print(result1)
print(result2)
print(result3)