import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib
import time

json_key = json.load(open('creds.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(credentials)
sheet = gc.open("test_budgets_export")

worksheet = sheet.get_worksheet(1)

all_cells = worksheet.range('A1:A149')

for cell in all_cells:
        # print cell.value
        keyword = cell.value
        url = 'https://api.semrush.com/?type=phrase_this&key=YOUR_SEMRUSH_API_KEY&export_columns=Db,Ph,Nq&database=us&phrase='
        urlwithkeyword = url + keyword
        # print urlwithkeyword
        f = urllib.urlopen(urlwithkeyword)
        time.sleep(0.5)
        myfile = f.read()
        print myfile
