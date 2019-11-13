# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/spanner_v1/proto/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/spanner_v1/proto/transaction.proto',
  package='google.spanner.v1',
  syntax='proto3',
  serialized_options=_b('\n\025com.google.spanner.v1B\020TransactionProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1\312\002\027Google\\Cloud\\Spanner\\V1'),
  serialized_pb=_b('\n/google/cloud/spanner_v1/proto/transaction.proto\x12\x11google.spanner.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xc3\x04\n\x12TransactionOptions\x12\x45\n\nread_write\x18\x01 \x01(\x0b\x32/.google.spanner.v1.TransactionOptions.ReadWriteH\x00\x12O\n\x0fpartitioned_dml\x18\x03 \x01(\x0b\x32\x34.google.spanner.v1.TransactionOptions.PartitionedDmlH\x00\x12\x43\n\tread_only\x18\x02 \x01(\x0b\x32..google.spanner.v1.TransactionOptions.ReadOnlyH\x00\x1a\x0b\n\tReadWrite\x1a\x10\n\x0ePartitionedDml\x1a\xa8\x02\n\x08ReadOnly\x12\x10\n\x06strong\x18\x01 \x01(\x08H\x00\x12\x38\n\x12min_read_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x32\n\rmax_staleness\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x34\n\x0eread_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x34\n\x0f\x65xact_staleness\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x1d\n\x15return_read_timestamp\x18\x06 \x01(\x08\x42\x11\n\x0ftimestamp_boundB\x06\n\x04mode\"M\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x32\n\x0eread_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa4\x01\n\x13TransactionSelector\x12;\n\nsingle_use\x18\x01 \x01(\x0b\x32%.google.spanner.v1.TransactionOptionsH\x00\x12\x0c\n\x02id\x18\x02 \x01(\x0cH\x00\x12\x36\n\x05\x62\x65gin\x18\x03 \x01(\x0b\x32%.google.spanner.v1.TransactionOptionsH\x00\x42\n\n\x08selectorB\x99\x01\n\x15\x63om.google.spanner.v1B\x10TransactionProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_TRANSACTIONOPTIONS_READWRITE = _descriptor.Descriptor(
  name='ReadWrite',
  full_name='google.spanner.v1.TransactionOptions.ReadWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=420,
)

_TRANSACTIONOPTIONS_PARTITIONEDDML = _descriptor.Descriptor(
  name='PartitionedDml',
  full_name='google.spanner.v1.TransactionOptions.PartitionedDml',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=438,
)

_TRANSACTIONOPTIONS_READONLY = _descriptor.Descriptor(
  name='ReadOnly',
  full_name='google.spanner.v1.TransactionOptions.ReadOnly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strong', full_name='google.spanner.v1.TransactionOptions.ReadOnly.strong', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_read_timestamp', full_name='google.spanner.v1.TransactionOptions.ReadOnly.min_read_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_staleness', full_name='google.spanner.v1.TransactionOptions.ReadOnly.max_staleness', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_timestamp', full_name='google.spanner.v1.TransactionOptions.ReadOnly.read_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exact_staleness', full_name='google.spanner.v1.TransactionOptions.ReadOnly.exact_staleness', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_read_timestamp', full_name='google.spanner.v1.TransactionOptions.ReadOnly.return_read_timestamp', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='timestamp_bound', full_name='google.spanner.v1.TransactionOptions.ReadOnly.timestamp_bound',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=441,
  serialized_end=737,
)

_TRANSACTIONOPTIONS = _descriptor.Descriptor(
  name='TransactionOptions',
  full_name='google.spanner.v1.TransactionOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_write', full_name='google.spanner.v1.TransactionOptions.read_write', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partitioned_dml', full_name='google.spanner.v1.TransactionOptions.partitioned_dml', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_only', full_name='google.spanner.v1.TransactionOptions.read_only', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTIONOPTIONS_READWRITE, _TRANSACTIONOPTIONS_PARTITIONEDDML, _TRANSACTIONOPTIONS_READONLY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='mode', full_name='google.spanner.v1.TransactionOptions.mode',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=166,
  serialized_end=745,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='google.spanner.v1.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.spanner.v1.Transaction.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_timestamp', full_name='google.spanner.v1.Transaction.read_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=747,
  serialized_end=824,
)


