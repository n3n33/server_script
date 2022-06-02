from openpyxl import Workbook, workbook

import logging
import sys

def create_workbook():
  # workbook 생성
  wb = Workbook()
  # 시트명 가져옴
  ws = wb.active
  # 시트명 변경
  ws.title = 'testsheet'
  logging.info('Workbook sheet renamed')
  # 엑셀 저장
  wb.save('C:/Users/User/Desktop/excel_create_macro.xlsx')
  logging.info('Excel stored')
  wb.close()


# create_workbook()