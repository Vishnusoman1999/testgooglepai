import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st



scope =['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

cred = ServiceAccountCredentials.from_json_keyfile_name('economicdata.json', scope)

client = gspread.authorize(cred)

#sheet  = client.create('fistsheet')

#sheet.share('shanvishnu007@gmail.com',perm_type='user',role='writer')

wks = client.open('All Data').sheet1
i = wks.get('A1:BG8625')

df = pd.DataFrame(i[1:],columns=i[0])

st.write(df)
