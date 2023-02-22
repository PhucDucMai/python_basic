'''
Chương trình quản lý các CD(Công đoàn)
Thông tin công đoàn:
 - Tên CD
 - Tên Ca sĩ
 - Số bài hát
 - Giá thành
 ---> Yêu cầu: Chương trình liệt kê ra danh sách CD và tổng tiền của các CD đó
'''

class Programing_CD():
    def __init__(self,tenCD , tenCaSi , soBaiHat , giaCD):
        self.tenCD = tenCD
        self.tenCaSi = tenCaSi
        self.soBaiHat = soBaiHat
        self.giaCD = giaCD

if __name__ == '__main__':
    # Save information of CD
    lst_cd = []
    n = int(input('Enter number of CD: '))
    for i in range(n):
        tenCD = input("Nhập vào tên CD: ")
        tenCaSi = input("Nhập vào tên ca sĩ: ")
        soBaiHat = int(input("Nhập vào số bài hát: "))
        giaCD = float(input("Nhập vào giá của CD: "))
        print("")
        cd = Programing_CD(tenCD , tenCaSi , soBaiHat , giaCD)
        lst_cd.append(cd)

    # In ra thông tin của các CD có trong danh sách
    for i in range(len(lst_cd)):
        print("------------------- Thông tin CD thứ {0} -------------------".format(i+1))
        print("Tên CD: " , lst_cd[i].tenCD)
        print("Tên ca sĩ: ", lst_cd[i].tenCaSi)
        print("Số bài hát: ", lst_cd[i].soBaiHat)
        print("Giá CD: ", lst_cd[i].giaCD)
    # Tính tổng số tiền của các CD:
    total_money = 0
    for cd in lst_cd:
        total_money += cd.giaCD
    print("\n Tổng tiền CD: " , total_money)

