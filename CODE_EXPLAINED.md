# How the Code Works

This repository contains three Python scripts using only the Python standard library.

## 1. vaishnavi_http_check.py
This script opens `http://blog.0x10.cloud` using `urllib.request.urlopen()`.  
If the final URL still begins with `http://`, it reports that HTTPS is not enforced.

## 2. vaishnavi_port_check.py
This script uses `socket.connect_ex()` to test whether port `2323` is open on `telnet.0x10.cloud`.  
If the connection succeeds, it reports that the Telnet service is exposed.

## 3. vaishnavi_header_check.py
This script requests `http://api.0x10.cloud` and reads response headers.  
If the `X-Frame-Options` header is missing, it reports a possible clickjacking risk.

## Error Handling
Each script uses `try/except` so it prints a readable error message rather than crashing.
