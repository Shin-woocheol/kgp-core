import pandas as pd
import os

def get_group_params(dataset):
    # 데이터셋 그룹 설정
    group2 = {'house_bills', 'kosarak', 'Insta_cart'}
    group1 = {'gowalla', 'amazon', 'aminer'}

    if dataset in group1:
        return {
            'default': {'k': 5, 'g': 5, 'p': 0.8},
            'variation': {
                'k': [3, 4, 5, 6, 7],
                'g': [3, 4, 5, 6, 7],
                'p': [0.2, 0.4, 0.6, 0.8, 1.0]
            }
        }
    elif dataset in group2:
        return {
            'default': {'k': 30, 'g': 30, 'p': 0.8},
            'variation': {
                'k': [20, 25, 30, 35, 40],
                'g': [20, 25, 30, 35, 40],
                'p': [0.2, 0.4, 0.6, 0.8, 1.0]
            }
        }
    else:
        # Fallback 설정
        return {
            'default': {'k': 0, 'g': 0, 'p': 0},
            'variation': {
                'k': [0],
                'g': [0],
                'p': [0]
            }
        }

def process_results(base_dir, datasets):
    output_dir = os.path.join('./output', 'csv', 'case4')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results_by_variable = {'k': [], 'g': [], 'p': []}

    for dataset in datasets:
        group_params = get_group_params(dataset)
        default_params = group_params['default']
        variations = group_params['variation']
        if dataset == 'aminer':
            formatted_dataset_name = 'AMiner'
        elif dataset == 'gowalla':
            formatted_dataset_name = 'Gowalla'
        elif dataset == 'house_bills':
            formatted_dataset_name = 'House Bills'
        elif dataset == 'kosarak':
            formatted_dataset_name = 'Kosarak'
        elif dataset == 'Insta_cart':
            formatted_dataset_name = 'Instacart'
        elif dataset == 'amazon':
            formatted_dataset_name = 'Amazon'
        
        for variable, values in variations.items():
            data_dir = os.path.join(base_dir, dataset)

            for value in values:
                current_params = default_params.copy()
                current_params[variable] = value
                file_name = f"{dataset}_k{current_params['k']}_g{current_params['g']}_p{current_params['p']}.txt"
                file_path = os.path.join(data_dir, file_name)
                
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        data = file.read()

                    num_remain_nodes = int(data.split("num_remain_node: ")[1].split()[0])
                    num_remain_edges = int(data.split("num_remain_edge: ")[1].split()[0])
                    # formatted_dataset_name = 'DBLP' if dataset == 'dblp' else dataset.capitalize()

                    results_by_variable[variable].append({
                        'data': formatted_dataset_name,
                        'variable_value': f"{value}",
                        'value1': num_remain_nodes,
                        'value2': num_remain_edges
                    })
                else:
                    print(f"Warning: {file_path} does not exist.")

    # 각 변수에 대한 결과를 해당 변수 이름의 CSV 파일로 저장
    for variable, results in results_by_variable.items():
        df = pd.DataFrame(results)
        df.sort_values(by=['data', 'variable_value'], ascending=[True, True], inplace=True)
        output_file_path = os.path.join(output_dir, f"case4_{variable}.csv")
        df.to_csv(output_file_path, index=False)
        print(f"File saved: {output_file_path}")


# 실험을 위한 주 폴더 경로
base_dir = "./output/naive"

# 데이터셋 목록
datasets = ['house_bills', 'kosarak', 'Insta_cart', 'gowalla', 'amazon', 'aminer']

# 결과 처리
process_results(base_dir, datasets)