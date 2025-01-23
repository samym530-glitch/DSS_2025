from PIL import Image
import numpy as np
import pandas as pd #2
import streamlit as st

im = Image.open("DSS_Pic.png")
image= np.array(im)
st.markdown(" <center>  <h1> Training Certificates Verification </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

st.image(image)
File="DSS.xlsx"
st.markdown(" <right>  <h1>Please Enter Serial Number </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
st.markdown(" <right>  <h1>                                     الرجاء إدخال كود الشهادة </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

SN = st.text_input("",value="",key="SN")
SN=SN.replace(' ','')
SN=SN.upper()
df = pd.read_excel(File,'Sheet1')
#df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]

#df['DATE']=df['DATE'].astype(str)
#df['DATE']=df['DATE'].str.split(' ').str[0]
#df['DATE']= pd.to_datetime(df['DATE'])
#df.dropna(axis=0, inplace=True)
df['RESULT']=df['RESULT'].astype('str').replace('1','Verification Code is Valid')

df['CERTIFICATE NO']=df['CERTIFICATE NO'].astype('str')

if SN in (df['CERTIFICATE NO'].unique()):
 Result=df[df['CERTIFICATE NO']==SN]

 Result=Result.T
else:
 Result=['Verification Code is not Valid']            


df.fillna(0)
if st.button("Verify"):
 st.write('Validation Status')           
 st.dataframe(Result)
 st.write('A certificate is only valid if the information matches the information provided above. If you have any questions or concerns, please contact Delta Safety at deltasafetyscience@gmail.com Or call our office at +201159417372')           
 st.write('Or you can communicate with us on WhatsApp through following link: https://wa.me/201159417372')
