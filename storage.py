import json,os,pathlib
DATA_FILE = pathlib.Path("data/records.json") 

def load_records():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open( "r",encoding="utf-8") as f:
        return json.load(f)
    

def save_records(records):
    #保证目录存在
    DATA_FILE.parent.mkdir(exist_ok=True)
    with DATA_FILE.open("w",encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


#data=load_records()
#print(f"整体数据类型: {type(data)}")    整体数据类型: <class 'list'>