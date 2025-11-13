# main.py
from finance import add_record, list_records, summary, filter_records
from utils import parse_date, parse_amount

menu = """
======== 个人记账本 ========
1. 添加记录
2. 查看全部
3. 统计收支
4. 筛选记录
0. 退出
==========================="""

def safe_input(prompt, parser=str):
    while True:
        try:
            return parser(input(prompt))
        except ValueError as e:
            print(f"❌ 输入无效：{e}")

def main():
    while True:
        print(menu)
        choice = input("请选择操作：").strip()
        if choice == "1":
            date = input("日期（留空=今天，格式 yyyy-mm-dd）：").strip()
            try:
                date = parse_date(date)
            except ValueError:
                print("❌ 日期格式应为 yyyy-mm-dd")
                continue
            category = input("类别: ").strip()
            description = input("描述: ").strip()
            amount = safe_input("金额（收入为正，支出为负）: ", parse_amount)
            add_record(category, description, amount, date)
        elif choice == "2":
            list_records()
        elif choice == "3":
            summary()
        elif choice == "4":
            date = input("筛选日期（留空=不限）：").strip() or None
            category = input("筛选类别（留空=不限）：").strip() or None
            filter_records(date=date, category=category)
        elif choice == "0":
            print("👋 拜拜~")
            break
        else:
            print("❌ 无效选择，请重试")

if __name__ == "__main__":
    main()