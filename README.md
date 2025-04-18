# 📊 Trading Dashboard (Streamlit)

This is a Streamlit-based dashboard to visualize and analyze the performance of a simulated trading strategy with risk-based rules, payout cycles, and equity management.

---

## 🚀 Features

- Equity curve chart (monthly)
- Trade-level breakdown by month
- Payout cycle summary
- Win/loss pie chart for any selected month
- Key performance metrics (trades, win rate)
- Sidebar filter by month

---

## 📁 Files Included

- `trading_dashboard_app.py` – Main dashboard app (Streamlit)
- `Strategy_Data_for_Dashboard.xlsx` – Excel file with:
  - Trade Data
  - Payout Cycle Summary
  - Equity Curve
- `requirements.txt` – Python libraries required to run the dashboard

---

## 🛠 How to Run Locally

```bash
pip install streamlit pandas matplotlib openpyxl
streamlit run trading_dashboard_app.py
```

---

## 🌐 Hosting with Streamlit Cloud

1. Create a [Streamlit Cloud](https://streamlit.io/cloud) account
2. Connect your GitHub
3. Deploy the app using:
   - **Repo:** `pranit70/trading-dashboard`
   - **Branch:** `main`
   - **Main file path:** `trading_dashboard_app.py`

---

## 📬 Questions?

If you need help customizing the dashboard or understanding the strategy logic, feel free to reach out!
