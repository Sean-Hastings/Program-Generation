from .rpe_chart import RPE_CHART

'''
TODO:
- Add formatting
- Add top row
- Add left column
'''
def add_rpe_chart(workbook):
    worksheet = workbook.add_worksheet("RPE Chart")

    # Add top row
    # ...

    # Add left column
    # ...

    # Add chart
    for i_row in range(len(RPE_CHART)):
        for i_column in range(len(RPE_CHART[0])):
            worksheet.write(i_row + 1, i_column + 1, RPE_CHART[i_row][i_column])
