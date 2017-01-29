# -*- coding: utf-8 -*-

"""
Module implementing StringTableDialog.
"""
import xlrd
import os.path
import time
import os
import sys
import codecs
from Tools import Tools

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QFileDialog

from Ui_UIStringTableDlg import Ui_Dialog


class StringTableDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(StringTableDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_mBroseExcelBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        fileName1, filetype = QFileDialog.getOpenFileName(self,  
                                   "选取文件",  
                                    "",  
                                    "Excel Files (*.xlsx)")   #设置文件扩展名过滤,注意用双分号间隔
        self.mExcelPath.setText(fileName1) 
        
        
    @pyqtSlot()
    def on_mLuaPathBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        fileName2 = QFileDialog.getExistingDirectory(self,  
                                    "文件保存",                                  
                                    "")  
        self.mOutputPath.setText(fileName2)
    
    @pyqtSlot()
    def on_mOutputBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        filename = self.mExcelPath.text()
        output_path = self.mOutputPath.text()
        
        if not os.path.exists(filename):
            self.mStateTipTxt.setText("请输入正确的excel文件路径")
            return
        data, ret, errstr = self.make_table(filename)
        if ret != 0:
            self.mStateTipTxt.setText(errstr)
        else:
            self.mStateTipTxt.setText("输出成功")
            self.write_to_lua_script(data,  output_path)
    def write_sheet_to_lua_script(self, output_path, sheet_name, sheet):
        sheet_name = sheet_name.lower()
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        output_filename = output_path + "/" + sheet_name + ".lua"
        outfp = codecs.open(output_filename, 'w', 'UTF-8')
        create_time = time.strftime("%a %b %d %H:%M:%S %Y", time.gmtime(time.time()))
        outfp.write(Tools.SCRIPT_HEAD_STR %(create_time))
        
        outfp.write("local " + sheet_name + " =")
        outfp.write("\n{")
        
        for row_idx, row in sheet.items():
            row_key = Tools.get_string(row[0])
            outfp.write("\t[" + "\"" + row_key + "\"" + "] = ")
            row_value = Tools.get_string(row[1])
            outfp.write("\"" + row_value + "\",\n")
        outfp.write("}\n")
        
        outfp.write("\nfunction " + sheet_name + ".get_text(key, ...)\n\treturn string.format(" + sheet_name + "[key], ...);\nend\n")
        outfp.write("\nfunction " + sheet_name + ".get_temp_text(key, ...)\n\treturn string.format(key, ...);\nend\n")

        outfp.write("\nreturn " + sheet_name)

        outfp.close()
        
    def write_to_lua_script(self, excel_data, output_path):
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        for(sheet_name, sheet) in excel_data["data"].items():
            global_dir = output_path + "\\" + sheet_name[12:]
            self.write_sheet_to_lua_script(global_dir, "string_table", sheet)
    
    def handle_one_sheet(self, excel,  sheet):
        sheet_name = sheet.name.replace(" ", "_")
        if not sheet_name.startswith("OUT_"):
            return
        sheet_name = sheet_name[4:].lower()
        print(sheet_name + " sheet")
        excel["data"][sheet_name] = {}
        
        if sheet.ncols < 2:
            return
        row_idx = 0
        for row_idx in range(0,  sheet.nrows):
            row = {}
            col_idx = 0
            for col_idx in range(0,  sheet.ncols):
                value = sheet.cell_value(row_idx,  col_idx)
                row[col_idx] = Tools.format_str(value)
            excel["data"][sheet_name][row[0]] = row
    
    def make_table(self, filename):
        if not os.path.isfile(filename):
            print("%s is not a valid filename" % filename)
            return
        book_xlrd = xlrd.open_workbook(filename)
        
        excel = {}
        excel["filename"] = filename
        excel["data"] = {}
        
        for sheet in book_xlrd.sheets():
            self.handle_one_sheet(excel, sheet)
        return excel, 0, "ok"
