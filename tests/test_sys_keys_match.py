# System test: test_sys_keys_match

import os
from rift_expect_session import RiftExpectSession

def check_rift_node1(res):
    res.check_adjacency_3way(
        node="node1",
        interface="if1")
    expect_rib = [
        r"| 2.2.2.2/32 | South SPF | Positive | if1",
        r"| 3.3.3.3/32 | South SPF | Positive | if1",
    ]
    res.check_rib("node1", expect_rib)
    expect_node_security = [
        r"Security Keys:",
        r"| Key ID | Algorithm | Secret                           |",
        r"| 0      | null      |                                  |",
        r"| 1      | sha-256   | this-is-the-secret-for-key-1     |",
        r"| 2      | sha-256   | this-is-the-secret-for-key-2     |",
        r"| 3      | sha-256   | this-is-the-secret-for-key-3     |",
        r"| 4      | sha-256   | this-is-the-secret-for-key-4     |",
        r"| 66051  | sha-256   | this-is-the-secret-for-key-66051 |",
        r"Origin Keys:",
        r"| Active Origin Key  | 4     |",
        r"| Accept Origin Keys | 66051 |",
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_node_security("node1", expect_node_security)
    expect_intf_security = [
        r"Outer Keys:",
        r"| Key | Key ID\(s\) | Configuration Source |",
        r"| Active Outer Key  | 1 | Interface Active Key  |",
        r"| Accept Outer Keys | 2 | Interface Accept Keys |",
        r"Nonces:",
        r"| Last Received LIE Nonce  | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"| Last Sent Nonce          | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_intf_security("node1", "if1", expect_intf_security)

def check_rift_node2(res):
    res.check_adjacency_3way(
        node="node2",
        interface="if1")
    res.check_adjacency_3way(
        node="node2",
        interface="if2")
    expect_rib = [
        r"| 0.0.0.0/0  | North SPF | Positive | if1",
        r"| 3.3.3.3/32 | South SPF | Positive | if2",
    ]
    res.check_rib("node2", expect_rib)
    expect_node_security = [
        r"Security Keys:",
        r"| Key ID | Algorithm | Secret                           |",
        r"| 0      | null      |                                  |",
        r"| 1      | sha-256   | this-is-the-secret-for-key-1     |",
        r"| 2      | sha-256   | this-is-the-secret-for-key-2     |",
        r"| 3      | sha-256   | this-is-the-secret-for-key-3     |",
        r"| 4      | sha-256   | this-is-the-secret-for-key-4     |",
        r"| 66051  | sha-256   | this-is-the-secret-for-key-66051 |",
        r"Origin Keys:",
        r"| Active Origin Key  | 4     |",
        r"| Accept Origin Keys | 66051 |",
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted | [0-9]*[1-9][0-9]* Packets",   # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_node_security("node2", expect_node_security)
    expect_intf_security = [
        r"Outer Keys:",
        r"| Key | Key ID\(s\) | Configuration Source |",
        r"| Active Outer Key  | 2 | Interface Active Key  |",
        r"| Accept Outer Keys | 1 | Interface Accept Keys |",
        r"Nonces:",
        r"| Last Received LIE Nonce  | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"| Last Sent Nonce          | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_intf_security("node2", "if1", expect_intf_security)
    expect_intf_security = [
        r"Outer Keys:",
        r"| Key | Key ID\(s\) | Configuration Source |",
        r"| Active Outer Key  | 2 | Interface Active Key  |",
        r"| Accept Outer Keys | 3 | Interface Accept Keys |",
        r"Nonces:",
        r"| Last Received LIE Nonce  | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"| Last Sent Nonce          | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_intf_security("node2", "if2", expect_intf_security)

def check_rift_node3(res):
    res.check_adjacency_3way(
        node="node3",
        interface="if1")
    expect_rib = [
        r"| 0.0.0.0/0 | North SPF | Positive | if1",
    ]
    res.check_rib("node3", expect_rib)
    expect_node_security = [
        r"Security Keys:",
        r"| Key ID | Algorithm | Secret                           |",
        r"| 0      | null      |                                  |",
        r"| 1      | sha-256   | this-is-the-secret-for-key-1     |",
        r"| 2      | sha-256   | this-is-the-secret-for-key-2     |",
        r"| 3      | sha-256   | this-is-the-secret-for-key-3     |",
        r"| 4      | sha-256   | this-is-the-secret-for-key-4     |",
        r"| 66051  | sha-256   | this-is-the-secret-for-key-66051 |",
        r"Origin Keys:",
        r"| Active Origin Key  | 66051 |",
        r"| Accept Origin Keys | 4     |",
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_node_security("node3", expect_node_security)
    expect_intf_security = [
        r"Outer Keys:",
        r"| Key | Key ID\(s\) | Configuration Source |",
        r"| Active Outer Key  | 3 | Interface Active Key  |",
        r"| Accept Outer Keys | 2 | Interface Accept Keys |",
        r"Nonces:",
        r"| Last Received LIE Nonce  | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"| Last Sent Nonce          | [0-9]*[1-9][0-9]* |",   # non-zero value
        r"Security Statistics:",
        r"| Non-empty outer fingerprint accepted  | [0-9]*[1-9][0-9]* Packets",  # non-zero value
        r"| Non-empty origin fingerprint accepted | [0-9]*[1-9][0-9]* Packets",  # non-zero value
    ]
    res.check_intf_security("node3", "if1", expect_intf_security)

def test_keys_match():
    passive_nodes = os.getenv("RIFT_PASSIVE_NODES", "").split(",")
    res = RiftExpectSession("keys_match")
    if "node1" not in passive_nodes:
        check_rift_node1(res)
    if "node2" not in passive_nodes:
        check_rift_node2(res)
    if "node3" not in passive_nodes:
        check_rift_node3(res)
    res.stop()
