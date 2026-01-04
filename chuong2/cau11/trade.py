import json
from datetime import datetime

giao_dich_tien = []
giao_dich_vang = []

def nhap_giao_dich_tien():
    print("Nhập giao dịch tiền:")
    ma = input("Mã giao dịch: ")
    ngay = input("Ngày giao dịch (YYYY-MM-DD): ")
    so_tien = float(input("Số tiền: "))
    mo_ta = input("Mô tả: ")

    giao_dich = {"id": ma, "loai": "tiền", "so_tien": so_tien, "mo_ta": mo_ta, "ngay": ngay }

    giao_dich_tien.append(giao_dich)

def nhap_giao_dich_vang():
    print("Nhập giao dịch vàng:")
    ma = input("Mã giao dịch: ")
    ngay = input("Ngày giao dịch (YYYY-MM-DD): ")
    so_luong = float(input("Số lượng vàng: "))
    don_gia = float(input("Đơn giá: "))
    mo_ta = input("Mô tả: ")

    giao_dich = { "id": ma, "loai": "vàng", "so_luong": so_luong, "don_gia": don_gia, "mo_ta": mo_ta, "ngay": ngay }

    giao_dich_vang.append(giao_dich)
 
def ghi_vao_file():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{timestamp}.json"

    du_lieu = {"giao_dich_tien": giao_dich_tien, "giao_dich_vang": giao_dich_vang }

    with open(file_name, "w", encoding="utf-8") as file: json.dump(du_lieu, file, indent=4, ensure_ascii=False)

    print(f"\nDữ liệu đã được ghi vào tệp: {file_name}")

def main():
    print("==== QUẢN LÝ GIAO DỊCH ====")
    while True:
        print("\n1. Nhập giao dịch tiền")
        print("2. Nhập giao dịch vàng")
        print("0. Kết thúc nhập")
        chon = input("Chọn chức năng: ")

        if chon == "1": nhap_giao_dich_tien()
        elif chon == "2": nhap_giao_dich_vang()
        elif chon == "0": break
        else: print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

    while True:
        luu = input("\nBạn có muốn ghi giao dịch vào tệp không? (1: Có, 0: Không): ")
        if luu == "1":
            ghi_vao_file()
            break
        elif luu == "0":
            print("Dữ liệu KHÔNG được ghi vào tệp.")
            break
        else: print("Vui lòng nhập 1 hoặc 0.")

if __name__ == "__main__": main()