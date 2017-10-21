import config_handler
import json


if __name__ == '__main__':
    test_value = json.loads(config_handler.load_config()['test1']['test_dict'])
    data = None
    with open('test.json') as test_file:    
        data = json.load(test_file)
    if data is not None:
        if data == test_value:
            print('Verified')
        else:
            print('Data: ' + str(data) + str(type(data)))
            print('Test: ' + str(test_value) + str(type(test_value)))
            print('Did not match')

    else:
        print('data is None?!')
