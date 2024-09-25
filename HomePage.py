import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Health & Sleep Statistics", layout="wide")
st.title("Welcome to Health & Sleep Statistics 🌙")
df = pd.read_csv('Health_Sleep_Statistics.csv')
st.write("Original DataFrame:")
st.dataframe(df)


tab1, tab2, tab3 = st.tabs(['🏠 Welcome', '🔧 Handling the Data', '📊 Understanding the Data'])

with tab1:
    st.subheader('Exploring the Data Columns')
    st.code(df.columns.tolist())
    st.info('Check the data types using `df.info()` for better understanding.')
    st.code('df.info()')
    st.image('Image1.jpg')
    st.warning('Bedtime and Wake-up Time columns are in object format; consider converting them to datetime.')


with tab2:
    st.title("Data Handling 🛠️")
    st.write('We will convert BedTime & Wake-up Time to datetime format and calculate sleep duration.')

    st.code("""
    df['Bedtime'] = pd.to_datetime(df['Bedtime']).dt.time
    df['Wake-up Time'] = pd.to_datetime(df['Wake-up Time']).dt.time

    # Function to convert time to hours
    def time_to_hours(t):
        return t.hour + t.minute / 60 + t.second / 3600

    # Convert 'Bedtime' and 'Wake-up Time' to hours
    df['Bedtime_hours'] = df['Bedtime'].apply(time_to_hours)
    df['Wakeup_hours'] = df['Wake-up Time'].apply(time_to_hours)

    # Calculate sleep time in hours
    df['Sleep_time'] = df['Wakeup_hours'] - df['Bedtime_hours']

    # Adjust for cases where sleep time is negative
    df.loc[df['Sleep_time'] < 0, 'Sleep_time'] += 24
    """)

    # Process the DataFrame
    df['Bedtime'] = pd.to_datetime(df['Bedtime']).dt.time
    df['Wake-up Time'] = pd.to_datetime(df['Wake-up Time']).dt.time

    def time_to_hours(t):
        return t.hour + t.minute / 60 + t.second / 3600

    df['Bedtime_hours'] = df['Bedtime'].apply(time_to_hours)
    df['Wakeup_hours'] = df['Wake-up Time'].apply(time_to_hours)
    df['Sleep_time'] = df['Wakeup_hours'] - df['Bedtime_hours']
    df.loc[df['Sleep_time'] < 0, 'Sleep_time'] += 24

    # Display the modified DataFrame
    st.write("Processed DataFrame with Sleep Time:")
    st.dataframe(df.head())
    st.warning('''
    We can remove the BedTime, Wake-up Time, and User ID from the dataset, as they won't contribute to our analysis.
    ''')
    st.code("df.drop({'Bedtime', 'Wake-up Time', 'User ID'}, axis=1, inplace=True)")
    df.drop(['Bedtime', 'Wake-up Time', 'User ID'], axis=1, inplace=True)
    st.dataframe(df.head())

with tab3:
    st.header("Understanding the Data 🔍")
    st.write("Let's start with the numeric columns:")
    st.code(df.describe())
    cat_colu = list(df.select_dtypes(include='O').columns)
    cat_choic = st.selectbox(label='Choose Catigorical The column you want to understand', options=cat_colu)
    if cat_choic:
        st.write(f'The number of unique values in "{cat_choic}" is: {df[cat_choic].nunique()}')
        st.write(f'The unique values in "{cat_choic}" are: {df[cat_choic].unique()}')
        st.write(f'The count of unique values in "{cat_choic}" is:')
        st.write(df[cat_choic].value_counts())
        
        if st.checkbox("Show Sleep Time Distribution"):
            plt.figure(figsize=(10, 5))
            sns.histplot(df['Sleep_time'], bins=30, kde=True)
            plt.title('Distribution of Sleep Time (Hours)')
            plt.xlabel('Sleep Time (Hours)')
            plt.ylabel('Frequency')
            st.pyplot(plt)

st.sidebar.header("Settings")
st.sidebar.text("Adjust your preferences here!")


