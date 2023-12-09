from xlrd import *

def read_locator(sname):
    wb = open_workbook("../Excel/Locator.xls")
    sh = wb.sheet_by_name(sname)
    row_count = sh.nrows
    d = {sh.row_values(i)[0]:(sh.row_values(i)[1], sh.row_values(i)[2]) for i in range(1, row_count)}
    return d

