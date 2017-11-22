import config_handler
import json
from optparse import OptionParser
import sys
import config_handler
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def craft_operation_payload(operation):
     operation_payload = {}
     operation_payload['opr'] = re.match(
         r'^[^\(]+', operation).group().strip()
     if operation_payload['opr'] == 'get':
         value = re.search(
             r'\(([^)]+)\)',
             operation).group()[
             1:- 
             1].replace(
             "'",
             "") 
         key = None
     else:
         key, value = re.search(
             r'\(([^)]+)\)', operation).group()[1:-1].replace("'", "").split(',')
     operation_payload['payload'] = {}
     operation_payload['payload']['key'] = key.strip() if key else None
     operation_payload['payload']['value'] = value
     return operation_payload

def parse_workload_client(workload):
     workload_list = workload.split(';')
     # print('Workload List: ', workload_list)
     operation_set = []
     for work in workload_list:
         operation_set.append(work)
     if operation_set[-1] == ' ':
         return operation_set[:-1]
     return operation_set

def do_dict_operation(operation, test_dict):
    op = operation['opr']
    payload = operation['payload']
    key = payload['key']
    value = payload['value']
    if op == 'put':
        test_dict[key] = value
    elif op == 'append':
        if key in test_dict:
            test_dict[key] = test_dict[key]+value
    elif op == 'slice':
       if key in test_dict:
            early_value = test_dict[key]
            start, end = value.split(':')
            if start == '' and end != '': 
                end = int(end)
                test_dict[key] = early_value[: end]
            elif start != '' and end == '': 
                start = int(start)
                test_dict[key] = early_value[start:]
            else:
                start = int(start)
                end = int(end)
                if end > start:
                    test_dict[key] = early_value[start:end] 

def parse_workload(workload):
    match = re.match(r'^[^\(]+', workload).group()
    if match == 'pseudorandom':
        seed, size = re.search(
            r'\(([^)]+)\)', workload).group()[1:-1].replace("'", "").split(',')
        seed = int(seed)
        size = int(size)
        workload = config_handler.pseudorandom(seed, size)
        #print('Workload: ', workload)
    return workload

def dict_simulator(test_case):
    test_dict = {}
    for workload in config_handler.load_config()[test_case]['workload']:
        workload = parse_workload(workload)
        workload = parse_workload_client(workload)
        for operation in workload:
            op = craft_operation_payload(operation)
            do_dict_operation(op, test_dict)
    return test_dict
    

if __name__ == '__main__':

    option_parser = OptionParser()
    option_parser.add_option("--test_case_name",\
                             dest='test_case',\
                             help = 'test case name in the config \
                                    file that should be tested',\
                             metavar='TESTCASE')
    (options, args) = option_parser.parse_args()
    test_case = None

    if not options.test_case:
        print('Print Test Case Name Not Supplied')
        sys.exit(0)
    else:
        test_case = options.test_case
    simulated_dict = dict_simulator(test_case)
    #print(simulated_dict)

    test_value = json.loads(config_handler.load_config()[test_case]['test_dict'])
    test_value = simulated_dict
    client_data = None
    with open('test.json') as test_file:
        client_data = json.load(test_file)
    if client_data is not None:
        if client_data == test_value:
            pass
        else:
            print(bcolors.FAIL, '[Failed]: ', bcolors.ENDC)
    for key in test_value:
        if key in client_data:
            if client_data[key] == test_value[key]:
                print(bcolors.OKGREEN, '[Passed]', bcolors.ENDC, 'Key: ' +str(key)+ " Value: " + str(test_value[key]))
            else:
                print(bcolors.FAIL, '[Failed]', bcolors.ENDC, 'Key: ' +str(key)+ " Value: " + str(test_value[key]))
        else:
            print(bcolors.FAIL, '[Failed] ' + str(key)+' : '+str(test_value[key]), bcolors.ENDC)
