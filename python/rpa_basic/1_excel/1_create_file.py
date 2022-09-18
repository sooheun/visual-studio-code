from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "heunsheet"
wb.save("sample.xlsx")
wb.close()
