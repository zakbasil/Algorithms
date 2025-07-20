import openpyxl

def count_cell_colors(file_path, sheet_name):
    # Load the workbook and select the sheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    # Initialize a Counter to count colors

    # Iterate through all cells in the sheet
    for row in sheet.iter_rows():
        score = 0
        rowNo = 0
        for cell in row:
            rowNo = cell.row
            if cell.fill and cell.fill.start_color.index == 'FFB6D7A8':                
                score += 1
        sheet['O'+str(rowNo)] = score
        print(rowNo, score)
    workbook.save("C:\\Users\\basil\\Downloads\\resultSJEC.xlsx") 


# Example usage
file_path = 'C:\\Users\\basil\\Downloads\\Python Fundamentals Quiz (Responses).xlsx'
sheet_name = 'Form responses 1'
color_counts = count_cell_colors(file_path, sheet_name)
