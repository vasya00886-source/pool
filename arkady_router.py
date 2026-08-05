import json
import os
import urllib.request

class ArkadyRouter:
    def __init__(self):
        self.providers = {
            'ollama': {'url': 'http://localhost:11434', 'key': None},
            'openrouter': {'url': 'https://openrouter.com/api', 'key': 'your_openrouter_key'},
            'groq': {'url': 'https://api.groq.com', 'key': 'your_groq_key'},
            'cerebras': {'url': 'https://api.cerebras.com', 'key': 'your_cerebras_key'}
        }

    def call(self, provider, data):
        try:
            url = self.providers[provider]['url']
            key = self.providers[provider]['key']

            headers = {
                'Content-Type': 'application/json'
            }
            if key:
                headers['Authorization'] = f'Bearer {key}'

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            response = urllib.request.urlopen(req)
            return json.load(response)
        except Exception as e:
            print(f"Error calling provider {provider}: {e}")
            return None