import csv, pathlib, datetime
from storage import load_records

CSV_FILE = pathlib.Path("data/records.csv")

def to_csv():
    records = load_records()
    if not records:
        print("📭 暂无记录，跳过导出"); return
    CSV_FILE.parent.mkdir(exist_ok=True)
    with CSV_FILE.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "description", "amount"])
        writer.writeheader()
        writer.writerows(records)
    print(f"✅ 已导出 → {CSV_FILE.resolve()}")