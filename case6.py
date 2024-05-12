import os
import csv

# 디렉토리 설정
input_dir = './output/iter_report/ASAP'
output_dir = './output/csv/case6'

# 출력 디렉토리가 없으면 생성
os.makedirs(output_dir, exist_ok=True)

def process_file(filename):
    input_path = os.path.join(input_dir, filename)
    if filename[:-4] == 'kosarak':
        output_path = os.path.join(output_dir, f'case6_Kosarak.csv')
    elif filename[:-4] == 'Insta_cart':
        output_path = os.path.join(output_dir, f'case6_Instacart.csv')
    
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    # 데이터 파싱
    results = []
    for line in lines:
        if 'iter:' in line:
            parts = line.split(',')
            iter_part = int(parts[0].split(':')[1].strip())
            node_part = int(parts[1].split(':')[1].strip())
            edge_part = int(parts[2].split(':')[1].strip())
            results.append([iter_part, node_part, edge_part])
    
    # CSV 파일로 저장
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['iter', 'value1', 'value2'])  # 헤더
        writer.writerows(results)

# 파일 처리
for filename in ['Insta_cart.txt', 'kosarak.txt']:
    process_file(filename)
