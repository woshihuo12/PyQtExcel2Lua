import xlrd
import os.path
import time
import os
import sys
import codecs

class Tools:
    SCRIPT_HEAD_STR = "-- This file is generated by program!\n\
-- Don't change it manaully.\n\
-- Create at:%s\n\
\n\
\n\
"
    @staticmethod
    def format_str(value):
        if type(value) == int or type(value) == float:
            value = str(value)
        
        value = value.replace('\"',  '\\\"')
        value = value.replace('\'', '\\\'')
        return value
    
    @staticmethod
    def handle_one_sheet(excel,  sheet):
        sheet_name = sheet.name.replace(" ", "_")
        if not sheet_name.startwith("OUT_"):
            return
        sheet_name = sheet_name[4:].lower()
        print(sheet_name + " sheet")
        excel["data"][sheet_name] = {}
        
        if sheet.ncols < 2:
            return {}, -1, "sheet[" + sheet_name + "]" + "coumns must >=2"
        row_idx = 0
        for row_idx in range(0,  sheet.nrows):
            row = {}
            col_idx = 0
            for col_idx in range(0,  sheet.ncols):
                value = sheet.cell_value(row_idx,  col_idx)
                row[col_idx] = format_str(value)
            excel["data"][sheet_name][row[0]] = row
    
    @staticmethod
    def get_string(value):
        if value is None:
            return ""
        return value