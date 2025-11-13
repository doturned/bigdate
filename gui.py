import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from finance import add_record, list_records, summary
from export import to_csv
from chart import expense_pie
from utils import parse_amount, get_current_date

class App(ttk.Window):
    def __init__(self):
        super().__init__(title="记账本", size=(400, 500), resizable=(False, False))
        self.build_ui()

    def build_ui(self):
        ttk.Label(self, text="类别", font=("微软雅黑", 10)).pack(pady=5)
        self.cat = ttk.Entry(self, width=25); self.cat.pack()

        ttk.Label(self, text="描述", font=("微软雅黑", 10)).pack(pady=5)
        self.desc = ttk.Entry(self, width=25); self.desc.pack()

        ttk.Label(self, text="金额（收入正/支出负）", font=("微软雅黑", 10)).pack(pady=5)
        self.amt = ttk.Entry(self, width=25); self.amt.pack()

        ttk.Button(self, text="添加记录", command=self.add, bootstyle=SUCCESS).pack(pady=10)
        ttk.Button(self, text="查看全部", command=list_records, bootstyle=INFO).pack(pady=5)
        ttk.Button(self, text="统计收支", command=summary, bootstyle=INFO).pack(pady=5)
        ttk.Button(self, text="导出 CSV", command=to_csv, bootstyle=WARNING).pack(pady=5)
        ttk.Button(self, text="支出饼图", command=expense_pie, bootstyle=DANGER).pack(pady=5)

    def add(self):
        try:
            amount = parse_amount(self.amt.get())
            add_record(self.cat.get(), self.desc.get(), amount)
            self.cat.delete(0, END); self.desc.delete(0, END); self.amt.delete(0, END)
        except ValueError as e:
            ttk.dialogs.Messagebox.show_error(f"输入错误：{e}", title="提示")

if __name__ == "__main__":
    App().mainloop()