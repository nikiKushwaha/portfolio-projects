# Description: This is a stock market dashboard to show same charts and data on some stock

#Import the libraries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           import streamlit as st
import pandas as pd
from PIL import Image


#add a title and an image
st.write("""
 # Stock Market Web Application
 Visually show data on a stock! Date range from jan 2,
  2,2021 - Sep 5, 2021)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

 image = Image.open("C:/Users/Nikita Kushwaha/Visual stdio/python_program/stock_image/WMT(Walmark-flipkart).csv")
 st.image(image,use_column_width=True)

 #Create a sidebar header
 st.sidebar.header('User Input')

 #Create a function to get the users input
 def get_input():
     start_date = st.sidebar.text_input("Start Date", "2020-11-06")
     end_date = st.sidebar.text_input("End Date", "2021-11-05")
     stock_symbol = st.sidebar.text_input("Stock Symbol","walmark")
     return start_date, end_date, stock_symbol 

 #Create a function to get the company name
  def get_company_name(symbol):
    if symbol == 'WMT(Walmark-flipkart)':
       return 'Flipkart'
    elif symbol == 'TSLA':
       return 'Tesla' 
    elif symbol == 'GOOG': 
       return 'Alphabet'
    else:
       'None'
 
 #Create a function to get the proper company data and the proper timeFrane from the user start date to   
  def get_data(symbol,start,end):

 #Load the data
  if symbol.upper() == 'WMT(Walmark-flipkart)':
      df = pd.read_csv("C:/Users/Nikita Kushwaha/Visual stdio/python_program/stocks/walmart.csv")                                 
  
  else:
      df = pd.DataFrame(columns = ['Date', 'close', 'Open', 'Volume', 'Adj Close', 'High', Low])

 #Get the date range
 start = pd.to_datetime(start)
 end = pd.to_datetime(end)

 #Set the start and and index rows both to 0
 start_row = 0
 end_row = 0

 #Start the date from the topof the data set and go down to see if the users start date is less than or equal to the date in the data
  for i in range(0, len(df)):
      if start <= pd.to_datetime(df['Date'][i]):
          start_row = i
           break
 
 #Start from the bottom of the data set and go up to see if the users and date is greater than or equal to the data
  for j in range(0, len(df)):
      if end >= pd.to_datetime(df['Date'][len(df)-1]):
         end_row = len(df) -1 - j
         break

 #Set the index to the date
   df = df.set_index(pd.DatetimeIndex(df['Date'].values))   
       return df.iloc[start_row:end_row+1, :] 

 #Get the users input
 start, end, symbol = get_input()
 #Get the data
  df = get_data(symbol, start, end)
 #Get the company name
  company_name = get_company_name(symbol.upper())    

 #Display the close price
 st.header(company_name+" Close Price\n")   
 st.line_chart(df['close'])

 #Display the volume
  st.header(company_name+" Volumn\n")
  st.line_chart(df['Volumn']) 

 #Get statistics on the data
  st.header('Data Statistics')
  st.write(df.describe())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 