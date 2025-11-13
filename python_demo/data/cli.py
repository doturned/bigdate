# cli.py
import argparse, sys
from finance import add_record, list_records, summary
from utils import parse_date, parse_amount

def main():
    parser = argparse.ArgumentParser(description="个人记账本-命令行模式")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="添加记录")
    p_add.add_argument("-c", "--category", required=True, help="类别")
    p_add.add_argument("-d", "--desc", required=True, help="描述")
    p_add.add_argument("-a", "--amount", required=True, help="金额")
    p_add.add_argument("--date", help="日期 yyyy-mm-dd（默认今天）")

    sub.add_parser("list", help="查看全部")
    sub.add_parser("summary", help="统计收支")

    args = parser.parse_args()

    if args.cmd == "add":
        date = parse_date(args.date or "")
        amount = parse_amount(args.amount)
        add_record(args.category, args.desc, amount, date)
    elif args.cmd == "list":
        list_records()
    elif args.cmd == "summary":
        summary()

if __name__ == "__main__":
    main()