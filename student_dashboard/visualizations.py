import streamlit as st

def show_summary(df):
    st.subheader("📊 Subject-wise Averages")
    subjects = ['Punjabi', 'Hindi', 'English', 'Math', 'Science', 'Social Science']
    avg_scores = df[subjects].mean().round(2)
    st.bar_chart(avg_scores)

def show_top_table(df):
    from analytics import get_top_students
    st.subheader("🏆 Top Performers")
    top_df = get_top_students(df)
    st.dataframe(top_df[['Name', 'Class', 'Gender', 'Total', 'Percentage']])

def show_gender_pie(df):
    import plotly.express as px
    gender_counts = df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig = px.pie(gender_counts, names='Gender', values='Count', title='Gender Distribution')
    st.plotly_chart(fig)

def show_heatmap(df):
    import seaborn as sns
    import matplotlib.pyplot as plt

    st.subheader("📊 Subject Score Correlation")
    subjects = ['Punjabi', 'Hindi', 'English', 'Math', 'Science', 'Social Science']
    corr = df[subjects].corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)


# import streamlit as st

# def show_summary(df):
#     st.subheader("📊 Subject-wise Averages")
#     subjects = ['Punjabi', 'Hindi', 'English', 'Math', 'Science', 'Social Science']
#     avg_scores = df[subjects].mean().round(2)
#     st.bar_chart(avg_scores)

# def show_top_table(df):
#     from analytics import get_top_students
#     st.subheader("🏆 Top Performers")
#     top_df = get_top_students(df)
#     st.dataframe(top_df[['Name', 'Class', 'Gender', 'Total', 'Percentage']])

