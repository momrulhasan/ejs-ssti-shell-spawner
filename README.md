# EJS SSTI Shell Spawner

**Auto-exploit CVE-2023-29827 in `ejs@3.1.9` to gain a reverse shell via SSTI → RCE.**

---

## 🛠️ Description

This tool automatically exploits a Server-Side Template Injection (SSTI) vulnerability in `ejs@3.1.9` to trigger Remote Code Execution (RCE) and spawn a reverse shell using a single script.

> 🔥 **CVE-2023-29827**: EJS 3.1.9 allows injection into templates that leads to arbitrary command execution when `escapeFunction` is user-controlled.

---

## ✨ Features

- Interactive prompts (LHOST, LPORT, target path, POST data, cookie)
- Automatic reverse shell payload crafting
- Netcat listener spawns automatically
- Simple and fast exploitation

---

## 📦 Installation

### Using `pip`
```bash
pip install ejs-ssti-shell-spawner
Certainly! Here's the continuation of your `README.md` after the `pip install` section:
```

### Manual Installation

```bash
git clone https://github.com/yourusername/ejs-ssti-shell-spawner.git
cd ejs-ssti-shell-spawner
pip install .
```

---

## 🚀 Usage

```bash
ejs-ssti-shell-spawner
```

You will be prompted for the following inputs:

* **LHOST**: Your IP address to receive the reverse shell
* **LPORT**: Port to listen on (must be open)
* **RHOST**: Target server (e.g., `vulnerable.site`)
* **Path**: Path to the vulnerable endpoint (e.g., `/settings`)
* **POST Data**: Key-value pairs required by the target (e.g., `name=test&password=test`)
* **Session Cookie**: Authenticated cookie string (e.g., `connect.sid=xyz`)

Once provided, the script will:

1. Start a netcat listener on your LPORT
2. Craft and send the EJS SSTI payload via `escapeFunction`
3. Wait for a reverse shell connection from the vulnerable target

---

## ⚠️ CVE Details

* **CVE ID**: [CVE-2023-29827](https://nvd.nist.gov/vuln/detail/CVE-2023-29827)
* **Package**: `ejs@3.1.9`
* **Vulnerability Type**: Server-Side Template Injection (SSTI)
* **Vector**: Untrusted `escapeFunction` parameter in EJS templates
* **Impact**: Remote Code Execution (RCE)
* **Patched Version**: `ejs@3.1.10`

---

## 🔧 Requirements

* Python 3.6+
* `requests` Python module
* `nc` (netcat) installed on your machine

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧪 Tested On

* Kali Linux 2023.1
* Python 3.10
* Netcat (traditional)
* Local EJS-lab running in Docker

---

## 🙋 Author

**Md. Momrul Hasan**
Cybersecurity Enthusiast | Red Teamer | Exploit Developer
🔗 [GitHub](https://github.com/momrulhasan)
🔗 [LinkedIn](https://linkedin.com/in/momrulhasan)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 💥 Disclaimer

This tool is for **educational and authorized testing purposes only**.
Any misuse of this code is not the responsibility of the author. Always get proper authorization before testing.

```
```
