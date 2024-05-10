import pandas as pd
import os

def process_results(base_dir, datasets, variable, values, default_params):
    all_results = []  # 모든 데이터셋의 결과를 저장할 리스트

    for dataset in datasets:
        results = []
        variable_defaults = {'k': default_params['k'], 'g': default_params['g'], 'p': default_params['p']}
        data_dir = os.path.join(base_dir, dataset)

        for value in values:
            variable_defaults[variable] = value
            file_name = f"{dataset}_k{variable_defaults['k']}_g{variable_defaults['g']}_p{variable_defaults['p']}.txt"
            file_path = os.path.join(data_dir, file_name)
            
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = file.read()
                
                num_remain_nodes = int(data.split("num_remain_node: ")[1].split()[0])
                num_remain_edges = int(data.split("num_remain_edge: ")[1].split()[0])
                
                # 데이터셋 이름 포맷팅을 저장 단계에서만 적용
                formatted_dataset_name = 'DBLP' if dataset == 'dblp' else dataset.capitalize()
                
                results.append({
                    'data': formatted_dataset_name,  # 데이터셋 이름을 포맷팅하여 저장
                    'variable': f"{value}",
                    'num_of_nodes': num_remain_nodes,
                    'num_of_edges': num_remain_edges
                })
            else:
                print(f"Warning: {file_path} does not exist.")

        # 각 데이터셋의 결과를 전체 결과에 추가
        all_results.extend(results)

    # 결과 저장 폴더 생성
    output_dir = os.path.join('./output', 'csv', 'case3')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 데이터 프레임 생성 및 CSV로 저장
    df = pd.DataFrame(all_results)
    output_file_path = os.path.join(output_dir, f"case4_{variable}.csv")
    df.to_csv(output_file_path, index=False)
    print(f"File saved: {output_file_path}")

# 실험을 위한 주 폴더 경로
base_dir = "./output/naive"

# 기본 파라미터 설정
default_params = {'k': 5, 'g': 5, 'p': 0.8}

datasets = ['contact', 'congress', 'meetup', 'enron', 'trivago', 'history', 'dblp']
params = {
    'k': [3, 4, 5, 6, 7],
    'g': [3, 4, 5, 6, 7],
    'p': [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
}

# 각 변수에 대해 전체 데이터셋의 결과 처리
for variable, values in params.items():
    process_results(base_dir, datasets, variable, values, default_params)
