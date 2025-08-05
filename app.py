import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import io

from data_loader import load_data
from analytics import calculate_scores, get_top_students
from filters import apply_filters
from visualizations import show_summary, show_top_table, show_gender_pie, show_heatmap

# Load authentication config
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name} 👋")

    st.set_page_config(page_title="Student Dashboard", layout="wide")
    st.title("📚 Student Performance Dashboard")

    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if uploaded_file:
        df = load_data(uploaded_file)
        df = calculate_scores(df)
        filtered_df = apply_filters(df)

        show_summary(filtered_df)
        show_top_table(filtered_df)
        show_gender_pie(filtered_df)
        show_heatmap(filtered_df)

        # Export filtered data
        st.subheader("📥 Download Filtered Data")
        buffer = io.BytesIO()
        filtered_df.to_excel(buffer, index=False)
        st.download_button(
            label="Download Filtered Data as Excel",
            data=buffer,
            file_name="filtered_students.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Export top performers
        st.subheader("📥 Download Top Performers")
        top_df = get_top_students(filtered_df)
        buffer_top = io.BytesIO()
        top_df.to_excel(buffer_top, index=False)
        st.download_button(
            label="Download Top Performers as Excel",
            data=buffer_top,
            file_name="top_students.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

elif authentication_status is False:
    st.error("Username or password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")


# import streamlit as st
# from data_loader import load_data
# from analytics import calculate_scores
# from filters import apply_filters
# from visualizations import show_summary, show_top_table

# st.set_page_config(page_title="Student Dashboard", layout="wide")
# st.title("📚 Student Performance Dashboard")

# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])
# if uploaded_file:
#     df = load_data(uploaded_file)
#     df = calculate_scores(df)
#     filtered_df = apply_filters(df)

#     show_summary(filtered_df)
#     show_top_table(filtered_df)
