PLATFORM: 
    Primary Operating System :MAC OS/X, Fedora 25
    VMs: Ubuntu 16.04
    Docker : Community Edition 17.09.0
    DistAlgo Version: 1.0.9
    Python: Python 3.5.4

INSTRUCTIONS:
    Installation(Dependencies): python3 -r requirements.txt  [Install dependencies]

    How to run the code (Go inside src/): 

    1. First we run main(Lets say test case 1)
        
        Single Node:
            python3 -m da -n MainNode main.da --test_case=test1
        
        Multi Node:
            python3 -m da -H <host_ip> -n MainNode main.da --test_case=test1


    2. Then we run olympus
        2.1 If the workload is a lot, then we run the olympus as:
            
            Single Node:
                python3 -m da --message-buffer-size 10240000 -n OlympusNode -D olympus.da
            
            Multi Node:
                python3 -m da --message-buffer-size 10240000 -H <host_ip> -R <main_node_ip> -n OlympusNode -D olympus.da

        2.2 If workload is not much, then we run olympus as:

            Single Node:
                python3 -m da -n OlympusNode -D olympus.da
            
            Multi Node:
                python3 -m da -H <host_ip> -R <main_node_ip> -n OlympusNode -D olympus.da


    3. Then we run the client
        3.1 If the workload is a lot, then we run the client as:

            Single Node:
                python3 -m da --message-buffer-size 10240000 -n ClientNode -D client.da
            
            Multi Node:
                python3 -m da --message-buffer-size 10240000 -H <host_ip> -R <main_node_ip> -n ClientNode -D client.da
                
        3.2 If workload is not much, then we run client as:

            Single Node:
                python3 -m da -n ClientNode -D client.da

            Multi Node:
                python3 -m da -H <host_ip> -R <main_node_ip> -n ClientNode -D client.da
                

WORKLOAD GENERATION:
    The algorithm we have used to generate our pseudorandom client workload is as follows:
    
        generate_pseudorandom_workload(seed, size):
            opeartion_list -> [list_of_supported_ips]
            workload -> "empty_string"
            rw -> initialize the Random Word generator
            random.seed(seed) # Initialize the random function with a seed
            current_key_set = [dummy_value] # the current key set is used to store all the keys that
                                            # have been randomly generated. We initialize it with a 
                                            # dummy value, to support 'get', 'append' and 'slice'
                                            # operations, before any keys have been generated
        
            loop though range of size:
                random_word -> generate a random word using rw
                random_operation -> choose a an operation from operation list randomly using the random function
                check the value of the random operation:
                    if random_operation == 'put' then:
                        1. concatenate the workload string with the put opeation along with a random word 
                            as a key and a random word as the value
                        2. store the value of the generated key in current_key_set
                    else if random_operation == 'get' then:
                        1. concatenate the workload string with the get operation along with a key that
                           has been randomly selected from current_key_set
                    else if random_operation == 'append' then:
                        1. concatenate the workload string with the append operation along with a key that has
                           been randomly selected from the current_key_set and a random word as the value
                    else if random_operation == 'slice' then:
                        1. concatenate the workload string with the slice operation along with a key that has
                            been randomly selected from the current_key_set and two colon separated integers
                            between the values 0 and 10 to specify indices.

            return the workload string

                        

BUGS AND LIMITATIONS: Known list of bugs:
    1. Stack overflow during stress testing 

CONTRIBUTIONS:
    Nirvik(nghosh) : Handled the replica module, signature validations, logs
    Nihal(nharish) : Handled olympus, client, workload generation, matching dictionary contents at the end of test case

MAIN FILES: 
    src/replica.da
    src/main.da
    src/olympus.da
    src/client.da


CODE SIZE:

       9 text files.
       9 unique files.                              
       0 files ignored.

github.com/AlDanial/cloc v 1.74  T=0.10 s (151.4 files/s, 46441.2 lines/s)
--------------------------------------------------------------------------------------------------------
File                               blank        comment           code		 algorithm	other
--------------------------------------------------------------------------------------------------------
src/replica.da                         110              1           1306	    997		309		
src/olympus.da                          42              8            460	    354		106
src/client.da                           26              1            257	    204		53
src/test_suite.py                       12              3            119	     0          119
src/config_handler.py                   17              9             89	    26          63
src/main.da                             15              0             66	     0          66
src/constants.py                         8              5             41	     0          41
src/message_type.py                      4              0              7	     0           7
src/test.json                            0              0              1	     0           1
--------------------------------------------------------------------------------------------------------
SUM:                                    234             27           2346           1581	765
--------------------------------------------------------------------------------------------------------

       9 text files.
       9 unique files.                              
       0 files ignored.

github.com/AlDanial/cloc v 1.74  T=0.04 s (212.7 files/s, 61608.0 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
DAL                              4            193             10           2089
Python                           4             41             17            256
JSON                             1              0              0              1
-------------------------------------------------------------------------------
SUM:                             9            234             27           2346
-------------------------------------------------------------------------------

LANGUAGE FEATURE USAGE:
    
    1. List Comprehensions : 1
    2. Dictionary Comprehensions : 0
    3. Set Comprehensions : 0
    4. aggregations : 1
    5. quantifications : 8


PERFORMANCE REPORT:

    1. raft2.da : OUTPUT: elapsed time (seconds):  6.50653600692749
    2. perform900.txt in a single-host configuration: 17.96326896303912
    23.perform900.txt on a multi-host configuration:  20.74592648572649
