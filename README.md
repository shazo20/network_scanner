# 📡 Network Port Scanner (Python)

## Overview

This project is a lightweight **multi-threaded network port scanner** written in Python.
It scans a given **CIDR subnet** and checks whether a specific port is open on each host.

The tool is designed for learning purposes in:

* Network programming
* Socket programming
* Multithreading
* Basic network reconnaissance

---

## ⚙️ Features

* CIDR subnet input support (e.g. `192.168.1.0/24`)
* Multi-threaded scanning using `ThreadPoolExecutor`
* Fast TCP port checking using `socket.connect_ex`
* Thread-safe result storage using `Lock`
* Colored terminal output for better readability
* Lightweight and dependency minimal

---

## 🧠 How It Works

1. User provides a subnet in CIDR format
2. The subnet is expanded into individual IP addresses
3. Each IP is scanned concurrently using threads
4. A TCP connection attempt is made to the target port
5. Results are categorized as:

   * OPEN (reachable on port)
   * CLOSED (not reachable)
6. All reachable IPs are stored in a shared list safely using thread locking

---

## 📥 Requirements

Install dependencies:

```bash
pip install colorama
```

Built-in modules used:

* `socket`
* `ipaddress`
* `threading`
* `concurrent.futures`

---

## 🚀 Usage

Run the script:

```bash
python scanner.py
```

### Input example:

```text
Please enter ip and subnet in this format (192.168.1.0/24): 192.168.1.0/24
Please enter port: 80
```

---

## 📤 Output Example

```text
Ip: 192.168.1.10 is available on port: 80
Ip: 192.168.1.11 is not available on port: 80
Ip: 192.168.1.15 is available on port: 80

Available ips: ['192.168.1.10', '192.168.1.15']
```

---

## 🧩 Technical Details

### Networking Layer

* Uses TCP sockets (`SOCK_STREAM`)
* Connection test via `connect_ex()`

### Concurrency Model

* Thread pool with max 100 workers
* Parallel scanning of IP range for performance improvement

### Thread Safety

* Shared resource (`available_ips`) protected using `Lock`

---

## ⚠️ Limitations

* No UDP scanning support
* No service fingerprinting
* No stealth scanning (SYN scan not implemented)
* Performance depends on network latency
* May trigger security alerts on monitored networks

---

## 🧭 Future Improvements

* Async IO implementation (faster scanning)
* Service detection (banner grabbing)
* Multi-port scanning
* Export results to JSON/CSV
* CLI argument support (`argparse`)
* Integration with subnet auto-detection tools

---

## 📚 Educational Purpose

This project is intended for:

* Learning socket programming
* Understanding network scanning concepts
* Practicing multithreading in Python
* Building foundation for tools similar to Nmap

---

## 👨‍💻 Disclaimer

This tool is for **educational and authorized testing only**.
Do not use it on networks you do not own or have permission to scan.

