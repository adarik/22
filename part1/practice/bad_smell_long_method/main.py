# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(string: str) -> list:
    data = []
    for part_str in string.split('\n'):
        data.append(part_str.split(';'))
    return data


def _sort(data: list) -> list:
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data: list) -> list:
    filtered_data = []
    for pair in data:
        if int(pair[1]) > 10:
            filtered_data.append(pair)

    return filtered_data


if __name__ == '__main__':
    print(get_users_list())
