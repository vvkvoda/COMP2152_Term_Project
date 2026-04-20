# COMP2152 — Term Project: CTF Bug Bounty

## Submission Type
Individual submission due to exceptional circumstances.

## Student Information
- **Name:** Vaishnavi Vodapalli
- **Student ID:** 101504750
- **Course Code:** COMP2152

## Team / Member Table

| Member | Vulnerability Found | Branch Name |
|--------|---------------------|-------------|
| Vaishnavi Vodapalli | HTTP not enforced / Open Telnet port / Missing security header | individual_submission |

## Videos
- Vaishnavi: (https://youtu.be/wjlGUKIZAhY)

## Target
- Server: `0x10.cloud` and its subdomains
- Submission: `submit.0x10.cloud`
- Leaderboard: `ranking.0x10.cloud`

## Important: Rate Limit
The server allows **10 requests per second** per IP address. If requests are sent too quickly, the server may return HTTP 429. Add a small delay between requests when needed.

```python
import time
time.sleep(0.15)
```

## Repository Files
- `vaishnavi_http_check.py` — checks whether HTTP redirects to HTTPS
- `vaishnavi_port_check.py` — checks whether Telnet port 2323 is open
- `vaishnavi_header_check.py` — inspects headers for a missing security header
- `main.py` — runs all three scripts
- `AI Usage Declaration.docx`

## Vulnerability Summary
| Script | Vulnerability |
|--------|--------------|
| `vaishnavi_http_check.py` | Website does not enforce HTTPS |
| `vaishnavi_port_check.py` | Open Telnet port (2323) |
| `vaishnavi_header_check.py` | Missing `X-Frame-Options` header |

## Notes
This repository is organized as an individual submission and uses Python standard library modules only.
