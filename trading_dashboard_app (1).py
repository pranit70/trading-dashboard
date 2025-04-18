
# Streamlit Dashboard for Trading Strategy
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    trade_data = pd.read_excel("Strategy_Data_for_Dashboard.xlsx", sheet_name="Trade Data")
    cycle_data = pd.read_excel("Strategy_Data_for_Dashboard.xlsx", sheet_name="Cycle Summary")
    equity_data = pd.read_excel("Strategy_Data_for_Dashboard.xlsx", sheet_name="Equity Curve")
    return trade_data, cycle_data, equity_data

trade_data, cycle_data, equity_data = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_month = st.sidebar.selectbox("Select Month", sorted(trade_data['Month'].unique()), index=0)
filtered_trades = trade_data[trade_data['Month'] == selected_month]
filtered_cycles = cycle_data[cycle_data['Month'] == selected_month]

# Main Dashboard
st.title("📊 Trading Strategy Performance Dashboard")

# Equity Curve
st.subheader("Equity Curve")
fig, ax = plt.subplots()
ax.plot(equity_data["Month"], equity_data["Ending Equity"], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Ending Equity ($)")
ax.set_title("Equity Over Time")
ax.grid(True)
st.pyplot(fig)

# Cycle Payout Summary
st.subheader("Payout Cycle Summary (Selected Month)")
st.dataframe(filtered_cycles)

# Trade Results Breakdown
st.subheader("Trade Results (Selected Month)")
st.dataframe(filtered_trades)

# Win/Loss Pie Chart
st.subheader("Win vs Loss Distribution")
fig2, ax2 = plt.subplots()
trade_counts = filtered_trades['Result'].value_counts()
ax2.pie(trade_counts, labels=trade_counts.index, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
st.pyplot(fig2)

# KPIs
st.subheader("Key Metrics")
total_trades = len(filtered_trades)
win_rate = (trade_counts.get('Win', 0) / total_trades * 100) if total_trades > 0 else 0
st.metric("Total Trades", total_trades)
st.metric("Win Rate (%)", f"{win_rate:.2f}%")
