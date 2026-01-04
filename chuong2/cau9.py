import json

python_dict = {
    "email": "vana@example.com",
    "name": "Nguyễn Văn A",
    "age": 30,
    "is_employee": True,
    "address": {
        "city": "Hà Nội",
        "street": "123 Đường ABC",
        "postal_code": "100000"
    }
}

json_string = json.dumps(python_dict, indent=4, ensure_ascii=False, sort_keys=True)

print("Chuỗi JSON (được sắp xếp theo key, indent=4):\n")
print(json_string)

print("\nCác thành viên của đối tượng JSON:")
for key in sorted(python_dict.keys()): print(f"{key}: {python_dict[key]}")
