import requests

BASE_URL = "http://127.0.0.1:8000/items"

# ---------- CREATE (POST) ----------
new_item = {"name": "iPad", "price": 499.99}
response = requests.post(BASE_URL, json=new_item)
print("POST:", response.status_code, response.json())

# ---------- READ (GET) ----------
item_id = 1
response = requests.get(f"{BASE_URL}/{item_id}")
print("GET:", response.status_code, response.json())

# ---------- UPDATE (PUT) ----------
updated_item = {"name": "iPad Pro", "price": 999.99}
response = requests.put(f"{BASE_URL}/{item_id}", json=updated_item)
print("PUT:", response.status_code, response.json())

# ---------- DELETE ----------
response = requests.delete(f"{BASE_URL}/{item_id}")
print("DELETE:", response.status_code, response.text)

animal = ['lion', 'tiger', 'snake']
birds = ('pigeon', 'woodpecker', 'peaccock')
new_lst = animal + list(birds)
print(new_lst)