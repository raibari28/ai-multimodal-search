# xlsx_parser.py
import openpyxl

def parse_xlsx(file_path):
    wb = openpyxl.load_workbook(file_path)
    text = []
    for sheet in wb:
        for row in sheet.iter_rows(values_only=True):
            text.append(" ".join([str(cell) for cell in row if cell]))
    return "\n".join(text)
