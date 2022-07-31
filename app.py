import streamlit as st 
import boto3 
 
st.title('Text Extraction using AWS') 
 
img_file=st.file_uploader('upload image',type=['jpg','png','jpeg']) 
if img_file is not None: 
    file_details={} 
    file_details['name']=img_file.name 
    file_details['type']=img_file.type   
    file_details['size']=img_file.size 
    st.write(file_details) 
     
    with open('input.jpg','wb') as f: 
        f.write(img_file.getbuffer()) 
 
    client=boto3.client('rekognition') 
    imageSource=open('input.jpg','rb') 
    response=client.detect_text(Image={'Bytes':imageSource.read()}) 
    st.write(response)