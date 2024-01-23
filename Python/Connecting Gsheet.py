import gspread 
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet(document_name , sheet_name):
    # Define the scope and load the credentials file
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\pranuh\Desktop\Projects\creds.json", scope)
    
    # Authorize the client and open the specified sheet
    client = gspread.authorize(creds)
    document = client.open(document_name)
    sheet = document.worksheet(sheet_name)
    load_sheet = sheet.get_all_values()                     # Get all values from the sheet 
      
    return load_sheet
