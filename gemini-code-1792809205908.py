import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(
    page_title="FinAI Simulator - KHKT 2026",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS TÙY CHỈNH MÀU SẮC & PHONG CÁCH TAY LÁI TRẺ ---
st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 800;
        text-align: center;
        font-size: 2.5rem;
    }
    .sub-title {
        color: #3B82F6;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 25px;
    }
    .stButton>button {
        border-radius: 12px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .author-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #3B82F6;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LỚP XỬ LÝ NGHỆ THUẬT & LOGIC ANALYZER ---
class AdvancedFinAIAnalyzer:
    def __init__(self, student_name, monthly_income):
        self.student_name = student_name
        self.income = float(monthly_income)
        self.transactions = []
        self.feedbacks = []
        self.historical_trend = [self.income * 0.75, self.income * 0.85]

    def add_transaction(self, amount, category, description):
        self.transactions.append({
            "amount": float(amount),
            "category": category,
            "description": description
        })

    def collect_feedback(self, rating, comment):
        self.feedbacks.append({"rating": rating, "comment": comment})

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

        if total_spent > self.income:
            risk_score -= 45
            warnings.append({
                "type": "🚨 BẪY THÂM HỤT & VỠ QUỸ TÀI CHÍNH",
                "detail": f"Chi tiêu ({total_spent:,.0f}đ) vượt quá thu nhập ({self.income:,.0f}đ). Bạn đang chạm vào khoản tiết kiệm hoặc phải vay mượn."
            })
            advice_list.append("💡 Lời khuyên: Kích hoạt chế độ 'Đóng băng chi tiêu'! Cắt giảm 100% các khoản không thiết yếu.")
        elif spending_ratio > 80:
            risk_score -= 25
            warnings.append({
                "type": "⚠️ BẪY CẠN KIỆT QUỸ DỰ PHÒNG",
                "detail": f"Tỷ lệ tiêu dùng chiếm {spending_ratio:.1f}% thu nhập, hạn chế khả năng tích lũy khẩn cấp."
            })
            advice_list.append("💡 Lời khuyên: Áp dụng quy tắc 50/30/20 để đưa mức chi tiêu về dưới 50% thu nhập.")
        else:
            advice_list.append("💡 Lời khuyên: Quản lý dòng tiền tuyệt vời! Hãy duy trì gửi tiết kiệm số tiền thặng dư.")

        online_trap_total = spending_breakdown.get("Game/Giải trí", 0) + spending_breakdown.get("Mua sắm Online", 0)
        if self.income > 0 and (online_trap_total / self.income) > 0.3:
            risk_score -= 25
            warnings.append({
                "type": "🎯 BẪY TIÊU DÙNG SỐ / FOMO MUA SẮM",
                "detail": f"Chi phí Game và Săn sale chiếm tới {(online_trap_total/self.income)*100:.1f}% tổng thu nhập."
            })
            advice_list.append("💡 Lời khuyên: Thực hiện quy tắc trì hoãn '24 Giờ' trước khi chốt đơn mua hàng online.")

        health_status = "🟢 Tốt - Tự chủ tài chính"
        if risk_score < 50:
            health_status = "🔴 Báo động đỏ - Cần điều chỉnh khẩn cấp"
        elif risk_score < 75:
            health_status = "🟡 Trung bình - Cần tái cấu trúc dòng tiền"

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

# --- THUẬT TOÁN HIỆU ỨNG CHỜ NGẪU NHIÊN ---
def trigger_random_loading():
    mascots = [
        ("🦊 Con Cáo Cần Mẫn", "Đang tính toán các khoản chi tiêu... 🪙💸"),
        ("🐰 Con Thỏ Siêu Trí Tuệ", "Đang phân tích bẫy tài chính FOMO... 🍕🥤"),
        ("🐻 Chú Hổ Tài Chính", "Đang giả lập biểu đồ 3 tháng... 📈📉"),
        ("🐱 Mèo Thần Tài", "Đang đếm số tiền tiết kiệm của bạn... 💵✨")
    ]
    mascot, text = random.choice(mascots)
    with st.spinner(f"{mascot}: {text}"):
        time.sleep(1.2)

# --- KHỞI TẠO ĐIỀU HƯỚNG TRANG (NAVIGATION) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2953/2953361.png", width=80)
st.sidebar.title("📌 Danh Mục Dự Án")
page = st.sidebar.radio(
    "Chuyển trang:",
    [
        "1. Chào Mừng & Hướng Dẫn",
        "2. Trạm Phân Tích Tài Chính",
        "3. Đào Tạo & Chơi Thử Chứng Khoán",
        "4. Lời Cảm Ơn & Tác Giả"
    ]
)

# ==========================================
# TRANG 1: CHÀO MỪNG & HƯỚNG DẪN
# ==========================================
if page == "1. Chào Mừng & Hướng Dẫn":
    st.markdown("<h1 class='main-title'>🚀 CHÀO MỪNG BẠN ĐẾN VỚI FINAI SIMULATOR!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Hệ thống Phân tích & Đào tạo Quản lý Tài chính Thông minh dành cho Học sinh</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://img.freepik.com/free-vector/happy-students-concept-illustration_114360-8276.jpg", use_container_width=True)
    
    with col2:
        st.markdown("### 👋 Xin chào những nhà quản lý tài chính tương lai!")
        st.write("""
        Bạn có bao giờ thắc mắc số tiền tiêu vặt hay tiền mừng tuổi của mình đã 'bay biến' đi đâu mất?
        Đừng lo lắng! **FinAI Simulator** ra đời để giúp bạn làm chủ dòng tiền, tránh bẫy tiêu dùng số và xây dựng tư duy tài chính vững chắc.
        """)
        
        st.info("""
        🎯 **3 Bước Trải Nghiệm Nhanh:**
        1. **Bước 1:** Chuyển sang **Trạm Phân Tích** để nhập thu nhập và danh sách chi tiêu.
        2. **Bước 2:** Nhận ngay Báo cáo Sức khỏe Tài chính & Cảnh báo bẫy tài chính từ AI.
        3. **Bước 3:** Thử sức đầu tư chứng khoán lịch sử & Học mẹo quản lý tiền đỉnh cao tại **Trang Đào Tạo**.
        """)
        st.success("👉 Hãy chọn trang số **'2. Trạm Phân Tích Tài Chính'** ở thanh menu bên trái để bắt đầu ngay nào!")

# ==========================================
# TRANG 2: TRẠM PHÂN TÍCH TÀI CHÍNH
# ==========================================
elif page == "2. Trạm Phân Tích Tài Chính":
    st.markdown("<h2 class='main-title'>📊 TRẠM PHÂN TÍCH TÀI CHÍNH CỦA BẠN</h2>", unsafe_allow_html=True)
    st.markdown("---")

    name = st.text_input("👤 Nhập tên học sinh / người trải nghiệm:", "Nguyễn Lan Anh")
    income = st.number_input("💵 Nhập tổng thu nhập / tiền tiêu vặt trong tháng (VNĐ):", min_value=0.0, value=2500000.0, step=100000.0)

    if 'analyzer' not in st.session_state or st.session_state.get('current_name') != name or st.session_state.get('current_income') != income:
        st.session_state.analyzer = AdvancedFinAIAnalyzer(student_name=name, monthly_income=income)
        st.session_state.current_name = name
        st.session_state.current_income = income

    st.markdown("### 📝 Nhập các khoản chi tiêu của bạn")
    with st.form("transaction_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        with col_a:
            cat_choice = st.selectbox("Chọn danh mục:", ["Game/Giải trí", "Mua sắm Online", "Ăn uống", "Học tập", "Khác"])
            amount = st.number_input("Số tiền chi (VNĐ):", min_value=0.0, value=100000.0, step=50000.0)
        with col_b:
            desc = st.text_input("Mô tả chi tiết (ví dụ: Nạp game, Mua trà sữa...):")
        
        submitted = st.form_submit_button("✅ Thêm khoản chi")
        if submitted:
            trigger_random_loading()
            st.session_state.analyzer.add_transaction(amount, cat_choice, desc)
            st.success(f"Đã lưu: {cat_choice} - {amount:,.0f} VNĐ")

    if st.session_state.analyzer.transactions:
        st.markdown("#### 📋 Danh sách chi tiêu đã ghi nhận:")
        for i, t in enumerate(st.session_state.analyzer.transactions, 1):
            st.write(f"**{i}.** [{t['category']}] {t['amount']:,.0f} VNĐ - *{t['description']}*")

    st.markdown("---")
    if st.button("🔥 XUẤT BÁO CÁO PHÂN TÍCH & CẢNH BÁO AI", type="primary", use_container_width=True):
        trigger_random_loading()
        st.session_state.show_report = True

    if st.session_state.get('show_report', False):
        report = st.session_state.analyzer.analyze_deep_insights()
        
        if "error" in report:
            st.error(report["error"])
        else:
            st.markdown(f"### 🎯 BÁO CÁO TÀI CHÍNH DÀNH CHO: **{name.upper()}**")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Thu Nhập", f"{report['total_income']:,.0f}đ")
            c2.metric("Chi Tiêu", f"{report['total_spent']:,.0f}đ", delta=f"{report['spending_ratio']}%", delta_color="inverse")
            c3.metric("Tích Lũy", f"{report['savings']:,.0f}đ")
            c4.metric("Điểm Sức Khỏe", f"{report['health_score']}/100", delta=report['health_status'])

            st.markdown("#### 📈 Giả lập Xu hướng Dòng tiền 3 Tháng")
            months = ["Tháng trước (T-2)", "Tháng trước (T-1)", "Tháng này"]
            chart_data = {m: val for m, val in zip(months, report['trend_data'])}
            st.bar_chart(chart_data)

            st.markdown("#### 🧠 Cảnh Báo Bẫy Tài Chính AI")
            if not report['warnings']:
                st.success("🎉 Tuyệt vời! Bạn không vướng phải bẫy rủi ro tài chính nào.")
            else:
                for w in report['warnings']:
                    st.warning(f"**{w['type']}**\n\n{w['detail']}")

            st.markdown("#### 💡 Lời Khuyên Hành Động")
            for adv in report['advice']:
                st.info(adv)

            st.markdown("---")
            st.markdown("#### 💬 Góp ý & Đánh giá trải nghiệm")
            rating = st.slider("Đánh giá độ hài lòng (1-5 sao):", 1, 5, 5)
            comment = st.text_area("Ý kiến đóng góp của bạn:")
            if st.button("📤 Gửi Đánh Giá"):
                st.session_state.analyzer.collect_feedback(rating, comment)
                st.balloons()
                st.success("🙏 Cảm ơn bạn đã đóng góp! Ý kiến của bạn đã được ghi nhận để hệ thống ngày càng thông minh hơn.")

# ==========================================
# TRANG 3: ĐÀO TẠO & CHƠI THỬ CHỨNG KHOÁN
# ==========================================
elif page == "3. Đào Tạo & Chơi Thử Chứng Khoán":
    st.markdown("<h2 class='main-title'>📈 ĐÀO TẠO & GIẢ LẬP ĐẦU TƯ CHỨNG KHOÁN</h2>", unsafe_allow_html=True)
    st.markdown("---")

    tab1, tab2 = st.columns(2)

    with tab1:
        st.markdown("### 🎮 Chơi Thử Chứng Khoán Lịch Sử")
        st.caption("Thực hành mua/bán cổ phiếu mô phỏng biến động thực tế!")
        
        stock_choice = st.selectbox("Chọn cổ phiếu mô phỏng:", ["VNM (Vinamilk - Tiêu dùng)", "FPT (Công nghệ)", "HPG (Hòa Phát - Thép)"])
        cash = st.number_input("Số vốn giả lập (VNĐ):", value=10000000.0, step=1000000.0)
        buy_amount = st.slider("Phần trăm vốn dùng để mua cổ phiếu (%):", 10, 100, 50)
        
        if st.button("🚀 Thực hiện mô phỏng đợt đầu tư"):
            trigger_random_loading()
            change = random.choice([-15, -8, 5, 12, 25])
            profit = (cash * (buy_amount/100)) * (change/100)
            final_cash = cash + profit
            
            st.markdown(f"**Kết quả đợt mô phỏng:** Cổ phiếu **{stock_choice.split()[0]}** biến động **{change:+d}%**")
            if profit >= 0:
                st.success(f"🎉 Bạn đã CÓ LÃI: **+{profit:,.0f} VNĐ**! Tổng số vốn hiện tại: **{final_cash:,.0f} VNĐ**.")
            else:
                st.error(f"📉 Bạn bị THUA LỖ: **{profit:,.0f} VNĐ**! Tổng số vốn còn lại: **{final_cash:,.0f} VNĐ**.")
            st.caption("Bài học: Đầu tư luôn đi kèm rủi ro. Chỉ dùng tiền nhàn rỗi để đầu tư!")

    with tab2:
        st.markdown("### 📚 Phương Pháp Quản Lý Tiền Kinh Điển")
        
        with st.expander("⭐ 1. Quy tắc 50/30/20"):
            st.write("- **50% Thu nhập:** Cho Nhu cầu thiết yếu (Ăn uống, học tập).")
            st.write("- **30% Thu nhập:** Cho Sở thích cá nhân (Giải trí, mua sắm).")
            st.write("- **20% Thu nhập:** Dành cho Tiết kiệm & Tích lũy.")

        with st.expander("🍯 2. Phương pháp 6 Hũ Tài Chính"):
            st.write("Chia thu nhập thành 6 phần: Thiết yếu (55%), Tích lũy (10%), Giáo dục (10%), Hưởng thụ (10%), Đầu tư (10%), Cho đi (5%).")

        with st.expander("⏳ 3. Quy tắc Kiềm chế 24 Giờ"):
            st.write("Khi muốn mua một món đồ không quá cần thiết, hãy đợi đúng 24 giờ. Nếu sau 24h bạn vẫn thấy cần, hãy quyết định mua!")

# ==========================================
# TRANG 4: LỜI CẢM ƠN & TÁC GIẢ
# ==========================================
elif page == "4. Lời Cảm Ơn & Tác Giả":
    st.markdown("<h2 class='main-title'>💖 LỜI CẢM ƠN & THÔNG TIN DỰ ÁN</h2>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("""
    ### 🙏 Lời Cảm Ơn Chân Thành
    Nhóm tác giả xin gửi lời cảm ơn sâu sắc nhất tới **Ban Giám khảo**, quý Thầy Cô giáo hướng dẫn cùng toàn thể các bạn học sinh đã trải nghiệm và đóng góp ý kiến quý báu cho phần mềm **FinAI Simulator**. 
    
    Sự ủng hộ của mọi người chính là động lực lớn nhất để nhóm tiếp tục phát triển phần mềm ngày càng thông minh và hữu ích hơn!
    """)

    st.markdown("<div class='author-card'>", unsafe_allow_html=True)
    st.markdown("### 👥 NHÓM TÁC GIẢ THỰC HIỆN DỰ ÁN")
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("🌐 **Tác giả 1:** Nguyễn Lan Anh")
        st.markdown("🏫 **Đơn vị:** Học sinh Trung học")
    with col_y:
        st.markdown("🌐 **Tác giả 2 & Đồng đội:** (Nhập tên đồng đội của bạn ở đây)")
        st.markdown("🏫 **Giáo viên hướng dẫn:** (Nhập tên GVHD ở đây)")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: center; color: #1E3A8A;'>"
        "🏆 SẢN PHẨM NGHIÊN CỨU THAM DỰ CUỘC THI KHOA HỌC KỸ THUẬT (KHKT) DÀNH CHO HỌC SINH TRUNG HỌC"
        "</h4>",
        unsafe_allow_html=True
    )