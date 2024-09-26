from collections import defaultdict


def solution(points, routes):
    # 포인트 번호를 기준으로 좌표 매핑
    point_map = {i + 1: tuple(point) for i, point in enumerate(points)}

    # 각 로봇의 전체 경로를 시간별로 기록
    robot_paths = []
    for route in routes:
        path = []
        current = point_map[route[0]]
        path.append(current)
        for next_point in route[1:]:
            target = point_map[next_point]
            # 최단 경로를 r 먼저, 그 다음 c 변경
            while current != target:
                r, c = current
                tr, tc = target
                if r < tr:
                    r += 1
                elif r > tr:
                    r -= 1
                elif c < tc:
                    c += 1
                elif c > tc:
                    c -= 1
                current = (r, c)
                path.append(current)
        robot_paths.append(path)

    # 모든 로봇의 최대 이동 시간 계산
    max_time = max(len(path) for path in robot_paths)

    # 시간별로 로봇의 위치를 기록하고 위험 상황을 카운트
    danger = 0
    for t in range(max_time):
        position_count = defaultdict(int)
        for path in robot_paths:
            if t < len(path):
                position = path[t]
                position_count[position] += 1
        # 각 위치별로 2대 이상인 경우 카운트
        for count in position_count.values():
            if count >= 2:
                danger += 1
    return danger
