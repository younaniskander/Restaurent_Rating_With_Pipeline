import numpy as np
import pandas as pd
import streamlit as st 
import joblib

regressor=joblib.load('/kaggle/working/RestaurentRatingWithPipeline.pkl')


def welcome():
    return "Welcome All"


def predict_RestaurentRating(Has_Table_booking, Has_Online_delivery, Price_range , Votes, Cuisines):
    prediction=regressor.predict(pd.DataFrame({'Has Table booking':[Has_Table_booking], 'Has Online delivery':[Has_Online_delivery],
                                             'Price range':[Price_range],'Votes':[Votes],'Cuisines':[Cuisines]}))
    print(prediction)
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
        result=predict_bmwcar(Has_Table_booking, Has_Online_delivery, Price_range , Votes, Cuisines)
    st.success('The Restaurent Rating is {} From 5'.format(result))
    if st.button("About"):
        st.text("our app using streamlit")
        st.text("best of luck in your GP")
if __name__=='__main__':
    main()        
