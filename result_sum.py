import os
import pandas as pd
import re

def extract_data_from_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                if value == 'N/A':
                    value = None
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                data[key] = value
    return data

def parse_filename(filename):
    match = re.match(r'.*?_k(\d+)_g(\d+)_p([0-9.]+)\.txt', filename)
    if match:
        return match.groups()
    return None, None, None

def process_datasets(output_directory, selected_datasets):
    results = []
    algorithms = ['naive', 'ASAP']

    for dataset in selected_datasets:
        for algorithm in algorithms:
            directory_path = os.path.join(output_directory, algorithm, dataset)
            if os.path.isdir(directory_path):
                for filename in os.listdir(directory_path):
                    if filename.endswith('.txt'):
                        file_path = os.path.join(directory_path, filename)
                        k, g, p = parse_filename(filename)
                        if k and g and p:
                            data = extract_data_from_file(file_path)
                            result = {
                                'dataset': dataset.capitalize(),
                                'algorithm': algorithm,
                                'k': int(k),
                                'g': int(g),
                                'p': float(p),
                                'Run_Time': data.get('Run_Time'),
                                'KG_Time': data.get('KG_Time'),
                                'Main_Time': data.get('Main_Time'),
                                'Ng_Time': data.get('N^g_Time'),
                                'N^g_Count': data.get('N^g_Count'),
                                'num_kg_node': data.get('num_kg_node'),
                                'num_kg_edge': data.get('num_kg_edge'),
                                'num_remain_node': data.get('num_remain_node'),
                                'num_remain_edge': data.get('num_remain_edge')
                            }
                            results.append(result)

    # 결과를 데이터 프레임으로 변환하고 정렬
    df = pd.DataFrame(results)
    df.sort_values(['dataset', 'algorithm', 'k', 'g', 'p'], ascending=[True, False, True, True, True], inplace=True)
    # 결과를 CSV 파일로 저장
    df.to_csv('./output/csv/output_results.csv', index=False)
    print("CSV 파일이 저장되었습니다: output_results.csv")

output_directory = './output'
selected_datasets = ['gowalla', 'house_bills', 'kosarak', 'Insta_cart',  'amazon', 'aminer']
process_datasets(output_directory, selected_datasets)
