from openpyxl import Workbook
from Models.ExcelModel import ExcelModel


class Generate_excel:
    def __init__(self):
        pass

    def generate_excel(self, order, client, supplier, shipment):
        wb = Workbook()
        ws = wb.active()
        ws.title = "Order_info"
        cells_order = ['A1', 'A2', 'A3', 'A4', 'A5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1']
        cells_client = ['A20', 'A21', 'A22']
        cells_supplier = ['B20', 'B21', 'B22']
        #cells_products = ['A7','B7','C7','D7','E7','F7','G7','H7']
        letter_product = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(order.number_of_product()):
            row_index = 7 + i
            new_cp = [letter + str(row_index) for letter in letter_product]
            cells_order.append(new_cp)

        cells_shipment=['E1','E2','E3','E4','E5']
        order.print_to_cell(ws, cells_order)
        client.print_to_cell(ws, cells_client)
        supplier.print_to_cell(ws, cells_supplier)
        shipment.print_to_cell(ws, cells_shipment)
        wb.save("test_excel.xlsx")