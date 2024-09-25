import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.header('📝 Input Your Data for Analysis')
st.markdown("Please fill in the following details to help us analyze your health and sleep statistics:")

age = st.slider(label='Enter Your Age', min_value=22, max_value=55)

col_1, col_2, col_3 = st.columns(3)
with col_1:
    gender = st.radio(label='choose your Gender', options=['male','female'])
with col_3:    
    activity_level = st.radio(label='choose your Physical Activty', options=['low','medium','high'])

dietary_habits = st.selectbox(label='Choose Your Dietary Habits', options=['Healthy', 'Unhealthy', 'Medium'])

st.markdown("---")  

# Sleep and Health-related inputs
col_1, col_2, col_3 = st.columns(3)
with col_1:
    sleep_disorder = st.radio(label='Do You Suffer from Sleep Disorders?', options=['Yes', 'No'])
with col_3:
    medication_usage = st.radio(label='Do You Use Any Medication?', options=['Yes', 'No'])
sleep_duration = st.number_input("Enter Your Sleep Duration (in Hours)", min_value=4.0, max_value=9.0, step=0.1)
steps_today = st.slider(label='Enter The Amount of Steps You Took Today', min_value=3000, max_value=11000)

st.markdown("---")  

is_submit = st.button('Submit Data for Analysis')
if is_submit == True:
    st.success("Thank you for your input! Your data will be analyzed.")
    # Summary of inputs
    st.subheader("Summary of Your Inputs")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Physical Activity Level:** {activity_level}")
    st.write(f"**Dietary Habits:** {dietary_habits}")
    st.write(f"**Sleep Disorders:** {sleep_disorder}")
    st.write(f"**Medication Usage:** {medication_usage}")
    st.write(f"**Sleep Duration:** {sleep_duration} hours")
    st.write(f"**Steps Taken Today:** {steps_today}")

