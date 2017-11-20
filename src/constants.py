# Old Failure triggers
RESULT_SHUTTLE_FAILURE_TRIGGER = 'result_shuttle'
CLIENT_REQUEST_FAILURE_TRIGGER = 'client_request'
SHUTTLE_FAILURE_TRIGGER = 'shuttle'
FORWARDED_FAILURE_TRIGGER = 'forwarded_request'
CHANGE_OPERATION_FAILURE = 'change_operation'
CHANGE_RESULT_FAILURE = 'change_result'
DROP_RESULT_FAILURE = 'drop_result_stmt'

# New failure triggers
WEDGE_REQUEST_FAILURE_TRIGGER = 'wedge_request'  # receipt of m'th wedge-request message.
NEW_CONFIGURATION_FAILURE_TRIGGER = 'new_configuration'  # receipt of m'th new_configuration message from Olympus.  it doesn't matter whether your implementation actually sends a new_configuration message for the initial configuration; either way, m=0 corresponds to the first configuration change after the initial configuration.
CHECKPOINT_FAILURE_TRIGGER = 'checkpoint'  # receipt of m'th checkpoint message
COMPLETE_CHECKPOINT_FAILURE_TRIGGER = 'completed_checkpoint'  # receipt of m'th completed checkpoint message
GET_RUNNING_STATE_FAILURE_TRIGGER = 'get_running_state'  #  receipt of m'th get_running_state message.
CATCH_UP_FAILURE_TRIGGER = 'catch_up'  # receipt of m'th catch_up message.

REPLICA_PENDING = 'PENDING'
REPLICA_ACTIVE = 'ACTIVE'
REPLICA_IMMUTABLE = 'IMMUTABLE'


# Shuttle message keys
SHUTTLE_RESULT_PROOF = 'result_proof'
SHUTTLE_ORDER_PROOF = 'order_proof'
SHUTTLE_SLOT = 'slot'
SHUTTLE_OPERATION = 'operation'
SHUTTLE_CHECKSUM = 'checksum'
SHUTTLE_CLIENT_ID = 'client_id'
CLIENT_SIGNATURE = 'client-signature'
SHUTTLE = 'shuttle'

CHECKSUM = 'checksum'
CLIENT_ID = 'client_id'
CLIENT_REQUEST_ID = 'client_request_id'

RESULT = 'result'

STATUS = 'status'

# Old failures
CHANGE_RESULT = 'change_result()'
CHANGE_OPERATION = 'change_operation()'
DROP_RESULT_STMT = 'drop_result_stmt()'
# New Failures
CRASH = 'crash()'  # immediately call logging.shutdown() (to flush logs to disk) and then os._exit(-1).  you need "import logging" and "import os" for this to work.
TRUNCATE_HISTORY = 'truncate_history()'  # in the next outgoing wedged message, send a truncated history by omitting the last entry.
SLEEP = 'sleep()'  # sleep for the specified time, in milliseconds.  this is a timing failure.
DROP = 'drop()'  # drop (i.e., ignore) the incoming message that triggered this failure.
INCREMENT_SLOT = 'increment_slot()'  # if this replica is the head, it immediately increments the variable in which it stores the slot number to assign to the next request.  this should be done before processing the message that triggered the failure.  if this replica is not the head, this failure has no effect.
EXTRA_OP = 'extra_op()'  # this replica immediately applies the operation put('a','a') to its running state.  this should be done before processing the message that triggered the failure.
INVALID_ORDER_SIG = 'invalid_order_sig()'  # in the next outgoing shuttle message, this replica puts an invalid signature on its order statement.
INVALID_RESULT_SIG = 'invalid_result_sig()'  #  if this replica is not the tail, it puts an invalid signature on its result statement in the next outgoing shuttle message [note: this is "shuttle message" not "result shuttle message"].  if this replica is the tail, it puts an invalid signature on its result statement in the next outgoing result message to a client.
DROP_CHECKPOINT_STMTS = 'drop_checkpt_stmts()'  # in the next outgoing completed checkpoint proof shuttle [this is the message that travels along the chain from tail to head], this replica omits the checkpoint statements from the first t+1 replicas in the chain.
