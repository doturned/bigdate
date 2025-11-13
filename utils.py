# utils.py
from datetime import datetime

def get_current_date():
    return datetime.today().strftime("%Y-%m-%d")

def parse_date(s: str):
    """返回 yyyy-mm-dd 字符串；格式错误抛 ValueError"""
    if s.strip() == "":
        return get_current_date()
    datetime.strptime(s, "%Y-%m-%d")  # 校验
    return s

def parse_amount(s: str):
    """返回 float；非法抛 ValueError"""
    v = float(s)
    if v == 0:
        raise ValueError("金额不能为 0")
    return v