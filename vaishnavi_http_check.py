# Author: Vaishnavi Vodapalli
# Student ID: 101504750
# Course: COMP2152
# Vulnerability: Website does not enforce HTTPS
# Target: blog.0x10.cloud

import urllib.request


def check_http_redirect(url: str) -> None:
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(f"Status: {response.status}")
        print(f"Final URL: {response.url}")

        if response.url.startswith("http://"):
            print("VULNERABILITY: Website does not enforce HTTPS")
            print("Risk: Data can be transmitted in plaintext and intercepted")
        else:
            print("Secure: HTTPS is enforced")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    check_http_redirect("http://blog.0x10.cloud")
