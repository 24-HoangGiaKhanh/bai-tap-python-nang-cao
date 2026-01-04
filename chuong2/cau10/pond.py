import json
from collections import Counter

with open("company.json", "r", encoding="utf-8") as file: data = json.load(file)

company_name = data.get("company_name", "Không rõ tên công ty")
address = data.get("address", "Không rõ địa chỉ")
employees = data.get("employees", [])

total_employees = len(employees)

department_counts = Counter(emp["department"] for emp in employees)

print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {address}")
print(f"Tổng số nhân viên: {total_employees}\n")

print("Thống kê nhân viên theo đơn vị:")
print(f"{'Tên đơn vị':<25} {'Số nhân viên':<15} {'Tỷ lệ (%)':<10}")
print("-" * 55)

for dept, count in department_counts.items():
    ratio = (count / total_employees) * 100
    print(f"{dept:<25} {count:<15} {ratio:.2f}%")
