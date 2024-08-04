def hello():
    print('hello from util.py')


from werkzeug.datastructures import ImmutableMultiDict

def get_values(data_dict: ImmutableMultiDict) -> list:
    values = [int(data_dict.get(key)) for key in data_dict.keys() if data_dict.get(key) is not None and data_dict.get(key) != '']
    return values


if __name__ == '__main__':
    hello()
    result = get_values(data_dict)
    print(result)

