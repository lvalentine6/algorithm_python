def solution(edges):
    # 최대 노드 숫자 구하기
    max_node = max([i for sub in edges for i in sub])

    # 각 노드의 나가는 간선과 들어오는 간선을 리스트로 구성
    out_in = [[0, 0] for _ in range(max_node)]

    for start_node, end_node in edges:
        out_in[start_node - 1][0] += 1
        out_in[end_node - 1][1] += 1

    p_node = s_node = node_8 = 0

    for idx, node in enumerate(out_in):
        out_cnt, in_cnt = node
        # 나가는 간선이 없다면 막대모양
        if out_cnt == 0:
            s_node += 1
        # 나가는 간선이 2개 이상이고 들어오는 간선이 없다면 정점
        elif out_cnt >= 2 and in_cnt == 0:
            p_node = idx + 1
        # 나가는 간선이 2개이고 들어오는 간선이 2개 이상이면 8자모양
        elif out_cnt == 2 and in_cnt >= 2:
            node_8 += 1

    # 도넛 모양 = 정점에서 나가는 간선의 개수 - 막대모양 도형 개수 - 8자 모양 도형 개수
    d_node = out_in[p_node - 1][0] - s_node - node_8

    answer = [p_node, d_node, s_node, node_8]

    return answer
