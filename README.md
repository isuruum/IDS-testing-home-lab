# Network Anomaly Detection Testing Suite

![Status](https://img.shields.io/badge/Status-Educational-blue) ![Python](https://img.shields.io/badge/Python-3.x-yellow)

> [!CAUTION]
> **Advises about risks or negative outcomes of certain actions.**
>
> This repository contains scripts designed **strictly for educational purposes and internal systems testing**. The tools provided here are intended to generate high-volume network traffic patterns to validate the performance of Intrusion Detection Systems (IDS).
>
> **Do not** use these scripts against networks, servers, or devices you do not own or have explicit written permission to test. The author claims no responsibility for misuse or damage caused by these tools.

---

## 📖 Overview

This project provides a collection of Python scripts developed to simulate various network conditions within a controlled Virtual Machine (VM) lab environment. The primary goal is to trigger specific alerts in a custom-built Anomaly Detection System (ADS) to verify:

1.  **Traffic Volumetric Analysis:** Detecting sudden spikes in packet volume.
2.  **Multi-Port Correlation:** Detecting concurrent traffic anomalies across multiple services.
3.  **Payload Variance:** Handling varying packet sizes and fragmentation.

## 🚀 Getting Started

### Prerequisites

* **OS:** Linux (Kali Linux / Ubuntu recommended) or Windows
* **Python:** Version 3.6+
* **Network:** An isolated Virtual Lab (e.g., VirtualBox NAT Network or Host-Only Adapter)

### Installation

1.  Ensure Python 3 is installed on your system.
2.  (Optional) Create and activate a virtual environment to keep your system clean:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### Usage

Navigate to the project directory and run any script with Python 3:

```bash
python3 <script_name>.py
```

> **Note:** Scripts using Scapy (`ids_trigger_v1.py`, `ids_trigger_v2.py`, `multiproto_anomaly.py`, `packet_size_anomaly.py`) require **root/sudo** privileges to craft raw packets.

---

## 📂 Scripts

| File | Description |
|---|---|
| `udp_flood_basic.py` | Basic UDP flood with hardcoded target IP, port, and duration. Sends 4000-byte payloads continuously. |
| `udp_flood_multiport.py` | Interactive UDP flood. Prompts for IP, multiple ports, packet size, and duration. |
| `ids_trigger_v1.py` | Scapy IDS trigger menu with **low thresholds** (High Traffic: >200 pkts, DoS: >500 pkts). Includes port scan, restricted ports, and ML anomaly tests. |
| `ids_trigger_v2.py` | Scapy IDS trigger menu with **high thresholds** (High Traffic: >1500 pkts, DoS: >2500 pkts). Same test scenarios as v1. |
| `multiproto_anomaly.py` | Multi-protocol flood tester supporting ICMP, TCP, UDP, HTTP, HTTPS, and IGMP with configurable duration and packet limit. |
| `packet_size_anomaly.py` | Packet size and MTU fragmentation tester. Sends custom-sized payloads to stress-test IDS buffer handling and fragmentation detection. |
