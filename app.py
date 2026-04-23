import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import wrds

st.set_page_config(page_title="WRDS Financial Data Analysis Tool", layout="wide")
st.title("Interactive Financial Data Analysis Tool")
st.caption("Dual Mode: WRDS Database Query + Local CSV Upload")

mode = st.radio("Select Data Source", ["Pull Data from WRDS Database", "Upload Local CSV File"], horizontal=True)

df = None

if mode == "Pull Data from WRDS Database":
    st.subheader("WRDS Database Connection")
    username = st.text_input("WRDS Username", type="default")
    password = st.text_input("WRDS Password", type="password")
 
    start_date = st.date_input("Start Date", value=None)
    end_date = st.date_input("End Date", value=None)
    permno = st.text_input("Stock PERMNO Code", value="")

    if st.button("Connect to WRDS and Pull Data"):
        try:
            db = wrds.Connection(wrds_username=username, wrds_password=password)
            st.success("WRDS database connected successfully!")

            query = f"""
                SELECT permno, date, prc, ret, vol, shrout
                FROM crsp.dsf
                WHERE permno = {permno}
                  AND date BETWEEN '{start_date}' AND '{end_date}'
                LIMIT 10000
            """
            df = db.raw_sql(query)
            db.close()

            st.session_state["df"] = df
            st.success(f"Successfully pulled data for PERMNO={permno}!")

        except Exception as e:
            st.error(f"Connection / Query Failed: {str(e)}")
            st.info("Please check your WRDS credentials, network access, and institutional VPN connection.")

    if "df" in st.session_state:
        df = st.session_state["df"]

else:
    st.subheader("Local CSV File Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df

if df is not None:
    st.subheader("Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Basic Data Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Rows", df.shape[0])
        st.metric("Total Columns", df.shape[1])
    with col2:
        st.metric("Total Missing Values", df.isnull().sum().sum())
        st.metric("Numeric Columns", len(df.select_dtypes(include=['float64', 'int64']).columns))

    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("Interactive Chart Generator")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 2:
        col_x, col_y = st.columns(2)
        with col_x:
            x_axis = st.selectbox("Select X-axis variable", numeric_cols)
        with col_y:
            y_axis = st.selectbox("Select Y-axis variable", numeric_cols)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df[x_axis], df[y_axis], alpha=0.6, color="#1f77b4")
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Scatter Plot of {x_axis} vs {y_axis}", fontsize=14)
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    st.success("Data analysis completed! You can switch variables or change data sources freely.")