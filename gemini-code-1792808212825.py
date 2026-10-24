import streamlit as st

# --- ĐỊNH NGHĨA LỚP XỬ LÝ BACKEND ---
class AdvancedFinAIAnalyzer:
    def __init__(self, student_name, monthly_income):
        self.student_name = student_name
        self.income = float(monthly_income)
        self.transactions = []
        self.feedbacks = []
        self.historical_trend = [self.income * 0.8, self.income * 0.9]  # Dữ liệu giả lập 2 tháng trước

    def add_transaction(self, amount, category, description):
        self.transactions.append({
            "amount": float(amount),
            "category": category,
            "description": description
        })

    def collect_feedback(self, rating, comment):
        self.feedbacks.append({
            "rating": rating,
            "comment": comment
        })

    def analyze_deep_insights(self):
        if not self.income:
            return {"error": "Thu nhập không hợp lệ."}
            
        spending_breakdown = {}
        total_spent = 0
        
        for t in self.transactions:
            cat = t["category"]
            amt = t["amount"]
            total_spent += amt
            spending_breakdown[cat] = spending_breakdown.get(cat, 0) + amt

        spending_ratio = (total_spent / self.income) * 100 if self.income > 0 else 100
        savings = self.income - total_spent
        
        current_month_trend = self.historical_trend + [total_spent]

        warnings = []
        advice_list = []
        risk_score = 100

        # Phân tích rủi ro
        if total_spent > self.income:
            risk_score -= 45
            warnings.append({
                "type": "🚨 BẪY THÂM HỤT & VỠ NẠN TÀI CHÍNH",
                "detail": f"Chi tiêu ({total_spent:,.0f}đ) vượt thu nhập ({self.income:,.0f}đ). Bạn đang tiêu phạm vào tiền gốc hoặc phải vay mượn."
            })
            advice_list.append("💡 Lời khuyên cốt lõi: Lập tức kích hoạt chế độ 'Đóng băng mua sắm'. Cắt giảm 100% các khoản chi phí không thiết yếu trong vòng 2 tuần tới.")
        elif spending_ratio > 80:
            risk_score -= 25
            warnings.append({
                "type": "⚠️ BẪY CẠN KIỆT QUỸ DỰ PHÒNG",
                "detail": f"Tỷ lệ tiêu dùng chiếm tới {spending_ratio:.1f}% thu nhập. Không còn khoản dự phòng cho các tình huống khẩn cấp."
            })
            advice_list.append("💡 Lời khuyên cốt lõi: Áp dụng ngay quy tắc 50/30/20. Cố gắng đưa tỷ lệ tiêu dùng xuống dưới 50% ở tháng tiếp theo.")
        else:
            advice_list.append("💡 Lời khuyên cốt lõi: Quản lý dòng tiền tốt! Hãy chuyển số tiền tiết kiệm vào tài khoản riêng biệt.")

        # Kiểm tra bẫy hành vi online
        online_trap_total = spending_breakdown.get("Game/Giải trí", 0) + spending_breakdown.get("Mua sắm Online", 0)
        if self.income > 0 and (online_trap_total / self.income) > 0.3:
            risk_score -= 25
            warnings.append({
                "type": "🎯 BẪY TIÊU DÙNG SỐ / FOMO ONLINE",
                "detail": f"Chi phí Game và Săn sale chiếm {(online_trap_total/self.income)*100:.1f}% thu nhập."
            })
            advice_list.append("💡 Lời khuyên hành vi: Sử dụng quy tắc '24 giờ' trước khi thanh toán giỏ hàng online hoặc nạp game.")

        health_status = "Xuất sắc (Ổn định dài hạn)"
        if risk_score < 50:
            health_status = "🔴 Báo động đỏ (Nguy cơ rủi ro cao)"
        elif risk_score < 75:
            health_status = "🟡 Cần tái cấu trúc dòng tiền"
        elif risk_score < 90:
            health_status = "🟢 Khá ổn định, cần duy trì"

        return {
            "total_income": self.income,
            "total_spent": total_spent,
            "savings": savings,
            "spending_ratio": round(spending_ratio, 2),
            "health_score": max(0, risk_score),
            "health_status": health_status,
            "breakdown": spending_breakdown,
            "warnings": warnings,
            "advice": advice_list,
            "trend_data": current_month_trend
        }


# --- GIAO DIỆN WEB STREAMLIT ---
st.set_page_config(page_title="FinAI Simulator", page_icon="📊", layout="centered")

