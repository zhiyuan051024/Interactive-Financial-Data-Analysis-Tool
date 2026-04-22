# Interactive-Financial-Data-Analysis-Tool
# 1. Problem & User
This interactive tool provides a code-free interface for finance students and academic researchers to quickly access, analyze, and visualize U.S. stock market data. It lowers the technical barrier for financial data exploration by supporting both professional WRDS database queries and local CSV file analysis.
# 2. Data
Source: CRSP Daily Stock File (dsf) via WRDS (Wharton Research Data Services); local CSV upload supported
Access Date: Real-time data query (April 2026)
Key Fields: permno (stock ID), date (trading date), prc (price), ret (return), vol (volume), shrout (shares outstanding)
Sample Data: Small stock dataset stored in /data/sample_stock_data.csv
# 3. Methods
Built interactive web application using Streamlit
Connected to WRDS database with dynamic SQL query (supports blank filters)
Data processing & statistics with Pandas
Custom scatter plot visualization with Matplotlib
Dual-mode support: WRDS data pull + local CSV analysis
# 4. Key Findings
The tool enables one-click professional financial data access without manual SQL coding
Blank-input friendly filters support flexible stock/date queries
Automated statistics and visualization complete end-to-end analysis in seconds
Dual-mode design ensures stable demonstration both online and offline
# 5. How to Run
Local Execution
Install dependencies:
pip install -r requirements.txt
Launch the app:
streamlit run app.py
Open in browser: http://localhost:8501
WRDS Mode Requirements
Valid WRDS account
University institutional VPN connection
# 6. Product Link / Demo
Live App: [YOUR STREAMLIT CLOUD LINK]
GitHub Repo: [YOUR GITHUB LINK]
Demo Video: [YOUR VIDEO LINK]
# 7. Limitations & Next Steps
Limitations
Only scatter plot visualization supported
Data limited to 10,000 rows for performance
WRDS access requires institutional account & VPN
Next Steps
Add time-series charts & financial indicators
Integrate Compustat financial data
Support data export to CSV/Excel
Optimize large-data query performance
