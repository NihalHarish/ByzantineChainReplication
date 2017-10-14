import re
import random

from random_words import RandomWords

def load_config(config_file='config.csv'):
    config = {}
    with open(config_file,'r') as f:
        for line in f:
            if line[0] != '#':
                (key,sep,val) = line.partition('=')
                # if the line does not contain '=', it is invalid and hence ignored
                if len(sep) != 0:
                    val = val.strip()
                    config[key.strip()] = int(val) if str.isdecimal(val) else val
    config = parse_config(config)
    return config


def __generate_pseudo_random_workload(size):
    operation_list = ['put', 'get', 'slice', 'append']
    current_key_set = ['start']
    rw = RandomWords()
    random_workload = []
    workload = ""

    random.random(seed) 

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

def parse_config(config):
    workloads = []
    workload_keys = []
    # Generate Psuedorandom Workload
    for key in config:
        x = re.search('workload\[(\d+)\]', key)
        if x != None:
            workload_keys.append(key)
            workload = config[key]
            workloads.insert(int(x.group(1)), workload)

    #print(workloads)
    for workload_key in workload_keys:
        config.pop(workload_key)
    config['workload'] = workloads
    return config

if __name__ == '__main__':
    config = load_config()
    #print(config)
    print(pseudorandom(17, 10))
