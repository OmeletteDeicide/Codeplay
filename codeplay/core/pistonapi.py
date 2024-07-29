import requests

class PistonAPI:
    def __init__(self):
        self.url = "https://emkc.org/api/v2/piston/execute"
    
    def execute(self, language, source_code):
        payload = {
            "language": language,
            "source": source_code,
        }
        response = requests.post(self.url, json=payload)
        return response.json()

# Exécution d'un test simple
if __name__ == "__main__":
    api = PistonAPI()
    result = api.execute(language="python3", source_code="print('Hello, World!')")
    print(result)
