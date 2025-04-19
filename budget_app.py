# DEMO BUDGET APP
import streamlit as st

st.title("💰 Budget Tracker Mini App")
st.write("Nhập thu nhập và chi tiêu hàng tháng của bạn để xem bạn tiết kiệm được bao nhiêu.")

# Nhập dữ liệu
income = st.number_input("Thu nhập hàng tháng (VND)", min_value=0)
expenses = st.number_input("Chi tiêu hàng tháng (VND)", min_value=0)

# Tính toán
if st.button("Tính ngân sách"):
    savings = income - expenses
    st.subheader(f"💡 Bạn tiết kiệm được: {savings:,} VND/tháng")

    if savings < 0:
        st.error("⚠️ Bạn đang chi tiêu quá mức!")
    elif savings == 0:
        st.warning("Bạn tiêu hết toàn bộ thu nhập!")
    else:
        st.success("Tốt! Bạn đang có ngân sách dương.")
