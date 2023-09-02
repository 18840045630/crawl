# 数据分割
import csv


# 读取CSV文件
with open('F:/data/fyx_chinamoney.csv', 'r') as file:
    reader = csv.reader(file)
    codes = list(reader)

# 拆分成批次
batch_size = 80
batches = [codes[i:i + batch_size] for i in range(0, len(codes), batch_size)]

# 打印输出每个批次
for batch in batches:
    code_list = [code[0] for code in batch]
    print(code_list)
    print('-' * 20)