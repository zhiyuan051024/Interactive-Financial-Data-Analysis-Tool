# Interactive-Financial-Data-Analysis-Tool
# Problem & User (1–2 sentences)
This tool delivers an intuitive, code-free interactive interface for finance students and academic researchers to access, explore, and visualize professional US stock market data. It solves the barrier of complex SQL and Python coding for exploratory financial data analysis, supporting both WRDS academic database and local CSV file inputs.
# Data (source + access date + key fields)
Primary Data Source: CRSP (Center for Research in Security Prices) Daily Stock File (dsf) via Wharton Research Data Services (WRDS)
Secondary Data Support: User-uploaded local CSV files for custom dataset analysis
Access Date: Real-time data access as of April 2026, with flexible user-defined date range filtering
Key Core Fields:
permno: Permanent unique identifier for US stocks
date: Daily trading date
prc: Closing price of the stock
ret: Daily total return of the stock
vol: Daily trading volume
shrout: Shares outstanding for the stock
# Methods (main Python steps)
Built interactive web interface and user workflow using the Streamlit framework, with dual data source mode selection
Integrated WRDS Python API to establish secure database connections, with dynamic SQL query generation for flexible stock and date filtering
Leveraged Pandas for data cleaning, preprocessing, and automated descriptive statistical analysis of the pulled/uploaded dataset
Implemented customizable data visualization with Matplotlib, enabling users to select X/Y axis variables for scatter plot generation
Used Streamlit session state to cache loaded data, avoiding repeated database queries and improving user experience
# Key Findings (3–5 bullets)
The tool enables one-click access to professional WRDS financial data, eliminating the need for manual SQL coding for basic exploratory analysis
The dual-mode design ensures consistent functionality: WRDS mode for academic financial data, and CSV mode for universal custom dataset analysis
The flexible filter system (supporting blank inputs for no filtering) adapts to diverse analysis needs, from single-stock deep dive to full-market data exploration
Automated statistics and visualization reduce the technical barrier for non-technical users to complete end-to-end financial data analysis in minutes
# How to run (optional but valuable)
Local Environment Setup
Clone or download the full repository to your local device
Open your terminal/Anaconda Prompt, and navigate to the project root folder
Install all required dependencies with the command:pip install -r requirements.txt
Launch the Streamlit application with the command:streamlit run app.py
Access the tool via your browser at the automatically generated local URL (default: http://localhost:8501)
Prerequisite for WRDS Mode
A valid WRDS account with CRSP database access permissions
Connection to your university's institutional VPN (required for off-campus WRDS access)
