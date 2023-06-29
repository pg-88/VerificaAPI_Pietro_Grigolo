import streamlit as st
import requests
import json

def get_request(in1, in2, in3, base):
    url =f'{base}?rd={in1}&admin={in2}&market={in3}'
    response = requests.get(url=url)#.json()
    st.success(response.json()['Profit'])

def post_request(in1,in2,in3, base):
    reqUrl = base
    headersList = {
        "Content-Type": "application/json" 
        }

    payload = json.dumps({
        "rd": in1,
        "admin": in2,
        "market": in3
        })
    response = requests.request("POST", reqUrl, data=payload,  headers=headersList).json()
    st.success(response['Profit'])

def main():
    '''Interfaccia utente per inserimento dati per la chiamata api'''
    st.header('Profit Prediction')

    # campi input
    rd = st.number_input("Research and Developent spent:", min_value=0)
    admin = st.number_input("Administration spent:", min_value=0)
    market = st.number_input("Marketing spent:", min_value=0)

    # base url del servizio
    url = st.text_input(label="Base URL", value="http://localhost:8000/profit")

    if st.button("GET"):
        get_request(rd, admin, market, url)


    if st.button("POST"):
        post_request(rd, admin, market, url)


if __name__ == '__main__':
    main()