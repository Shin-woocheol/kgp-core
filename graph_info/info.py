def analyze_hypergraph(file_path):
    node_set = set()
    edge_count = 0
    total_nodes_in_edges = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            edge = line.strip().split(',')
            node_ids = set(map(int, edge))  # 중복 제거를 위해 set 사용
            node_set.update(node_ids)
            edge_count += 1
            total_nodes_in_edges += len(node_ids)
    
    num_nodes = len(node_set)
    avg_nodes_per_edge = total_nodes_in_edges / edge_count if edge_count > 0 else 0

    return num_nodes, edge_count, avg_nodes_per_edge

# 파일 경로 예시: 'path/to/your/hypergraph.txt'
# 결과 사용 예시
num_nodes, edge_count, avg_nodes_per_edge = analyze_hypergraph('../ASAP_v5/dataset/real/genres/network.hyp')
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {edge_count}")
print(f"Average number of nodes per edge: {avg_nodes_per_edge:.2f}")