_TRANSACTIONSELECTOR = _descriptor.Descriptor(
  name='TransactionSelector',
  full_name='google.spanner.v1.TransactionSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='single_use', full_name='google.spanner.v1.TransactionSelector.single_use', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.spanner.v1.TransactionSelector.id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin', full_name='google.spanner.v1.TransactionSelector.begin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='selector', full_name='google.spanner.v1.TransactionSelector.selector',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=827,
  serialized_end=991,
)

_TRANSACTIONOPTIONS_READWRITE.containing_type = _TRANSACTIONOPTIONS
_TRANSACTIONOPTIONS_PARTITIONEDDML.containing_type = _TRANSACTIONOPTIONS
_TRANSACTIONOPTIONS_READONLY.fields_by_name['min_read_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONOPTIONS_READONLY.fields_by_name['max_staleness'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TRANSACTIONOPTIONS_READONLY.fields_by_name['read_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONOPTIONS_READONLY.fields_by_name['exact_staleness'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TRANSACTIONOPTIONS_READONLY.containing_type = _TRANSACTIONOPTIONS
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound'].fields.append(
  _TRANSACTIONOPTIONS_READONLY.fields_by_name['strong'])
_TRANSACTIONOPTIONS_READONLY.fields_by_name['strong'].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound']
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound'].fields.append(
  _TRANSACTIONOPTIONS_READONLY.fields_by_name['min_read_timestamp'])
_TRANSACTIONOPTIONS_READONLY.fields_by_name['min_read_timestamp'].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound']
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound'].fields.append(
  _TRANSACTIONOPTIONS_READONLY.fields_by_name['max_staleness'])
_TRANSACTIONOPTIONS_READONLY.fields_by_name['max_staleness'].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound']
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound'].fields.append(
  _TRANSACTIONOPTIONS_READONLY.fields_by_name['read_timestamp'])
_TRANSACTIONOPTIONS_READONLY.fields_by_name['read_timestamp'].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound']
_TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound'].fields.append(
  _TRANSACTIONOPTIONS_READONLY.fields_by_name['exact_staleness'])
_TRANSACTIONOPTIONS_READONLY.fields_by_name['exact_staleness'].containing_oneof = _TRANSACTIONOPTIONS_READONLY.oneofs_by_name['timestamp_bound']
_TRANSACTIONOPTIONS.fields_by_name['read_write'].message_type = _TRANSACTIONOPTIONS_READWRITE
_TRANSACTIONOPTIONS.fields_by_name['partitioned_dml'].message_type = _TRANSACTIONOPTIONS_PARTITIONEDDML
_TRANSACTIONOPTIONS.fields_by_name['read_only'].message_type = _TRANSACTIONOPTIONS_READONLY
_TRANSACTIONOPTIONS.oneofs_by_name['mode'].fields.append(
  _TRANSACTIONOPTIONS.fields_by_name['read_write'])
_TRANSACTIONOPTIONS.fields_by_name['read_write'].containing_oneof = _TRANSACTIONOPTIONS.oneofs_by_name['mode']
_TRANSACTIONOPTIONS.oneofs_by_name['mode'].fields.append(
  _TRANSACTIONOPTIONS.fields_by_name['partitioned_dml'])
_TRANSACTIONOPTIONS.fields_by_name['partitioned_dml'].containing_oneof = _TRANSACTIONOPTIONS.oneofs_by_name['mode']
_TRANSACTIONOPTIONS.oneofs_by_name['mode'].fields.append(
  _TRANSACTIONOPTIONS.fields_by_name['read_only'])
