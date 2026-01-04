import json

json_data = '''{
    "name": "Nguyễn Văn A",
    "age": 30,
    "email": "vana@example.com",
    "is_employee": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {"street": "123 Đường ABC","city": "Hà Nội","postal_code": "100000"}
    }'''


python_obj = json.loads(json_data)

print("Dữ liệu sau khi chuyển đổi:")
print(python_obj)

print("\nTên:", python_obj["name"])
print("Kỹ năng đầu tiên:", python_obj["skills"][0])
print("Thành phố:", python_obj["address"]["city"])
