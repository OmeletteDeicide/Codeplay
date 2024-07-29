import requests

API_URL = "https://emkc.org/api/v2/piston/execute"
LANGUAGE = "py" 
VERSION = "3.10"

user_code = """
def my_sum_func(a, b):
    return a + b
"""

test_code = """
if assert(my_sum_func(12, 42) == 54)
"""

complete_code = f"{user_code}\n\n{test_code}"

response = requests.post(
    API_URL,
    json={
        "language": LANGUAGE,
        "version": VERSION,
        "files": [{"name": "main.py", "content": complete_code}]
    }
)

result = response.json()
output = result.get('run', {}).get('stdout', '') or result.get('run', {}).get('stderr', '')
print("Output:")
print(output)