import time

class AdvancedFinAIAnalyzer:
    def __init__(self, student_name, monthly_income):
        self.student_name = student_name
        self.income = float(monthly_income)
        self.transactions = []
        self.feedback = {}
        self.historical_trend = [self.income * 0.8, self.income * 0.9]  # Dữ liệu giả lập 2 tháng trước để tạo xu hướng

    def add_transaction(self, amount, category, description):
        self.transactions.append({
            "amount": float(amount),
            "category": category,
            "description": description
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
        
        # Cập nhật xu hướng dòng tiền tháng này vào lịch sử
        current_month_trend = self.historical_trend + [total_spent]

        warnings = []
        advice_list = []
        risk_score = 100

        # --- 1. PHÂN TÍCH RỦI RO & ĐƯA RA LỜI KHUYÊN KĨ CÀNG ---
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
                "detail": f"Tỷ lệ tiêu dùng chiếm tới {spending_ratio:.1f}% thu nhập. Không còn khoản dự phòng cho các tình huống khẩn cấp (ốm đau, học tập)."
            })
            advice_list.append("💡 Lời khuyên cốt lõi: Áp dụng ngay quy tắc 50/30/20. Cố gắng đưa tỷ lệ tiêu dùng xuống dưới 50% ở tháng tiếp theo.")
        else:
            advice_list.append("💡 Lời khuyên cốt lõi: Quản lý dòng tiền tốt! Hãy chuyển số tiền tiết kiệm vào một tài khoản riêng biệt để sinh lời hoặc dự phòng.")

        # Kiểm tra bẫy hành vi online (Game & Mua sắm)
        online_trap_total = spending_breakdown.get("Game/Giải trí", 0) + spending_breakdown.get("Mua sắm Online", 0)
        if self.income > 0 and (online_trap_total / self.income) > 0.3:
            risk_score -= 25
            warnings.append({
                "type": "🎯 BẪY TIÊU DÙNG SỐ / FOMO ONLINE",
                "detail": f"Chi phí Game và Săn sale chiếm {(online_trap_total/self.income)*100:.1f}% thu nhập. Đây là bẫy tâm lý phổ biến khiến học sinh mất kiểm soát tài chính."
            })
            advice_list.append("💡 Lời khuyên hành vi: Sử dụng quy tắc '24 giờ' trước khi thanh toán giỏ hàng online hoặc nạp game. Hãy chờ qua 24h xem bạn có thực sự cần nó không.")

        # Xếp loại sức khỏe tài chính
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

    def collect_feedback(self, rating, comment):
        """Thu thập góp ý từ học sinh sau khi trải nghiệm phần mềm"""
        self.feedback = {
            "rating": rating,
            "comment": comment
        }


# ==========================================
# CHƯƠNG TRÌNH CHẠY TƯƠNG TÁC CHUYÊN SÂU
# ==========================================
if __name__ == "__main__":
    print("==================================================")
    print("   FINAI SIMULATOR - HỆ THỐNG PHÂN TÍCH & ĐÀO TẠO TÀI CHÍNH")
    print("==================================================\n")
    
    name = input("Nhập tên học sinh/người trải nghiệm: ")
    
    while True:
        try:
            income = float(input("Nhập tổng thu nhập/tiền tiêu vặt trong tháng (VNĐ): "))
            if income < 0:
                print("Thu nhập không được âm!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập định dạng số hợp lệ!")

    app = AdvancedFinAIAnalyzer(student_name=name, monthly_income=income)
    
    print("\n--- NHẬP CÁC KHOẢN GIAO DỊCH CHI TIÊU ---")
    print("Hướng dẫn: Chọn danh mục từ 1 đến 4. Nhập 'q' để kết thúc và xem phân tích.")
    
    while True:
        cat_choice = input("\nChọn danh mục (1: Game/Giải trí, 2: Mua sắm Online, 3: Ăn uống, 4: Khác) [Nhập q]: ").strip()
        if cat_choice.lower() == 'q':
            break
            
        if cat_choice not in ["1", "2", "3", "4"]:
            print("⚠️ Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")
            continue
            
        cat_map = {"1": "Game/Giải trí", "2": "Mua sắm Online", "3": "Ăn uống", "4": "Khác"}
        selected_category = cat_map[cat_choice]
        
        try:
            amount = float(input("Nhập số tiền chi tiêu (VNĐ): ").strip())
            if amount < 0:
                print("Số tiền không thể âm!")
                continue
        except ValueError:
            print("⚠️ Lỗi: Số tiền phải là dạng số!")
            continue
            
        desc = input("Mô tả chi tiết khoản chi: ")
        app.add_transaction(amount, selected_category, desc)
        print("✅ Đã ghi nhận giao dịch thành công.")

    # --- XUẤT BÁO CÁO PHÂN TÍCH CHUYÊN SÂU ---
    report = app.analyze_deep_insights()
    
    print("\n" + "="*50)
    print(f" 📊 BẢO CÁO PHÂN TÍCH TÀI CHÍNH CHUYÊN SÂU CHO: {name.upper()}")
    print("="*50)
    print(f"💰 Tổng thu nhập    : {report['total_income']:,.0f} VNĐ")
    print(f"💸 Tổng chi tiêu    : {report['total_spent']:,.0f} VNĐ ({report['spending_ratio']}% thu nhập)")
    print(f"🏦 Quỹ tích lũy     : {report['savings']:,.0f} VNĐ")
    print(f"🎯 Điểm sức khỏe    : {report['health_score']}/100 -> [{report['health_status']}]")
    
    print("\n--- 📈 MÔI TRƯỜNG GIẢ LẬP: XU HƯỚNG CHI TIÊU 3 THÁNG GẦN NHẤT ---")
    print("(Giúp học sinh nhận diện xu hướng tăng/giảm dòng tiền)")
    months = ["Tháng trước (T-2)", "Tháng trước (T-1)", "Tháng này (Hiện tại)"]
    for m, val in zip(months, report['trend_data']):
        bar = "█" * int(val / (report['total_income'] * 0.1 + 1) * 3) if report['total_income'] > 0 else ""
        print(f" {m:<20} : {val:10,.0f} VNĐ |{bar}")

    print("\n--- 🧠 NHẬN DIỆN BẪY TÀI CHÍNH & CẢNH BÁO ---")
    if not report['warnings']:
        print(" 🎉 Tuyệt vời! Không phát hiện bẫy rủi ro tài chính nào.")
    else:
        for w in report['warnings']:
            print(f" * [{w['type']}]\n   Chi tiết: {w['detail']}")

    print("\n--- 💡 LỜI KHUYÊN HÀNH ĐỘNG TỪ CHUYÊN GIA AI ---")
    for adv in report['advice']:
        print(f" {adv}")

    print("\n" + "-"*50)
    print(" 📝 GÓP Ý & ĐÁNH GIÁ TRẢI NGHIỆM PHẦN MỀM")
    print("-"*50)
    fb_rating = input("Bạn đánh giá thế nào về độ hữu ích của phần mềm từ 1 đến 5 sao? (Ví dụ: 5): ")
    fb_comment = input("Ý kiến đóng góp hoặc tính năng bạn muốn cải thiện thêm: ")
    
    app.collect_feedback(fb_rating, fb_comment)
    print("\n🙏 Cảm ơn bạn đã đóng góp! Ý kiến của bạn đã được ghi nhận để hệ thống ngày càng thông minh hơn.")