# finance.py
from storage import load_records, save_records
from utils import get_current_date

# -------- 原有 add_record 保留 --------
def add_record(category, description, amount, date=None):
    date = date or get_current_date()
    try:
        amount = float(amount)
    except ValueError:
        print("❌ 金额必须是数字！")
        return
    records = load_records()
    records.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    })
    save_records(records)
    print("✅ 记录已添加！")

# -------- 新增 --------
def list_records():
    records = load_records()
    if not records:
        print("📭 暂无记录")
        return
    print("\n📒 所有记录：")
    print(f"{'日期':<12}{'类别':<10}{'描述':<12}{'金额':>8}")
    print("-" * 42)
    for r in records:
        print(f"{r['date']:<12}{r['category']:<10}{r['description']:<12}{r['amount']:>8.2f}")

def summary():
    records = load_records()
    income = sum(r['amount'] for r in records if r['amount'] > 0)
    expense = sum(r['amount'] for r in records if r['amount'] < 0)
    balance = income + expense
    print("\n📊 统计：")
    print(f"  总收入：{income:>10.2f}")
    print(f"  总支出：{expense:>10.2f}")
    print(f"  余额：  {balance:>10.2f}")
# 放在 finance.py 末尾
def filter_records(date=None, category=None):
    records = load_records()
    if date:
        records = [r for r in records if r["date"] == date]
    if category:
        records = [r for r in records if r["category"].lower() == category.lower()]
    if not records:
        print("📭 没有符合条件的记录")
        return
    print(f"\n🔍 筛选结果（日期={date or '不限'}, 类别={category or '不限'}）：")
    print(f"{'日期':<12}{'类别':<10}{'描述':<12}{'金额':>8}")
    print("-" * 42)
    for r in records:
        print(f"{r['date']:<12}{r['category']:<10}{r['description']:<12}{r['amount']:>8.2f}")