import csv

# 原始CSV数据
original_data = [
    "2 + 3 = (),A.4,B.5,C.6,D.7,B",
    "4 - 1 = (),A.2,B.3,C.5,D.1,B",
    "6 * 2 = (),A.12,B.10,C.8,D.6,A",
    "8 ÷ 2 = (),A.4,B.3,C.5,D.6,A",
    "5 + 5 = (),A.8,B.10,C.9,D.7,B",
    "9 - 3 = (),A.6,B.12,C.9,D.3,A",
    "7 * 3 = (),A.21,B.14,C.22,D.23,A",
    "12 ÷ 3 = (),A.4,B.6,C.3,D.5,A",
    "3 + 7 = (),A.10,B.8,C.9,D.11,A",
    "5 - 2 = (),A.3,B.7,C.6,D.2,A",
    "4 * 4 = (),A.16,B.12,C.14,D.10,A",
    "20 ÷ 5 = (),A.4,B.3,C.5,D.2,A",
    "8 + 4 = (),A.12,B.10,C.9,D.7,A",
    "6 - 3 = (),A.3,B.9,C.6,D.2,A",
    "5 * 5 = (),A.25,B.20,C.15,D.30,A",
    "15 ÷ 3 = (),A.5,B.10,C.3,D.7,A",
    "9 + 2 = (),A.11,B.7,C.6,D.12,A",
    "7 - 4 = (),A.3,B.8,C.5,D.2,A",
    "3 * 6 = (),A.18,B.12,C.24,D.9,A",
    "24 ÷ 6 = (),A.4,B.3,C.8,D.12,A",
    "1 + 8 = (),A.9,B.7,C.6,D.10,A",
    "10 - 5 = (),A.5,B.8,C.3,D.7,A",
    "11 + 7 = (),A.18,B.16,C.19,D.17,A",
    "13 - 9 = (),A.4,B.5,C.3,D.6,A",
    "2 * 9 = (),A.18,B.12,C.17,D.11,A",
    "18 ÷ 3 = (),A.6,B.5,C.7,D.8,A",
    "14 + 1 = (),A.15,B.13,C.14,D.12,A",
    "8 - 5 = (),A.3,B.4,C.2,D.6,A",
    "7 * 4 = (),A.28,B.21,C.30,D.24,A",
    "25 ÷ 5 = (),A.5,B.4,C.3,D.6,A",
    "5 + 6 = (),A.11,B.9,C.10,D.8,C",
    "3 - 1 = (),A.2,B.4,C.1,D.3,A",
    "6 * 3 = (),A.18,B.15,C.12,D.9,A",
    "30 ÷ 6 = (),A.5,B.4,C.10,D.8,A",
    "15 + 10 = (),A.25,B.20,C.24,D.22,A",
    "12 - 7 = (),A.5,B.8,C.7,D.4,A",
    "4 * 5 = (),A.20,B.15,C.25,D.12,A",
    "36 ÷ 9 = (),A.4,B.3,C.6,D.5,A",
    "11 + 8 = (),A.19,B.17,C.18,D.20,A",
    "9 - 6 = (),A.3,B.5,C.2,D.4,A",
    "8 * 2 = (),A.16,B.14,C.12,D.10,A",
    "27 ÷ 9 = (),A.3,B.2,C.4,D.5,A",
    "16 + 3 = (),A.19,B.18,C.17,D.15,A",
    "10 - 4 = (),A.6,B.8,C.5,D.7,A",
    "5 * 8 = (),A.40,B.35,C.30,D.25,A",
    "1 + 9 = (),A.10,B.8,C.9,D.7,A",
    "14 - 6 = (),A.8,B.7,C.6,D.5,A",
    "3 * 7 = (),A.21,B.14,C.22,D.23,A",
    "21 ÷ 3 = (),A.7,B.6,C.5,D.8,A",
    "17 + 2 = (),A.19,B.18,C.20,D.17,A",
    "5 - 3 = (),A.2,B.5,C.1,D.3,A",
    "4 * 6 = (),A.24,B.18,C.20,D.22,A",
    "28 ÷ 7 = (),A.4,B.3,C.5,D.6,A",
    "20 + 0 = (),A.20,B.19,C.21,D.18,A",
    "7 - 1 = (),A.6,B.8,C.5,D.7,A",
    "5 * 3 = (),A.15,B.10,C.12,D.14,A",
    "35 ÷ 5 = (),A.7,B.6,C.5,D.8,A",
    "19 + 1 = (),A.20,B.18,C.19,D.17,A",
    "13 - 8 = (),A.5,B.7,C.4,D.6,A",
    "2 * 8 = (),A.16,B.12,C.14,D.10,A",
    "36 ÷ 6 = (),A.6,B.5,C.7,D.8,A",
    "22 + 8 = (),A.30,B.28,C.29,D.27,A",
    "10 - 7 = (),A.3,B.6,C.2,D.5,A",
    "9 * 4 = (),A.36,B.32,C.38,D.34,A",
    "42 ÷ 7 = (),A.6,B.5,C.7,D.8,A",
    "1 + 2 = (),A.2,B.3,C.4,D.5,B",
    "3 - 2 = (),A.1,B.0,C.2,D.3,A",
    "2 * 5 = (),A.10,B.8,C.6,D.5,A",
    "10 ÷ 5 = (),A.2,B.1,C.3,D.4,A",
    "4 + 6 = (),A.10,B.8,C.9,D.7,A",
    "7 - 4 = (),A.3,B.2,C.1,D.5,A",
    "3 * 4 = (),A.12,B.9,C.7,D.6,A",
    "12 ÷ 4 = (),A.3,B.2,C.4,D.5,A",
    "5 + 3 = (),A.8,B.6,C.7,D.9,A",
    "6 - 1 = (),A.5,B.7,C.4,D.3,A",
    "4 * 3 = (),A.12,B.10,C.9,D.8,A",
    "20 ÷ 4 = (),A.5,B.4,C.3,D.6,A",
    "8 + 7 = (),A.15,B.13,C.12,D.11,A",
    "9 - 5 = (),A.4,B.3,C.2,D.5,A",
    "2 * 6 = (),A.12,B.10,C.8,D.7,A",
    "18 ÷ 3 = (),A.6,B.5,C.7,D.8,A",
    "11 + 4 = (),A.15,B.13,C.14,D.12,A",
    "5 - 3 = (),A.2,B.3,C.1,D.4,A",
    "3 * 5 = (),A.15,B.12,C.10,D.14,A",
    "25 ÷ 5 = (),A.5,B.4,C.3,D.6,A",
    "9 + 1 = (),A.10,B.9,C.8,D.7,A",
    "5 - 1 = (),A.4,B.5,C.3,D.6,A",
    "3 * 8 = (),A.24,B.26,C.25,D.23,A",
    "27 ÷ 9 = (),A.3,B.2,C.4,D.5,A",
    "13 + 12 = (),A.25,B.24,C.23,D.22,A",
    "11 - 7 = (),A.4,B.3,C.5,D.6,A",
    "7 * 2 = (),A.14,B.13,C.12,D.11,A",
    "16 ÷ 4 = (),A.4,B.3,C.5,D.6,A",
    "15 + 5 = (),A.20,B.19,C.18,D.17,A",
    "8 - 2 = (),A.6,B.8,C.5,D.7,A",
    "6 * 4 = (),A.24,B.22,C.20,D.21,A",
    "40 ÷ 8 = (),A.5,B.4,C.3,D.6,A",
    "14 + 3 = (),A.17,B.16,C.15,D.14,A",
    "10 - 6 = (),A.4,B.5,C.3,D.2,A",
    "5 * 9 = (),A.45,B.40,C.42,D.43,A",
    "33 ÷ 11 = (),A.3,B.2,C.4,D.5,A",
    "21 + 4 = (),A.25,B.24,C.23,D.22,A",
    "6 - 3 = (),A.3,B.4,C.2,D.5,A",
    "4 * 7 = (),A.28,B.27,C.26,D.25,A",
    "56 ÷ 7 = (),A.8,B.7,C.6,D.5,A",
]

# 转换函数
def transform_line(line):
    parts = line.split(',')
    question = parts[0]  # 获取问题部分
    choices = parts[1:-1]  # 获取选项部分
    correct_answer = parts[-1]  # 获取正确答案部分
    # 移除选项前的字母，并组合问题和选项
    choices = [choice.split('.')[1] for choice in choices]  # 提取数字部分
    return question, choices[0], choices[1], choices[2], choices[3], correct_answer

# 转换所有行
transformed_data = [transform_line(line) for line in original_data]

# 写入CSV文件
with open('primary_math.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Question', 'A', 'B', 'C', 'D', 'Answer'])  # 写入表头
    for data in transformed_data:
        writer.writerow(data)

print("CSV file has been created.")
