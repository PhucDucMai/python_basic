'''
GiaoDichTienTe và GiaoDichVang kế thừa từ GiaoDich
---> Nhập xuất danh sach giao dịch
     Tính tong số lượng cho từng loại
     Tính tổng số tiền cho từng loại

GiaoDichTienTe: MaGiaoDich , NgayGiaoDich , TyGia , SoLuong , LoaiTien , LoaiGiaoDich
GiaoDichVang: MaGiaoDich , NgayGiaoDich , DonGia , SoLuong , LoaiVang
'''


class GiaoDich():

    def __init__(self, MaGiaoDich, NgayGiaoDich):
        self.MaGiaoDich = MaGiaoDich
        self.NgayGiaoDich = NgayGiaoDich


class GiaoDichVang(GiaoDich):

    def __init__(self, MaGiaoDich, NgayGiaoDich, DonGia, SoLuong, LoaiVang):
        super().__init__(MaGiaoDich, NgayGiaoDich)
        self.DonGia = DonGia
        self.SoLuong = SoLuong
        self.LoaiVang = LoaiVang

    def __str__(self):
        return "Giao dịch vàng: \n MaGiaoDich: {} \n NgayGiaoDich : {} \n DonGia: {} \n SoLuong: {} \n LoaiVang: {} \n TongTien = {}".format(
            self.MaGiaoDich, self.NgayGiaoDich, self.DonGia, self.SoLuong, self.LoaiVang, self.SoLuong * self.DonGia)


class GiaoDichTienTe(GiaoDich):

    def __init__(self, MaGiaoDich, NgayGiaoDich, TyGia, SoLuong, LoaiTien, LoaiGiaoDich):
        super().__init__(MaGiaoDich, NgayGiaoDich)
        self.TyGia = TyGia
        self.SoLuong = SoLuong
        self.LoaiTien = LoaiTien
        self.LoaiGiaoDich = LoaiGiaoDich

    def __str__(self):
        tongtien = 0
        if (self.LoaiGiaoDich == 1):
            tongtien = self.SoLuong * self.TyGia
        elif (self.LoaiGiaoDich == 2):
            tongtien = self.SoLuong * self.TyGia * 1.05
        return "Giao dịch tiền: \n MaGiaoDich: {} \n NgayGiaoDich: {} \n TyGia: {} \n SoLuong: {} \n LoaiTien: {} \n LoaiGiaoDich: {} \n TongTien = {}".format(
            self.MaGiaoDich, self.NgayGiaoDich, self.TyGia, self.SoLuong, self.LoaiTien, self.LoaiGiaoDich , tongtien)


if __name__ == '__main__':
    # Nhập dữ liệu
    lst_giaodich = []
    stt = 1
    while (stt == 1):
        MaGiaoDich = input("Nhập mã giao dịch: ")
        NgayGiaoDich = input("Nhập ngày giao dịch: ")
        check = 1
        while (check == 1):
            LoaiGiaoDich = int(input("1. Giao dịch vàng \t 2. Giao dịch tiền tệ \n Chọn loại giao dịch: "))
            if (LoaiGiaoDich != 1 and LoaiGiaoDich != 2):
                print("Loại giao dịch không hợp lệ. Xin kiểm tra lại")
            else:
                # Giao dịch vàng
                if LoaiGiaoDich == 1:
                    DonGia = float(input("Nhập vào đơn giá vàng: "))
                    SoLuong = int(input("Nhập vào số lượng: "))
                    while (True):
                        LoaiVang = int(input("1. Vàng 18k \t 2. Vàng 24k \t 3. Vàng 9999 \n Chọn loại vàng: "))
                        if (LoaiVang != 1 and LoaiVang != 2 and LoaiVang != 3):
                            print("Loại vàng không hợp lệ. Xin kiểm tra lại")
                        else:
                            temp = GiaoDichVang(MaGiaoDich, NgayGiaoDich, DonGia, SoLuong, LoaiVang)
                            lst_giaodich.append(temp)
                            check = 2
                            # stt = int(input("Nhập 1 để tiếp tục"))
                            break
                # Giao dịch tiền tệ
                elif LoaiGiaoDich == 2:
                    TyGia = float(input("Nhập vào tỷ giá: "))
                    SoLuong = int(input("Nhập vào số lượng: "))
                    test = 1
                    while (test == 1):
                        LoaiTienTe = int(input("1. USD \t 2. EUR \t 3. AUD \n Chọn loại tiền: "))
                        test_loaitiente = 1
                        while (test_loaitiente == 1):
                            if (LoaiTienTe != 1 and LoaiTienTe != 2 and LoaiTienTe != 3):
                                print("Loại tiền tệ không hợp lệ. Xin kiểm tra lại")
                            else:
                                while (True):
                                    LoaiMuaBan = int(input("1. Mua \t 2. Bán \n Chọn loại mua bán: "))
                                    if (LoaiMuaBan != 1 and LoaiMuaBan != 2):
                                        print("Loại mua bán không hợp lệ. Xin kiểm tra lại")
                                    else:
                                        temp = GiaoDichTienTe(MaGiaoDich, NgayGiaoDich, TyGia, SoLuong, LoaiTienTe,
                                                              LoaiMuaBan)
                                        lst_giaodich.append(temp)
                                        check = 2
                                        test_loaitiente = 2
                                        test = 2
                                        break

        stt = int(input("Nhập 1 để tiếp tục: "))
    print("----------------------- Quản lý giao dịch -----------------------")
    for i in lst_giaodich:
        print(i)