_TRANSACTIONOPTIONS.fields_by_name['read_only'].containing_oneof = _TRANSACTIONOPTIONS.oneofs_by_name['mode']
_TRANSACTION.fields_by_name['read_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSACTIONSELECTOR.fields_by_name['single_use'].message_type = _TRANSACTIONOPTIONS
_TRANSACTIONSELECTOR.fields_by_name['begin'].message_type = _TRANSACTIONOPTIONS
_TRANSACTIONSELECTOR.oneofs_by_name['selector'].fields.append(
  _TRANSACTIONSELECTOR.fields_by_name['single_use'])
_TRANSACTIONSELECTOR.fields_by_name['single_use'].containing_oneof = _TRANSACTIONSELECTOR.oneofs_by_name['selector']
_TRANSACTIONSELECTOR.oneofs_by_name['selector'].fields.append(
  _TRANSACTIONSELECTOR.fields_by_name['id'])
_TRANSACTIONSELECTOR.fields_by_name['id'].containing_oneof = _TRANSACTIONSELECTOR.oneofs_by_name['selector']
_TRANSACTIONSELECTOR.oneofs_by_name['selector'].fields.append(
  _TRANSACTIONSELECTOR.fields_by_name['begin'])
_TRANSACTIONSELECTOR.fields_by_name['begin'].containing_oneof = _TRANSACTIONSELECTOR.oneofs_by_name['selector']
DESCRIPTOR.message_types_by_name['TransactionOptions'] = _TRANSACTIONOPTIONS
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['TransactionSelector'] = _TRANSACTIONSELECTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionOptions = _reflection.GeneratedProtocolMessageType('TransactionOptions', (_message.Message,), dict(

  ReadWrite = _reflection.GeneratedProtocolMessageType('ReadWrite', (_message.Message,), dict(
    DESCRIPTOR = _TRANSACTIONOPTIONS_READWRITE,
    __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
    ,
    __doc__ = """Message type to initiate a read-write transaction. Currently this
    transaction type has no options.
    """,
    # @@protoc_insertion_point(class_scope:google.spanner.v1.TransactionOptions.ReadWrite)
    ))
  ,

  PartitionedDml = _reflection.GeneratedProtocolMessageType('PartitionedDml', (_message.Message,), dict(
    DESCRIPTOR = _TRANSACTIONOPTIONS_PARTITIONEDDML,
    __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
    ,
    __doc__ = """Message type to initiate a Partitioned DML transaction.
    """,
    # @@protoc_insertion_point(class_scope:google.spanner.v1.TransactionOptions.PartitionedDml)
    ))
  ,

  ReadOnly = _reflection.GeneratedProtocolMessageType('ReadOnly', (_message.Message,), dict(
    DESCRIPTOR = _TRANSACTIONOPTIONS_READONLY,
    __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
    ,
    __doc__ = """Message type to initiate a read-only transaction.
    
    
    Attributes:
        timestamp_bound:
            How to choose the timestamp for the read-only transaction.
        strong:
            Read at a timestamp where all previously committed
            transactions are visible.
        min_read_timestamp:
            Executes all reads at a timestamp >= ``min_read_timestamp``.
            This is useful for requesting fresher data than some previous
            read, or data that is fresh enough to observe the effects of
            some previously committed transaction whose timestamp is
            known.  Note that this option can only be used in single-use
            transactions.  A timestamp in RFC3339 UTC "Zulu" format,
            accurate to nanoseconds. Example:
            ``"2014-10-02T15:01:23.045123456Z"``.
        max_staleness:
            Read data at a timestamp >= ``NOW - max_staleness`` seconds.
            Guarantees that all writes that have committed more than the
            specified number of seconds ago are visible. Because Cloud
            Spanner chooses the exact timestamp, this mode works even if
            the client's local clock is substantially skewed from Cloud
            Spanner commit timestamps.  Useful for reading the freshest
            data available at a nearby replica, while bounding the
            possible staleness if the local replica has fallen behind.
            Note that this option can only be used in single-use
            transactions.
        read_timestamp:
            Executes all reads at the given timestamp. Unlike other modes,
            reads at a specific timestamp are repeatable; the same read at
            the same timestamp always returns the same data. If the
            timestamp is in the future, the read will block until the
            specified timestamp, modulo the read's deadline.  Useful for
            large scale consistent reads such as mapreduces, or for
            coordinating many reads against a consistent snapshot of the
            data.  A timestamp in RFC3339 UTC "Zulu" format, accurate to
            nanoseconds. Example: ``"2014-10-02T15:01:23.045123456Z"``.
        exact_staleness:
            Executes all reads at a timestamp that is ``exact_staleness``
            old. The timestamp is chosen soon after the read is started.
            Guarantees that all writes that have committed more than the
            specified number of seconds ago are visible. Because Cloud
            Spanner chooses the exact timestamp, this mode works even if
            the client's local clock is substantially skewed from Cloud
            Spanner commit timestamps.  Useful for reading at nearby
            replicas without the distributed timestamp negotiation
            overhead of ``max_staleness``.
        return_read_timestamp:
            If true, the Cloud Spanner-selected read timestamp is included
            in the [Transaction][google.spanner.v1.Transaction] message
            that describes the transaction.
    """,
    # @@protoc_insertion_point(class_scope:google.spanner.v1.TransactionOptions.ReadOnly)
    ))
  ,
  DESCRIPTOR = _TRANSACTIONOPTIONS,
  __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
  ,
  __doc__ = """Transactions
  
  
  Each session can have at most one active transaction at a time. After
  the active transaction is completed, the session can immediately be
  re-used for the next transaction. It is not necessary to create a new
  session for each transaction.
  
  Transaction Modes
  
  
  Cloud Spanner supports three transaction modes:
  
  1. Locking read-write. This type of transaction is the only way to write
     data into Cloud Spanner. These transactions rely on pessimistic
     locking and, if necessary, two-phase commit. Locking read-write
     transactions may abort, requiring the application to retry.
  
  2. Snapshot read-only. This transaction type provides guaranteed
     consistency across several reads, but does not allow writes. Snapshot
     read-only transactions can be configured to read at timestamps in the
     past. Snapshot read-only transactions do not need to be committed.
  
  3. Partitioned DML. This type of transaction is used to execute a single
     Partitioned DML statement. Partitioned DML partitions the key space
     and runs the DML statement over each partition in parallel using
     separate, internal transactions that commit independently.
     Partitioned DML transactions do not need to be committed.
  
  For transactions that only read, snapshot read-only transactions provide
  simpler semantics and are almost always faster. In particular, read-only
  transactions do not take locks, so they do not conflict with read-write
  transactions. As a consequence of not taking locks, they also do not
  abort, so retry loops are not needed.
  
  Transactions may only read/write data in a single database. They may,
  however, read/write data in different tables within that database.
  
  Locking Read-Write Transactions
  
  
  Locking transactions may be used to atomically read-modify-write data
  anywhere in a database. This type of transaction is externally
  consistent.
  
  Clients should attempt to minimize the amount of time a transaction is
  active. Faster transactions commit with higher probability and cause
  less contention. Cloud Spanner attempts to keep read locks active as
  long as the transaction continues to do reads, and the transaction has
  not been terminated by [Commit][google.spanner.v1.Spanner.Commit] or
  [Rollback][google.spanner.v1.Spanner.Rollback]. Long periods of
  inactivity at the client may cause Cloud Spanner to release a
  transaction's locks and abort it.
  
  Conceptually, a read-write transaction consists of zero or more reads or
  SQL statements followed by [Commit][google.spanner.v1.Spanner.Commit].
  At any time before [Commit][google.spanner.v1.Spanner.Commit], the
  client can send a [Rollback][google.spanner.v1.Spanner.Rollback] request
  to abort the transaction.
  
  Semantics
  
  
  Cloud Spanner can commit the transaction if all read locks it acquired
  are still valid at commit time, and it is able to acquire write locks
  for all writes. Cloud Spanner can abort the transaction for any reason.
  If a commit attempt returns ``ABORTED``, Cloud Spanner guarantees that
  the transaction has not modified any user data in Cloud Spanner.
  
  Unless the transaction commits, Cloud Spanner makes no guarantees about
  how long the transaction's locks were held for. It is an error to use
  Cloud Spanner locks for any sort of mutual exclusion other than between
  Cloud Spanner transactions themselves.
  
  Retrying Aborted Transactions
  
  
  When a transaction aborts, the application can choose to retry the whole
  transaction again. To maximize the chances of successfully committing
  the retry, the client should execute the retry in the same session as
  the original attempt. The original session's lock priority increases
  with each consecutive abort, meaning that each attempt has a slightly
  better chance of success than the previous.
  
  Under some circumstances (e.g., many transactions attempting to modify
  the same row(s)), a transaction can abort many times in a short period
  before successfully committing. Thus, it is not a good idea to cap the
  number of retries a transaction can attempt; instead, it is better to
  limit the total amount of wall time spent retrying.
  
  Idle Transactions
  
  
  A transaction is considered idle if it has no outstanding reads or SQL
  queries and has not started a read or SQL query within the last 10
  seconds. Idle transactions can be aborted by Cloud Spanner so that they
  don't hold on to locks indefinitely. In that case, the commit will fail
  with error ``ABORTED``.
  
  If this behavior is undesirable, periodically executing a simple SQL
  query in the transaction (e.g., ``SELECT 1``) prevents the transaction
  from becoming idle.
  
  Snapshot Read-Only Transactions
  
  
  Snapshot read-only transactions provides a simpler method than locking
  read-write transactions for doing several consistent reads. However,
  this type of transaction does not support writes.
  
  Snapshot transactions do not take locks. Instead, they work by choosing
  a Cloud Spanner timestamp, then executing all reads at that timestamp.
  Since they do not acquire locks, they do not block concurrent read-write
  transactions.
  
  Unlike locking read-write transactions, snapshot read-only transactions
  never abort. They can fail if the chosen read timestamp is garbage
  collected; however, the default garbage collection policy is generous
  enough that most applications do not need to worry about this in
  practice.
  
  Snapshot read-only transactions do not need to call
  [Commit][google.spanner.v1.Spanner.Commit] or
  [Rollback][google.spanner.v1.Spanner.Rollback] (and in fact are not
  permitted to do so).
  
  To execute a snapshot transaction, the client specifies a timestamp
  bound, which tells Cloud Spanner how to choose a read timestamp.
  
  The types of timestamp bound are:
  
  -  Strong (the default).
  -  Bounded staleness.
  -  Exact staleness.
  
  If the Cloud Spanner database to be read is geographically distributed,
  stale read-only transactions can execute more quickly than strong or
  read-write transaction, because they are able to execute far from the
  leader replica.
  
  Each type of timestamp bound is discussed in detail below.
  
  Strong
  
  
  Strong reads are guaranteed to see the effects of all transactions that
  have committed before the start of the read. Furthermore, all rows
  yielded by a single read are consistent with each other -- if any part
  of the read observes a transaction, all parts of the read see the
  transaction.
  
  Strong reads are not repeatable: two consecutive strong read-only
  transactions might return inconsistent results if there are concurrent
  writes. If consistency across reads is required, the reads should be
  executed within a transaction or at an exact read timestamp.
  
  See
  [TransactionOptions.ReadOnly.strong][google.spanner.v1.TransactionOptions.ReadOnly.strong].
  
  Exact Staleness
  
  
  These timestamp bounds execute reads at a user-specified timestamp.
  Reads at a timestamp are guaranteed to see a consistent prefix of the
  global transaction history: they observe modifications done by all
  transactions with a commit timestamp <= the read timestamp, and observe
  none of the modifications done by transactions with a larger commit
  timestamp. They will block until all conflicting transactions that may
  be assigned commit timestamps <= the read timestamp have finished.
  
  The timestamp can either be expressed as an absolute Cloud Spanner
  commit timestamp or a staleness relative to the current time.
  
  These modes do not require a "negotiation phase" to pick a timestamp. As
  a result, they execute slightly faster than the equivalent boundedly
  stale concurrency modes. On the other hand, boundedly stale reads
  usually return fresher results.
  
  See
  [TransactionOptions.ReadOnly.read\_timestamp][google.spanner.v1.TransactionOptions.ReadOnly.read\_timestamp]
  and
  [TransactionOptions.ReadOnly.exact\_staleness][google.spanner.v1.TransactionOptions.ReadOnly.exact\_staleness].
  
  Bounded Staleness
  
  
  Bounded staleness modes allow Cloud Spanner to pick the read timestamp,
  subject to a user-provided staleness bound. Cloud Spanner chooses the
  newest timestamp within the staleness bound that allows execution of the
  reads at the closest available replica without blocking.
  
  All rows yielded are consistent with each other -- if any part of the
  read observes a transaction, all parts of the read see the transaction.
  Boundedly stale reads are not repeatable: two stale reads, even if they
  use the same staleness bound, can execute at different timestamps and
  thus return inconsistent results.
  
  Boundedly stale reads execute in two phases: the first phase negotiates
  a timestamp among all replicas needed to serve the read. In the second
  phase, reads are executed at the negotiated timestamp.
  
  As a result of the two phase execution, bounded staleness reads are
  usually a little slower than comparable exact staleness reads. However,
  they are typically able to return fresher results, and are more likely
  to execute at the closest replica.
  
  Because the timestamp negotiation requires up-front knowledge of which
  rows will be read, it can only be used with single-use read-only
  transactions.
  
  See
  [TransactionOptions.ReadOnly.max\_staleness][google.spanner.v1.TransactionOptions.ReadOnly.max\_staleness]
  and
  [TransactionOptions.ReadOnly.min\_read\_timestamp][google.spanner.v1.TransactionOptions.ReadOnly.min\_read\_timestamp].
  
  Old Read Timestamps and Garbage Collection
  
  
  Cloud Spanner continuously garbage collects deleted and overwritten data
  in the background to reclaim storage space. This process is known as
  "version GC". By default, version GC reclaims versions after they are
  one hour old. Because of this, Cloud Spanner cannot perform reads at
  read timestamps more than one hour in the past. This restriction also
  applies to in-progress reads and/or SQL queries whose timestamp become
  too old while executing. Reads and SQL queries with too-old read
  timestamps fail with the error ``FAILED_PRECONDITION``.
  
  Partitioned DML Transactions
  
  
  Partitioned DML transactions are used to execute DML statements with a
  different execution strategy that provides different, and often better,
  scalability properties for large, table-wide operations than DML in a
  ReadWrite transaction. Smaller scoped statements, such as an OLTP
  workload, should prefer using ReadWrite transactions.
  
  Partitioned DML partitions the keyspace and runs the DML statement on
  each partition in separate, internal transactions. These transactions
  commit automatically when complete, and run independently from one
  another.
  
  To reduce lock contention, this execution strategy only acquires read
  locks on rows that match the WHERE clause of the statement.
  Additionally, the smaller per-partition transactions hold locks for less
  time.
  
  That said, Partitioned DML is not a drop-in replacement for standard DML
  used in ReadWrite transactions.
  
  -  The DML statement must be fully-partitionable. Specifically, the
     statement must be expressible as the union of many statements which
     each access only a single row of the table.
  
  -  The statement is not applied atomically to all rows of the table.
     Rather, the statement is applied atomically to partitions of the
     table, in independent transactions. Secondary index rows are updated
     atomically with the base table rows.
  
  -  Partitioned DML does not guarantee exactly-once execution semantics
     against a partition. The statement will be applied at least once to
     each partition. It is strongly recommended that the DML statement
     should be idempotent to avoid unexpected results. For instance, it is
     potentially dangerous to run a statement such as
     ``UPDATE table SET column = column + 1`` as it could be run multiple
     times against some rows.
  
  -  The partitions are committed automatically - there is no support for
     Commit or Rollback. If the call returns an error, or if the client
     issuing the ExecuteSql call dies, it is possible that some rows had
     the statement executed on them successfully. It is also possible that
     statement was never executed against other rows.
  
  -  Partitioned DML transactions may only contain the execution of a
     single DML statement via ExecuteSql or ExecuteStreamingSql.
  
  -  If any error is encountered during the execution of the partitioned
     DML operation (for instance, a UNIQUE INDEX violation, division by
     zero, or a value that cannot be stored due to schema constraints),
     then the operation is stopped at that point and an error is returned.
     It is possible that at this point, some partitions have been
     committed (or even committed multiple times), and other partitions
     have not been run at all.
  
  Given the above, Partitioned DML is good fit for large, database-wide,
  operations that are idempotent, such as deleting old rows from a very
  large table.
  
  
  Attributes:
      mode:
          Required. The type of transaction.
      read_write:
          Transaction may write.  Authorization to begin a read-write
          transaction requires
          ``spanner.databases.beginOrRollbackReadWriteTransaction``
          permission on the ``session`` resource.
      partitioned_dml:
          Partitioned DML transaction.  Authorization to begin a
          Partitioned DML transaction requires
          ``spanner.databases.beginPartitionedDmlTransaction``
          permission on the ``session`` resource.
      read_only:
          Transaction will not write.  Authorization to begin a read-
          only transaction requires
          ``spanner.databases.beginReadOnlyTransaction`` permission on
          the ``session`` resource.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.TransactionOptions)
  ))
_sym_db.RegisterMessage(TransactionOptions)
_sym_db.RegisterMessage(TransactionOptions.ReadWrite)
_sym_db.RegisterMessage(TransactionOptions.PartitionedDml)
_sym_db.RegisterMessage(TransactionOptions.ReadOnly)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
  ,
  __doc__ = """A transaction.
  
  
  Attributes:
      id:
          ``id`` may be used to identify the transaction in subsequent
          [Read][google.spanner.v1.Spanner.Read],
          [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql],
          [Commit][google.spanner.v1.Spanner.Commit], or
          [Rollback][google.spanner.v1.Spanner.Rollback] calls.  Single-
          use read-only transactions do not have IDs, because single-use
          transactions do not support multiple requests.
      read_timestamp:
          For snapshot read-only transactions, the read timestamp chosen
          for the transaction. Not returned by default: see [Transaction
          Options.ReadOnly.return\_read\_timestamp][google.spanner.v1.Tr
          ansactionOptions.ReadOnly.return\_read\_timestamp].  A
          timestamp in RFC3339 UTC "Zulu" format, accurate to
          nanoseconds. Example: ``"2014-10-02T15:01:23.045123456Z"``.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

TransactionSelector = _reflection.GeneratedProtocolMessageType('TransactionSelector', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONSELECTOR,
  __module__ = 'google.cloud.spanner_v1.proto.transaction_pb2'
  ,
  __doc__ = """This message is used to select the transaction in which a
  [Read][google.spanner.v1.Spanner.Read] or
  [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql] call runs.
  
  See [TransactionOptions][google.spanner.v1.TransactionOptions] for more
  information about transactions.
  
  
  Attributes:
      selector:
          If no fields are set, the default is a single use transaction
          with strong concurrency.
      single_use:
          Execute the read or SQL query in a temporary transaction. This
          is the most efficient way to execute a transaction that
          consists of a single SQL query.
      id:
          Execute the read or SQL query in a previously-started
          transaction.
      begin:
          Begin a new transaction and execute this read or SQL query in
          it. The transaction ID of the new transaction is returned in [
          ResultSetMetadata.transaction][google.spanner.v1.ResultSetMeta
          data.transaction], which is a
          [Transaction][google.spanner.v1.Transaction].
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.TransactionSelector)
  ))
_sym_db.RegisterMessage(TransactionSelector)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
