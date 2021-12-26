# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 02:53:25 2021

@author: HAlShekha


##############################################################################################################
##############################################################################################################
##############################################################################################################
#########################################  STEAMLIT  #########################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################



Tools & Developements

Streamlit oevrview:
https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/

How I Used Streamlit to Build a Web Application:
https://towardsdatascience.com/how-to-use-streamlit-to-create-web-applications-218af44064f5

How I Made a Website with Python and AWS
https://towardsdatascience.com/creating-a-website-to-host-your-python-web-application-f06f694a87e8



  Warning: to view this Streamlit app on a browser, run it with the following
  command:
      streamlit run  [ARGUMENTS] ==> [ARGUMENTS] = python file name in general
      

"""
################################## Bignner example for Streamlit  ########################################
# The formula of BMI Index when weight is in Kgs and height is in meters is:
#  BMI = W/h^2
    
# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('Welcome to BMI Calculator')
 
# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")
 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
     
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
         
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
     
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
         
else:
    # take height input in feet
    height = st.number_input('Feet')
     
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
 
# check if the button is pressed or not
if(st.button('Calculate BMI')):
     
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
     
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")