st.title("🚀 FinAI Simulator")
st.subheader("Hệ thống Phân tích & Đào tạo Tài chính Thông minh")
st.markdown("---")

# Nhập thông tin người dùng
name = st.text_input("Nhập tên học sinh / người trải nghiệm:", "Nguyễn Lan Anh")
income = st.number_input("Nhập tổng thu nhập / tiền tiêu vặt trong tháng (VNĐ):", min_value=0.0, value=25000000.0, step=500000.0)

# Khởi tạo Analyzer trong session_state để lưu dữ liệu khi bấm nút
if 'analyzer' not in st.session_state or st.session_state.get('current_name') != name or st.session_state.get('current_income') != income:
    st.session_state.analyzer = AdvancedFinAIAnalyzer(student_name=name, monthly_income=income)
    st.session_state.current_name = name
    st.session_state.current_income = income

st.markdown("### 📝 Nhập các khoản giao dịch chi tiêu")
with st.form("transaction_form", clear_on_submit=True):
    cat_choice = st.selectbox("Chọn danh mục chi tiêu:", ["Game/Giải trí", "Mua sắm Online", "Ăn uống", "Khác"])
    amount = st.number_input("Số tiền chi tiêu (VNĐ):", min_value=0.0, value=1000000.0, step=100000.0)
    desc = st.text_input("Mô tả chi tiết khoản chi:")
    
    submitted = st.form_submit_button("✅ Thêm giao dịch")
    if submitted:
        st.session_state.analyzer.add_transaction(amount, cat_choice, desc)
        st.success(f"Đã ghi nhận giao dịch: {cat_choice} - {amount:,.0f} VNĐ")

# Hiển thị danh sách giao dịch đã nhập
if st.session_state.analyzer.transactions:
    st.markdown("#### 📋 Danh sách giao dịch hiện tại:")
    for i, t in enumerate(st.session_state.analyzer.transactions, 1):
        st.text(f"{i}. [{t['category']}] {t['amount']:,.0f} VNĐ - {t['description']}")

st.markdown("---")

# Nút phân tích chuyên sâu
if st.button("📊 XUẤT BÁO CÁO PHÂN TÍCH TÀI CHÍNH CHUYÊN SÂU"):
    st.session_state.show_report = True

if st.session_state.get('show_report', False):
    report = st.session_state.analyzer.analyze_deep_insights()
    
    if "error" in report:
        st.error(report["error"])
    else:
        st.markdown(f"## 📊 KẾT QUẢ CHO: {name.upper()}")
        st.metric(label="Tổng thu nhập", value=f"{report['total_income']:,.0f} VNĐ")
        st.metric(label="Tổng chi tiêu", value=f"{report['total_spent']:,.0f} VNĐ", delta=f"{report['spending_ratio']}% thu nhập", delta_color="inverse")
        st.metric(label="Quỹ tích lũy", value=f"{report['savings']:,.0f} VNĐ")
        st.metric(label="Điểm sức khỏe tài chính", value=f"{report['health_score']}/100", delta=report['health_status'])
        
        st.markdown("### 📈 Môi trường giả lập: Xu hướng 3 tháng gần nhất")
        months = ["Tháng trước (T-2)", "Tháng trước (T-1)", "Tháng này (Hiện tại)"]
        chart_data = {m: val for m, val in zip(months, report['trend_data'])}
        st.bar_chart(chart_data)
        
        st.markdown("### 🧠 Nhận diện bẫy tài chính & Cảnh báo")
        if not report['warnings']:
            st.success("🎉 Tuyệt vời! Không phát hiện bẫy rủi ro tài chính nào.")
        else:
            for w in report['warnings']:
                st.warning(f"**{w['type']}**\n\n{w['detail']}")
                
        st.markdown("### 💡 Lời khuyên hành động từ chuyên gia AI")
        for adv in report['advice']:
            st.info(adv)
            
        st.markdown("---")
        st.markdown("### 📝 Góp ý & Đánh giá trải nghiệm phần mềm")
        rating = st.slider("Đánh giá độ hữu ích (1-5 sao):", 1, 5, 5)
        comment = st.text_area("Ý kiến đóng góp:")
        if st.button("Gửi đánh giá"):
            st.session_state.analyzer.collect_feedback(rating, comment)
            st.success("🙏 Cảm ơn bạn đã đóng góp! Ý kiến của bạn đã được ghi nhận để hệ thống ngày càng thông minh hơn.")