import config_handler
import json
from optparse import OptionParser
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

    test_value = json.loads(config_handler.load_config()[test_case]['test_dict'])
    client_data = None
    with open('test.json') as test_file:
        client_data = json.load(test_file)
    if client_data is not None:
        if client_data == test_value:
            pass
        else:
            print(bcolors.FAIL, '[Failed]', bcolors.ENDC)
            sys.exit(0)
    for key in test_value:
        if key in client_data:
            # print('checking key: ' +str(key)+ " for value: " + str(test_value[key]))
            if client_data[key] == test_value[key]:
                print(bcolors.OKGREEN, '[Passed]', bcolors.ENDC, 'Status Key: ' +str(key)+ " for value: " + str(test_value[key]))
            else:
                print(bcolors.FAIL, '[Failed]', bcolors.ENDC, 'Status Key: ' +str(key)+ " for value: " + str(test_value[key]))
        else:
            print(bcolors.FAIL, '[Failed]', bcolors.ENDC)
