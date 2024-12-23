from auth import spreadsheet_service
from auth import drive_service

def read_range(spreadsheet_id, sheet_name):
    range_name = f'{sheet_name}!A1:H10'  # retrieve data from existing sheet
    result = spreadsheet_service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))
    print('{0} rows retrieved.'.format(rows))
    return rows

def write_range(spreadsheet_id, sheet_name):
    range_name = f'{sheet_name}!A3:H3'  # the range to update in the existing sheet
    values = [["Ben", "Stiller", 50, 'Male', 'New Jersey', 'USA', '98989898989', 'j11292@example.com']]  # new row of data
    value_input_option = 'USER_ENTERED'
    body = {
    'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))





if __name__ == '__main__':
    ## NB: you must share edit permissions with the service account you created
    ## youtube link I used: https://www.youtube.com/watch?v=-vBbkrk9sdA&ab_channel=SpreadsheetPoint

    spreadsheet_id = "xxxxxxxx"
    sheet_name = "yyyyyy"
    write_range(spreadsheet_id, sheet_name)
    read_range(spreadsheet_id, sheet_name)
