info = {
    "name": "John",
    "surname": "Doe",
    "skills": {
        "html": 'True',
        "css": 'True',
        "js": 'False',
        "pythonFrameworks": {
            "flask": 'False',
            'django': {
                'django_rest_framework': 'True',
                'django': {
                    'dtl': 'True'
                }
            }
        }
    }
}


def recursive_check(arr):
    flag = 0
    for key, value in arr.items():
        if isinstance(value, dict) == True:
            arr = arr[key]
            flag = 1
            recursive_check(arr)

    if flag == 0:
        print(arr)


recursive_check(info)