import requests
import json

history = []

while True:
	prompt = input("You: ")
	history.append({"role":"user","content":prompt})
	ask = {
        "model":
        {
            "id":"gpt-3.5-turbo",
            "name":"GPT-3.5",
            "maxLength":12000,
			"tokenLimit":4096
        },
        "messages":history,
		"key":"",
		"prompt":"You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
		"temperature":0.7
        }
	resp = requests.post(url="https://chat.aivvm.com/api/chat",data=json.dumps(ask))
	print(f"GPT: {resp.text}")
	history.append({"role":"assistant","content":resp.text})