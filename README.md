# ByzantineChainReplication


## Dependencies

```
    python3 -r requirements.txt
```

## Checklist

### Client

- [x] generate pseudorandom workload with good diversity using specified seed  
- [x] generate request sequence specified in config file  
- [x] handle result: check signatures and hashes in result proof  
- [x] timeout and send request to all replicas if timely response not received  
- [ ] check that dictionary contains expected content at end of test case  

### Olympus

- [x] create initial configuration: create keys, create, setup, and start processes  

### Replicas

- [x] dictionary object: support put, get, slice, append  
- [x] head: handle new request: assign slot, sign order stmt & result stmt, send shuttle  
- [x] head: handle retransmitted request as described in paper  
- [x] handle shuttle: check validity of order proof (incl. signatures), add signed order statement and signed result statement, send updated shuttle  
- [x] tail: send result to client; send result shuttle to predecessor  
- [x] handle result shuttle: validate, save, and forward it  
- [x] non-head: handle request: send cached result, send error, or forward request  
- [x] fault-injection: required triggers (1 pt each)  
- [x] fault-injection: required failures (1 pt each)  

### MULTI-HOST EXECUTION  
- [ ] processes are spread across multiple hosts  

### CONFIGURATION FILES  
- [x] support configuration files specified in project.txt (if not, causing inability to test some functionality with instructor's testcases, also lose 1/3 of points for it)  

### LOGS  
- [ ] detailed and readable logs (If some functionality cannot be adequately verified due to inadequate logs, deduct suitable points for each affected item above)  

### DOCUMENTATION  
- [ ] README and testing.txt contain all information specified in project.txt  
