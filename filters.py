import streamlit as st

def apply_filters(df):
    gender = st.sidebar.selectbox("Filter by Gender", ["All"] + sorted(df['Gender'].unique()))
    class_ = st.sidebar.selectbox("Filter by Class", ["All"] + sorted(df['Class'].unique()))

    if gender != "All":
        df = df[df['Gender'] == gender]
    if class_ != "All":
        df = df[df['Class'] == class_]

    return df
