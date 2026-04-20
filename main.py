# ============================================================
#  COMP2152 — Term Project: CTF Bug Bounty
#  Main Runner — Runs all individual vulnerability check scripts
# ============================================================

import subprocess
import sys
import os

scripts = [
    "vaishnavi_http_check.py",
    "vaishnavi_port_check.py",
    "vaishnavi_header_check.py",
]

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n" + "=" * 50)
    print("  COMP2152 — Individual Submission Runner")
    print("  Running all vulnerability checks...")
    print("=" * 50, flush=True)

    for script in scripts:
        print(f"\n>>> Running {script}...\n", flush=True)
        script_path = os.path.join(script_dir, script)
        subprocess.run([sys.executable, script_path])

    print("\n" + "=" * 50)
    print("  All checks complete.")
    print("=" * 50 + "\n")
