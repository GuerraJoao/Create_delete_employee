import requests, json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # response0 = requests.post('https://dummy.restapiexample.com/api/v1/create', {"id":33,"employee_name":"Joao","employee_salary":10650,"employee_age":121,"profile_image":""}, headers={"User-Agent": "XY"})
    # response = requests.get('https://dummy.restapiexample.com/api/v1/employee/23', headers={"User-Agent": "XY"})

    # response = requests.get('https://dummy.restapiexample.com/api/v1/employees', headers={"User-Agent": "abc"})
    # parsedResponse = json.loads(response.text)
    response = requests.get(f'https://dummy.restapiexample.com/api/v1/delete/2', headers={"User-Agent": "XY"})
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
