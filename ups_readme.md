# UPS - Udeesh Port Scanner 🔍

<div align="center">

```
╦ ╦╔═╗╔═╗
║ ║╠═╝╚═╗
╚═╝╩  ╚═╝

🔍 UDEESH PORT SCANNER v1.0 🔍
```

**A powerful, multi-threaded port scanner for ethical hacking and cybersecurity professionals**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/yourusername/UPS)

</div>

## 🚀 Features

- **🎯 Multi-threaded Scanning** - Fast and efficient port discovery
- **🖥️ Interactive Mode** - User-friendly guided interface  
- **⚡ CLI Mode** - Direct command-line operation
- **🌐 Hostname Resolution** - Automatic DNS resolution support
- **🔧 Flexible Port Options** - Range, specific ports, or common ports
- **📊 Service Detection** - Identifies services running on open ports
- **🎨 Clean Interface** - Color-coded output with ASCII art
- **⚠️ Ethical Focus** - Built for legitimate security testing

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Interactive Mode](#interactive-mode)
  - [CLI Mode](#cli-mode)
- [Examples](#examples)
- [Features](#features-detailed)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Legal Disclaimer](#legal-disclaimer)
- [License](#license)

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required (uses built-in libraries)

### Clone the Repository
```bash
git clone https://github.com/yourusername/UPS.git
cd UPS
chmod +x ups.py
```

### Quick Start
```bash
python3 ups.py
```

## 🎮 Usage

### Interactive Mode
Simply run the script without arguments to enter interactive mode:

```bash
python3 ups.py
```

This will display the UPS banner and present you with scanning options:

1. **Quick Scan** - Scans common ports (1-1024)
2. **Full Port Range Scan** - Comprehensive scan (1-65535)
3. **Custom Port Range** - Define your own range
4. **Specific Ports Only** - Target specific ports
5. **Show Help & Examples** - View detailed usage guide
6. **Exit** - Quit the application

### CLI Mode
For direct command-line usage:

```bash
python3 ups.py [TARGET] [OPTIONS]
```

#### Parameters
| Parameter | Description | Default |
|-----------|-------------|---------|
| `TARGET` | IP address or hostname to scan | Required |
| `-p, --ports` | Port specification (range/list) | 1-1024 |
| `-t, --threads` | Number of scanning threads | 100 |
| `--timeout` | Connection timeout (seconds) | 1 |
| `--common-ports` | Scan only common service ports | False |
| `-h, --help` | Show help message | - |

## 💡 Examples

### Basic Scans
```bash
# Quick scan of common ports
python3 ups.py 192.168.1.1

# Scan specific website
python3 ups.py google.com --common-ports
```

### Advanced Scans
```bash
# Custom port range with more threads
python3 ups.py 10.0.0.1 -p 1-5000 -t 300

# Specific ports only
python3 ups.py server.com -p 22,80,443,8080

# Fast scan with reduced timeout
python3 ups.py target.com -p 1-1000 --timeout 0.5 -t 500
```

### Real-World Scenarios
```bash
# Web server assessment
python3 ups.py webserver.com -p 80,443,8080,8443

# Database server check
python3 ups.py db.local -p 3306,5432,1433,27017

# Full network discovery
python3 ups.py 192.168.1.0/24 -p 1-65535 -t 1000
```

## 🔧 Features Detailed

### Multi-threading
- **Concurrent Scanning**: Uses threading for parallel port checks
- **Configurable Threads**: Adjust thread count based on system capabilities
- **Thread Safety**: Proper locking mechanisms for result collection

### Port Specification Flexibility
- **Port Ranges**: `1-1000`, `80-443`
- **Specific Ports**: `22,80,443,8080`
- **Common Ports**: Predefined list of standard service ports
- **Full Range**: Complete port spectrum (1-65535)

### Smart Hostname Resolution
- **DNS Resolution**: Automatic hostname to IP conversion
- **IPv4 Support**: Full IPv4 address range support
- **Error Handling**: Graceful handling of resolution failures

### Service Detection
- **Service Identification**: Maps open ports to known services
- **Protocol Recognition**: TCP service discovery
- **Unknown Services**: Handles custom/unknown service ports

## 📸 Screenshots

### Interactive Mode
```
╦ ╦╔═╗╔═╗
║ ║╠═╝╚═╗
╚═╝╩  ╚═╝

🔍 UDEESH PORT SCANNER v1.0 🔍
Created by: Udeesh
Ethical Hacking & Cybersecurity Tool

🚀 INTERACTIVE MODE
══════════════════════════════════════════════════

Select an option:
1. Quick Scan (Common Ports)
2. Full Port Range Scan (1-65535)
3. Custom Port Range
4. Specific Ports Only
5. Show Help & Examples
6. Exit
```

### Scan Results
```
Target: scanme.nmap.org
Port Range: 1-1024
Threads: 100
Scan started at: 2024-12-20 15:30:45
══════════════════════════════════════════════════

[+] Port 22: Open (ssh)
[+] Port 80: Open (http)
[+] Port 443: Open (https)
[+] Port 9929: Open

══════════════════════════════════════════════════
SCAN COMPLETE
══════════════════════════════════════════════════
Found 4 open ports:
  22/tcp - ssh
  80/tcp - http
  443/tcp - https
  9929/tcp - unknown
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution
- [ ] UDP port scanning support
- [ ] Output formats (JSON, XML, CSV)
- [ ] OS fingerprinting
- [ ] Banner grabbing
- [ ] Stealth scanning techniques
- [ ] IPv6 support

## ⚖️ Legal Disclaimer

**IMPORTANT**: This tool is designed for **educational purposes** and **authorized security testing only**.

### Ethical Usage Guidelines
- ✅ **DO**: Use on your own networks and systems
- ✅ **DO**: Use for authorized penetration testing
- ✅ **DO**: Use for educational and research purposes
- ❌ **DON'T**: Scan networks without explicit permission
- ❌ **DON'T**: Use for malicious activities
- ❌ **DON'T**: Violate any local, state, or federal laws

### Responsibility
The author (Udeesh) is not responsible for any misuse of this tool. Users are solely responsible for ensuring their usage complies with all applicable laws and regulations.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Udeesh**
- 🔗 Cybersecurity Enthusiast
- 🎓 Ethical Hacking Student
- 🛡️ AI & Security Tools Developer

## 🙏 Acknowledgments

- Thanks to the cybersecurity community for inspiration
- Built for educational and ethical purposes
- Inspired by tools like Nmap and Masscan

## 📞 Support

If you encounter any issues or have questions:
- 🐛 [Report Issues](https://github.com/Udeesh-Dinnipati/UPS/issues)
- 💬 [Discussions](https://github.com/Udeesh-Dinnipati/UPS/discussions)
- ⭐ Star this repo if you find it useful!

---

<div align="center">

**Made with ❤️ by Udeesh for the cybersecurity community**

*Remember: With great power comes great responsibility. Use ethically! 🛡️*

</div>