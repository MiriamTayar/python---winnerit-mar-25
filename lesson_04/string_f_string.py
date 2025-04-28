name = "Alex"
profession = "QA"
experience = 6

print(f"Name: {name}, Profession: {profession} , Experience: {experience}")
print(f"Name: {name.upper()}, Profession: {profession.lower()} , Experience: {experience * 2}")
print(f"{name=}, {profession = }, {experience =}")

BASE_URL = "www.example.io"
BASE_API_URL = f"{BASE_URL}/api/v1"
BASE_ITEMS_URL = f"{BASE_API_URL}/items"
print(BASE_API_URL)
print(BASE_ITEMS_URL)