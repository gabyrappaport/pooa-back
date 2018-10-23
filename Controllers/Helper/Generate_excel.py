from flask import current_app as app
from openpyxl import Workbook, load_workbook
from Models.ExcelModel import ExcelModel
from openpyxl.drawing.image import Image


class GenerateExcel:
    def __init__(self):
        pass

    def generate_excel(self, order, client, supplier, filename):
        wb = load_workbook(app.config["EXCEL_FOLDER"] + '/order_template.xlsx')
        #wb.template = False #To change if we want a real template
        img = Image('public/excels/header_2.png')
        img.width = 563
        img.height = 110
        ws = wb.active
        ws.title = "Order_info"
        cells_order = ['A3', 'I24', 'F15', 'C14', 'F13', 'C55', 'C56', 'C57', 'F54', 'K15', 'C9']
        cells_client = ['A20', 'A21', 'C12']
        cells_supplier = ['B20', 'B21', 'F9']
        letter_product = ['B', 'K', 'C', 'D', 'F', 'G', 'I', 'J']
        for i in range(order.number_of_product()):
            row_index = 18 + i
            new_cp = [letter + str(row_index) for letter in letter_product]
            cells_order.append(new_cp)
        #cells_shipment=['E1','E2','E3','E4','E5']
        ws.add_image(img, 'B2')
        client.print_to_cell(ws, cells_client)
        order.print_to_cell(ws, cells_order)
        supplier.print_to_cell(ws, cells_supplier)
        #shipment.print_to_cell(ws, cells_shipment)
        wb.save(filename)