import openpyxl
ms = openpyxl.load_workbook('student.xlsx')
print(type(ms))
sheet = ms.sheetnames
print(sheet)