Installation(Dependencies):

python3 -r requirements.txt  [Install dependencies]


How to run the code: 

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
