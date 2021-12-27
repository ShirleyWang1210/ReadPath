import pandas as pd
import xlrd
import xlwt
from datetime import date, datetime
import os
excel_path = r'C:\Users\shirley4.wang\PycharmProjects\pythonProject\inbound'
datanames = os.listdir(excel_path)
excel_name = datanames[0]
excel_full_path = os.path.join(excel_path, excel_name)
workbook = xlrd.open_workbook(excel_path)

