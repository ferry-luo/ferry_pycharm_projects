from excel_response3 import ExcelResponse


def excelview(request):
    data = [
        ['Column 1', 'Column 2'],
        [1, 2],
        [23, 67]
    ]
    return ExcelResponse(data, 'my_data.xlsx')


