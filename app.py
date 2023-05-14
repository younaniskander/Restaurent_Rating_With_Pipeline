import numpy as np
import pandas as pd
import streamlit as st 
import joblib

regressor=joblib.load('/kaggle/working/RestaurentRatingWithPipeline.pkl')


def welcome():
    return "Welcome All"


def predict_RestaurentRating(Has Table booking, Has Online delivery, Price_range , Votes, Cuisines):
      prediction=regressor.predict(pd.DataFrame({'Has Table booking':[Has Table booking], 'Has Online delivery':[Has Online delivery],
                                             'Price range':[Price_range],'Votes':[Votes],'Cuisines':[Cuisines])
  return  prediction
def main():
    st.title("BMW price prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Restaurent Rating prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    model = st.text_input("Has Table booking","Type Here")
    year = st.text_input("Has Online delivery","Type Here")
    transmission = st.text_input("Price_range","Type Here")
    mileage = st.text_input("Votes","Type Here")
    fuelType = st.text_input("Cuisines","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_bmwcar(Has Table booking, Has Online delivery, Price_range , Votes, Cuisines)
    st.success('The price is {} USD'.format(result))
    if st.button("About"):
        st.text("our app using streamlit")
        st.text("best of luck in your GP")
if __name__=='__main__':
    main()        
