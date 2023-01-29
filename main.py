import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    '/Users/sebaty/PycharmProjects/excel/data/sebatyexcel-e4284260d5f2.json', scope)

client = gspread.authorize(creds)

sheet = client.open('sample_spreadsheet')

sheet_instance = sheet.get_worksheet(0)

records_data = sheet_instance.get_all_records()

print(records_data)

worksheet = sheet.add_worksheet(title="A sample Java worksheet", rows=100, cols=20)