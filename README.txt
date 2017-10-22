PLATFORM: 
    Primary Operating System :MAC OS/X, Fedora 25
    VMs: Ubuntu 
    DistAlgo Version: 1.0.9
    Python: Python 3.5.4

INSTRUCTIONS:
    Installation(Dependencies): python3 -r requirements.txt  [Install dependencies]

    How to run the code (Go inside src/): 

    1. First we run main(Lets say test case 1)

        python3 -m da -n MainNode main.da --test_case=test1

    2. Then we run olympus
        2.1 If the workload is a lot, then we run the olympus as:
            python3 -m da --message-buffer-size 10240000 -n OlympusNode -D olympus.da

        2.2 If workload is not much, then we run olympus as:
            python3 -m da -n OlympusNode -D olympus.da

    3. Then we run the client
        3.1 If the workload is a lot, then we run the client as:
            python3 -m da --message-buffer-size 10240000 -n ClientNode -D client.da
                                                                                      
        3.2 If workload is not much, then we run client as:
            python3 -m da -n ClientNode -D client.da

WORKLOAD GENERATION: <nihal>

BUGS AND LIMITATIONS: Known list of bugs:
    1. Currently multi host is not working

CONTRIBUTIONS:
    Nirvik(nghosh) : Handled the replica module, signature validations, logs
    Nihal(nharish) : Handled olympus, client, workload generation, matching dictionary contents at the end of test case

MAIN FILES: 
    src/replica.da
    src/main.da
    src/olympus.da
    src/client.da


CODE SIZE: <nihal>


LANGUAGE FEATURE USAGE: <nihal>
