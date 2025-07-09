import json
import requests

# Load dummy thread
with open("test_data/dummy_thread.json", "r") as f:
    thread = json.load(f)

# Send POST request
res = requests.post("http://127.0.0.1:8000/process-thread", json={"thread": thread})

# Show result
print("🧠 AI Output:")
print(json.dumps(res.json(), indent=2))
