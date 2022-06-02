from openpyxl import Workbook, workbook

def create_workbook():
  # workbook 생성
  wb = Workbook()
  # 시트명 가져옴
  ws = wb.active
  # 시트명 변경
  ws.title = 'testsheet'
  # 엑셀 저장
  wb.save('C:/Users/User/Desktop/excel_create_macro.xlsx')
  wb.close()


create_workbook()