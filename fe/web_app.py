import streamlit as st
import requests
# from fastapi import HTTPException

st.title('Image2Text')
# uploading the file
uploaded_file = st.file_uploader("Upload the image to extract it's text and send it to the database:", type=['png', 'jpg', 'jpeg', 'pdf'])
if uploaded_file is not None:
    st.image(uploaded_file)

    # creating request to api
    response = requests.post(url='http://localhost:8000/uploadimages/', files = {'file': uploaded_file})

    if response.status_code == 200:
        result = response.json()
        st.write('Successfuly uploaded the image!')
        st.write('Extracted Text:')
        st.write(result['fields'])
    # else:
    #     raise HTTPException(404, 'Incorrect image format or file not found.')
    else:
        st.write('File upload failed')