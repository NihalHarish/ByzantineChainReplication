import re
import random

from random_words import RandomWords

def load_config(config_file='config.csv'):
    config = {}
    test_cases = {}
    test_case_key = None
    with open(config_file,'r') as f:
        for line in f:
            if line[0] != '#':
                (key,sep,val) = line.partition('=')
                # if the line does not contain '=', it is invalid and hence ignored
                if len(sep) != 0:
                    val = val.strip()
                    if key.strip() == 'test_case_name':
                        if test_case_key:
                            test_cases[test_case_key] = parse_config(config)
                        test_case_key = val.strip()
                        config = {}
                    else:
                        config[key.strip()] = int(val) if str.isdecimal(val) else val
    test_cases[test_case_key] = parse_config(config)
    #config = parse_config(config)
    return test_cases

def __generate_pseudo_random_workload(seed, size):
    operation_list = ['put', 'append', 'get', 'slice']
    current_key_set = ['start']
    rw = RandomWords()
    random_workload = []
    workload = ""

    random.seed(seed)

    for x in range(size):
        random_word = rw.random_word()
        random_operation = random.choice(operation_list)
        if random_operation == 'put':
            workload += "put('" + random_word + "', '" + rw.random_word() + "'); "
            current_key_set.append(random_word)
        elif random_operation == 'get':
            workload += "get('" + random.choice(current_key_set) + "'); "
        elif random_operation == 'append':
            workload += "append('" + random.choice(current_key_set) + "', '" + random_word + "'); "
        elif random_operation == 'slice':
            workload += "slice('" + random.choice(current_key_set) + "', '" + str(random.randint(0, 10)) + ":" + str(random.randint(0,10)) + "'); "

    return workload

def pseudorandom(seed, size):
    workload = __generate_pseudo_random_workload(seed, size)
    return workload

def parse_failure_operations(operation_str):
    operations_list = []
    operations_tuple_list = operation_str.split(';')
    for operation in operations_tuple_list:
        operations_tuple = re.split(',\s*(?![^()]*\))', operation)
        operations_list.append(tuple(operations_tuple))
        print('Operations Tuple: ', operations_tuple)
    return operations_list

def parse_config(config):
    workloads = []
    workload_keys = []
    failures = []
    failure_keys = []
    # Generate Psuedorandom Workload
    for key in config:
        regex_match = re.search('workload\[(\d+)\]', key)
        if regex_match != None:
            workload_keys.append(key)
            workload = config[key]
            workloads.insert(int(regex_match.group(1)), workload)
        regex_match = re.search('failures\\[(\\d+),(\\d+)\]', key)
        if regex_match != None:
            config_number = regex_match.group(1)
            replica_number = regex_match.group(2)
            operations = parse_failure_operations(config[key])
            payload = {
                'config_number' : config_number,
                'replica_number' : replica_number,
                'operations' : operations
            }
            failures.append(payload)
            failure_keys.append(key)
    #print(workloads)
    for workload_key in workload_keys:
        config.pop(workload_key)
    config['workload'] = workloads

    for failure_key in failure_keys:
        config.pop(failure_key)
    config['failures'] = failures
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)
    #print(pseudorandom(17, 10))
