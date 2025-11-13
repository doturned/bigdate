import matplotlib.pyplot as plt
from collections import Counter
from storage import load_records

def expense_pie():
    records = load_records()
    expense = [r for r in records if r["amount"] < 0]
    if not expense:
        print("📭 暂无支出，无法画图"); return
    c = Counter()
    for r in expense:
        c[r["category"]] += -r["amount"]   # 转成正数
    plt.figure(figsize=(4, 4))
    plt.pie(c.values(), labels=c.keys(), autopct="%.1f%%", startangle=90)
    plt.title("支出分布")
    plt.show()