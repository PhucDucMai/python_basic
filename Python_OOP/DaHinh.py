'''
Chương trình tính chu vi và diện tích của các hình:
- Hình tròn
- Hình chữ nhật
- Hình tam giác
'''

import math


class HinhTron():
    def __init__(self, bankinh):
        self.bankinh = bankinh

    def ChuVi(self):
        ChuVi = 2 * math.pi * self.bankinh
        return "Chu vi hình tròn là: %.4f"%ChuVi

    def DienTich(self):
        DienTich = math.pi * pow(self.bankinh, 2)
        return "Diện tích hình chữ nhật: %.4f"%DienTich


class HinhChuNhat():
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def ChuVi(self):
        ChuVi = (self.chieudai + self.chieurong) * 2
        return "Chu vi của hình chữ nhật: %.4f"%ChuVi

    def DienTich(self):
        DienTich = self.chieudai * self.chieurong
        return "Diện tích của hình chữ nhật: %4f"%DienTich


if __name__ == '__main__':
    hinhtron = HinhTron(10)
    hcn = HinhChuNhat(2,5)

    print(hinhtron.ChuVi())
    print(hinhtron.DienTich())

    print(hcn.ChuVi())
    print(hcn.DienTich())
