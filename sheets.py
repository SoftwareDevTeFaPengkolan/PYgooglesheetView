import gspread


from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint as pp

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)
client = gspread.authorize(creds)

sheet = client.open("datasiswa").sheet1



#Getting data from the sheet
data = sheet.get_all_records()

pp(data)

