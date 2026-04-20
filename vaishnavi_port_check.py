# Author: Vaishnavi Vodapalli
# Student ID: 101504750
# Course: COMP2152
# Vulnerability: Open Telnet port
# Target: telnet.0x10.cloud:2323

import socket


def check_port(host: str, port: int) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"VULNERABILITY: Port {port} is OPEN on {host}")
            print("Risk: Telnet sends data in plaintext and is insecure")
        else:
            print(f"Port {port} is closed on {host}")
    except Exception as exc:
        print(f"Error: {exc}")
    finally:
        sock.close()


if __name__ == "__main__":
    check_port("telnet.0x10.cloud", 2323)
