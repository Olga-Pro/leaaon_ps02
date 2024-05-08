import requests
import pprint # библиотека для печати словарей

# Задание 1 (см.README.md)
url = " https://api.github.com"
my_params = {"q": 'html'} # параметры запроса в формате словаря

response = requests.get(url, params=my_params)
print("Задание 1")
print(f"Статус-код запроса = {response.status_code}")

result1 = response.json()
print("Результат запроса в формате JSON:")
pprint.pprint(result1)

# Задание 2 (см.README.md)
url = "https://jsonplaceholder.typicode.com/posts"
my_params = {"userId": '1'} # параметры запроса в формате словаря

response = requests.get(url, params=my_params)
result2 = response.json()
print("Задание 2")
print("Результат запроса в формате JSON:")
pprint.pprint(result2)

# Задание 3 (см.README.md)
url = "https://jsonplaceholder.typicode.com/posts"
my_data = {'title': 'foo',
             'body': 'bar',
             'userId': 1} #параметры запроса в формате словаря

response = requests.post(url, data=my_data)
print("Задание 3")
print(f"Статус-код запроса = {response.status_code}")

result3 = response.json()
print(f"Ответ post-запроса {result3}")
print("Еще вариант вывода результата запроса в формате JSON:")
pprint.pprint(result3)

