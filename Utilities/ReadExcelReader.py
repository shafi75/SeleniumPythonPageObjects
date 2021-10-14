from Utilities import ExcelReader
path="..//excel//testdata.xlsx"
sheetname="LoginTest"
rows=ExcelReader.getRowCount(path,sheetname)
cols=ExcelReader.getColCount(path,sheetname)
print(ExcelReader.getCellData(path,sheetname,1,1))
ExcelReader.setCellData(path,sheetname,1,3,"Age")