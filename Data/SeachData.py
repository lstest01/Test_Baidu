import xlrd
def testData():
    sheet = xlrd.open_workbook("./test_BD.xlsx").sheet_by_index(0)

    col_num = sheet.ncols
    row_num = sheet.nrows
    testData = []

    for i in range(1,row_num):
        n = sheet.row_values(i)
        testData.append(n)
    return testData