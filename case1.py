import pandas as pd
import os

def get_params_for_dataset(dataset):
    group1_datasets = {'house_bills', 'kosarak', 'Insta_cart'}
    group2_datasets = {'gowalla', 'amazon', 'aminer'}
    
    if dataset in group1_datasets:
        return {'k': 30, 'g': 30, 'p': 0.8}
    elif dataset in group2_datasets:
        return {'k': 5, 'g': 5, 'p': 0.8}
    else:
        return {'k': 0, 'g': 0, 'p': 0.0}  # Fallback/default parameters

def process_results(base_dir, algorithms, datasets):
    all_results = []

    for dataset in datasets:
        params = get_params_for_dataset(dataset)  # Get the specific parameters for the dataset
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


        for algorithm in algorithms:
            display_algorithm_name = 'NPA' if algorithm == 'naive' else algorithm
            data_dir = os.path.join(base_dir, algorithm, dataset)
            file_name = f"{dataset}_k{params['k']}_g{params['g']}_p{params['p']}.txt"
            file_path = os.path.join(data_dir, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    data = file.read()

                run_time = float(data.split("Run_Time: ")[1].split()[0])
                kg_time = float(data.split("KG_Time: ")[1].split()[0])
                main_time = float(data.split("Main_Time: ")[1].split()[0])
                ng_time = float(data.split("N^g_Time: ")[1].split()[0])

                all_results.append({
                    'data': formatted_dataset_name,
                    'algorithm': display_algorithm_name,
                    'value1': run_time,
                    'value2': kg_time,
                    'value3': main_time,
                    'value4': ng_time
                })
            else:
                print(f"Warning: {file_path} does not exist.")

    output_dir = os.path.join(base_dir, 'csv', 'case1')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file_path = os.path.join(output_dir, "case1.csv")
    df = pd.DataFrame(all_results)

    df['algorithm_sort'] = df['algorithm'].map({'NPA': 1, 'ASAP': 2})
    df.sort_values(by=['data', 'algorithm_sort'], inplace=True)
    df.drop('algorithm_sort', axis=1, inplace=True)

    df.to_csv(output_file_path, index=False)
    print(f"File saved: {output_file_path}")

# 실험을 위한 주 폴더 경로
base_dir = "./output"

# 사용할 알고리즘 목록
algorithms = ['naive', 'ASAP']

# 데이터셋 목록
datasets = ['house_bills', 'kosarak', 'Insta_cart', 'gowalla', 'amazon', 'aminer']

# 결과 처리
process_results(base_dir, algorithms, datasets)
