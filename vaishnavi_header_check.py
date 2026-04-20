# Author: Vaishnavi Vodapalli
# Student ID: 101504750
# Course: COMP2152
# Vulnerability: Missing security header
# Target: api.0x10.cloud

import urllib.request


def inspect_headers(url: str) -> None:
    try:
        response = urllib.request.urlopen(url, timeout=5)
        headers = dict(response.headers)

        server = headers.get("Server", "Not disclosed")
        x_frame = headers.get("X-Frame-Options", "Not disclosed")

        print(f"Server: {server}")
        print(f"X-Frame-Options: {x_frame}")

        if x_frame == "Not disclosed":
            print("VULNERABILITY: Missing X-Frame-Options header")
            print("Risk: Website may be vulnerable to clickjacking attacks")
        else:
            print("Security header present")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    inspect_headers("http://api.0x10.cloud")
