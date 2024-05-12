import os
import pandas as pd

def get_params_for_dataset(dataset):
    group1_datasets = {'house_bills', 'kosarak', 'Insta_cart'}
    group2_datasets = {'gowalla', 'amazon', 'aminer'}
    
    if dataset in group1_datasets:
        return {'k': 30, 'g': 30, 'p': 0.8}
    elif dataset in group2_datasets:
        return {'k': 5, 'g': 5, 'p': 0.8}
    else:
        return {'k': 0, 'g': 0, 'p': 0.0}  # Fallback/default parameters

def process_datasets(output_directory, selected_datasets):
    results = []

    for dataset in selected_datasets:
        default_params = get_params_for_dataset(dataset)  # 데이터셋에 맞는 기본 파라미터 가져오기
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
        
        file_name = f"{dataset}_k{default_params['k']}_g{default_params['g']}_p{default_params['p']}.txt"
        file_path = os.path.join(output_directory, 'ASAP', dataset, file_name)

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = file.read()
            
            nodelb_fail1 = int(data.split("Less_k_NodeLB_Fail: ")[1].split()[0])
            nodelb_fail2 = int(data.split("Ge_k_NodeLB_Fail: ")[1].split()[0])
            nodeLB_fail = nodelb_fail1 + nodelb_fail2
            edgeLB_fail1 = int(data.split("Less_k_EdgeLB_Fail: ")[1].split()[0])
            edgeLB_fail2 = int(data.split("Ge_k_EdgeLB_Fail: ")[1].split()[0])
            edgeLB_fail = edgeLB_fail1 + edgeLB_fail2
            
            results.append({
                'data': formatted_dataset_name,
                'value1': nodelb_fail2,
                'value2': edgeLB_fail2
            })
        else:
            print(f"Warning: {file_path} does not exist.")

    # 결과를 데이터 프레임으로 변환하고 CSV 파일로 저장
    output_dir = os.path.join(output_directory, 'csv', 'case2-2')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df = pd.DataFrame(results)
    df.sort_values(by=['data'], ascending=[True], inplace=True)
    df.to_csv(os.path.join(output_dir, 'case2-2.csv'), index=False)
    print("CSV 파일이 저장되었습니다: case2-2.csv")

output_directory = './output'
selected_datasets = ['gowalla', 'house_bills', 'kosarak', 'Insta_cart', 'amazon', 'aminer']
process_datasets(output_directory, selected_datasets)
