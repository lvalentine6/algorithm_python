import re


def solution(files):
    file_lst = []

    for idx, file in enumerate(files):
        file_split = re.split(r"(\d+)", file)
        tail = ''.join(file_split[2::])
        file_lst.append([file_split[0], file_split[1], tail, str(idx)])

    file_lst_sorted = sorted(file_lst, key=lambda key: (key[0].lower(), int(key[1]), int(key[3])))

    answer = [''.join(file[i] for i in range(3) if file[i] != '') for file in file_lst_sorted]

    return answer