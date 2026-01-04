import json

python_obj = {
    "name": "Nguyễn Văn A",
    "age": 30,
    "email": "vana@example.com",
    "is_employee": True,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Đường ABC",
        "city": "Hà Nội",
        "postal_code": "100000"
    }
}

json_string = json.dumps(python_obj, ensure_ascii=False, indent=4)

print("Chuỗi JSON:")
print(json_string)

def print_values(obj):
    if isinstance(obj, dict):
        for value in obj.values(): print_values(value)
    elif isinstance(obj, list):
        for item in obj: print_values(item)
    else: print(obj)

print("\nTất cả các giá trị:")
print_values(python_obj)
