import xlrd    # xls 读取
import xlwt    # xls 写入
from xlutils.copy import copy    # xls操作，目前使用 copy
import faker # 用于生成虚拟数据，欺骗者


def std_xlrd():
    wb = xlrd.open_workbook(r'xls\a.xls')
    sheets = wb.sheets()
    sheet = sheets[0]
    rows = sheet.nrows
    cols = sheet.ncols
    print(rows,cols)
    for row in range(rows):
        for col in range(cols):
            print(sheet.cell(row,col).value,end="|")
        print("\n")


def std_xlutils():
    wb = xlrd.open_workbook(r'xls\a1.xls', formatting_info=True)
    xwb = copy(wb)
    sheet = xwb.get_sheet('a')
    rows = sheet.get_rows()
    fake = faker.Faker()
    for i in range(len(rows), 200):
        sheet.write(i, 0, fake.first_name() + ' ' + fake.last_name())
        sheet.write(i, 1, fake.address())
        sheet.write(i, 2, fake.phone_number())
        sheet.write(i, 3, fake.city())
    xwb.save(r'xls\a1.xls')


def std_xlwt():
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("a")
    head_data = [1, 2, 3, 4, 5]
    for head in head_data:
        sheet.write(0, head_data.index(head), head)

    fake = faker.Faker()
    for i in range(1, 100):
        sheet.write(i, 0, fake.first_name() + " " + fake.last_name())
        sheet.write(i, 1, fake.address())
        sheet.write(i, 2, fake.phone_number())
        sheet.write(i, 3, fake.city())
    wb.save("a.xls")

if __name__ == "__main__":
    std_xlrd()