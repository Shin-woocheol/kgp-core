import os
import csv
import re

def parse_filename(filename):
    # 파일 이름에서 k, g, p 값 추출, 문자열로 처리
    match = re.search(r'k(\d+)_g(\d+)_p(\d+\.\d+)', filename)
    if match:
        # k, g, p를 문자열로 유지
        return match.groups()
    return None, None, None

def process_file(filename):
    # 파일 내용을 파싱하여 딕셔너리로 변환
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            if(line == '\n'):
                continue
            key, value = line.split(': ')
            data[key.strip()] = value.strip()
    return data

def generate_csv(source_dir, csv_filename):
    files_data = []
    # 각 파일을 반복 처리
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(source_dir, filename)
            k, g, p = parse_filename(filename)
            if k and g and p:
                data = process_file(filepath)
                data['k'] = k
                data['g'] = g
                data['p'] = p
                files_data.append(data)
    
    # k, g, p 기준으로 데이터 정렬
    files_data.sort(key=lambda x: (int(x['k']), int(x['g']), float(x['p'])))
    
    # CSV 파일 생성
    with open(csv_filename, 'w', newline='') as csvfile:
        if files_data:
            # 헤더 정의: k, g, p를 맨 앞으로
            keys = ['k', 'g', 'p'] + [key for key in files_data[0] if key not in ('k', 'g', 'p')]
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            # 데이터 쓰기
            for data in files_data:
                writer.writerow(data)


# 알고리즘과 네트워크 이름 설정
algorithm = 'ASAP'
network = 'hwdblp1'
# algorithm = 'naive'


# 경로 동적 생성
source_dir = f'./output/{algorithm}/{network}/'
final_dir = f'./output/csv/{algorithm}/'
csv_filename = f'./output/csv/{algorithm}/{algorithm}_{network}_summary.csv'

if not os.path.exists(final_dir):
    os.makedirs(final_dir)
# CSV 파일 생성
generate_csv(source_dir, csv_filename)
