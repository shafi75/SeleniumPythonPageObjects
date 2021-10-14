import openpyxl

path="..//excel//testdata.xlsx"
wb=openpyxl.load_workbook(path)
sheet=wb["LoginTest"]
for rows in range(4,8):
    for  cols in range(1,4):
        sheet.cell(row=rows,column=cols).value="Hello"

wb.save(path)

