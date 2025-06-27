
import json

with open('alt.json', 'r', encoding='utf-8') as file:
    data = json.load(file)["output"]
    # print(data)
def main(arg1: list):
    # json_str=arg1[0]
    # json_data=json.loads(json_str)
    result_list=[]
    for item in arg1:
        for i in item:
            if i:
                result_list.append(i)
    return result_list
data2=main(data)
# print(data2)
# print(len(data2))

def alt(arg2:list):
    key_check="步骤"
    correct_list=[]
    for item in arg2:
        if isinstance(item,dict):
            if key_check  in item:
                correct_list.append(item)
    # print(correct_list)
    # print(len(correct_list))
    list_1=[]

    for i in range(int(len(correct_list)/2-1)):
        list_1.append(correct_list.pop(i))

    with open("问题拆分_操作系统_数据清洗1.json", 'a', encoding='utf-8') as f:
        json.dump(list_1, f, ensure_ascii=False, indent=4)

    with open("问题拆分_操作系统_数据清洗2.json", 'a', encoding='utf-8') as f:
        json.dump(correct_list, f, ensure_ascii=False, indent=4)
# alt(data2)

def check_same():
    with open('问题拆分_操作系统_数据清洗1.json', 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open('问题拆分_操作系统_数据清洗2.json', 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    for item1 in data1:
        query=item1["答案"]
        for item2 in data2:
            if query==item2["答案"]:
                print(query)
            else:exit(0)
check_same()