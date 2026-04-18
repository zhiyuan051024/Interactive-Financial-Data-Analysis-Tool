import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import wrds

st.set_page_config(page_title="WRDS金融数据分析工具", layout="wide")
st.title("📊 交互式金融数据分析工具")
st.caption("支持WRDS专业数据库拉取 + 本地CSV文件上传双模式")

mode = st.radio("选择数据来源", ["从WRDS数据库拉取数据", "本地上传CSV文件"], horizontal=True)

df = None

if mode == "从WRDS数据库拉取数据":
    st.subheader("🔐 WRDS数据库连接")
    username = st.text_input("WRDS用户名", type="default")
    password = st.text_input("WRDS密码", type="password")
 
    start_date = st.date_input("开始日期", value=None)
    end_date = st.date_input("结束日期", value=None)
    permno = st.text_input("股票PERMNO代码", value="")

    if st.button("连接WRDS并拉取数据"):
        try:
            db = wrds.Connection(wrds_username=username, wrds_password=password)
            st.success("✅ WRDS数据库连接成功！")

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
            st.success(f"✅ 成功拉取 PERMNO={permno} 的数据！")

        except Exception as e:
            st.error(f"连接/拉取失败：{str(e)}")
            st.info("请检查你的WRDS账号密码、网络权限，以及机构VPN是否已连接")

    if "df" in st.session_state:
        df = st.session_state["df"]

else:
    st.subheader("📁 本地CSV文件上传")
    uploaded_file = st.file_uploader("请上传 CSV 文件", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df

if df is not None:
    st.subheader("🔍 数据预览")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("📈 数据基本统计信息")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("数据总行数", df.shape[0])
        st.metric("数据总列数", df.shape[1])
    with col2:
        st.metric("缺失值总数", df.isnull().sum().sum())
        st.metric("数值型列数量", len(df.select_dtypes(include=['float64', 'int64']).columns))

    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("📊 交互式图表生成")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 2:
        col_x, col_y = st.columns(2)
        with col_x:
            x_axis = st.selectbox("选择X轴字段", numeric_cols)
        with col_y:
            y_axis = st.selectbox("选择Y轴字段", numeric_cols)

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df[x_axis], df[y_axis], alpha=0.6, color="#1f77b4")
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"{x_axis} 与 {y_axis} 散点分布", fontsize=14)
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    st.success("✅ 数据分析完成！你可以自由切换字段、更换数据来源")