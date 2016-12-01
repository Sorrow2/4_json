import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as file:
        return json.load(file)


def pretty_print_json(json_data):
    return json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    try:
        json_file = input('Введите путь до json файла: ')
        print(pretty_print_json(load_data(json_file)))
    except FileNotFoundError:
        print('Файл не найден. Попробуйте ещё раз.')
    except json.decoder.JSONDecodeError:
        print('Файл не является JSON. Попробуйте ещё раз.')
    except UnicodeDecodeError:
        print('Ошибка кодировки. Данный должны быть в UTF-8')
