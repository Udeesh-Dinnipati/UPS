#!/usr/bin/env python3
"""
UPS - Udeesh Port Scanner
A CLI tool for scanning open ports on target IP addresses
Author: Udeesh
"""

import socket
import sys
import threading
import argparse
from datetime import datetime
import ipaddress

class PortScanner:
    def __init__(self, target, start_port=1, end_port=1024, threads=100, timeout=1):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()
        
    def scan_port(self, port):
        """Scan a single port on the target"""
        try:
            # Create socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Attempt to connect
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    try:
                        service = socket.getservbyport(port)
                        print(f"[+] Port {port}: Open ({service})")
                    except:
                        print(f"[+] Port {port}: Open")
            
            sock.close()
            
        except socket.gaierror:
            # Could not resolve hostname
            pass
        except Exception as e:
            # Other exceptions
            pass
    
    def display_banner(self):
        """Display the UPS banner"""
        banner = """
╦ ╦╔═╗╔═╗
║ ║╠═╝╚═╗
╚═╝╩  ╚═╝
        
 █    █ ██████  █████ █████  █   █      
 █    █ █     █ █     █      █   █      
 █    █ █     █ █████ █████  █████      
 █    █ █     █ █     █      █   █      
 ██████ ██████  █████ █████  █   █      
                                        
██████   ██████  ██████  ████████       
█     █ █     █ █     █    █     █      
█     █ █     █ █     █    █     █      
██████  █     █ ██████     █     █      
█       █     █ █   █      █     █      
█       ██████  █    █     █     █      
                                        
 █████   █████   █████  █   █ █   █ █████ ██████ 
█       █       █     █ ██  █ ██  █ █     █     █
█████   █       █████ █ █ █ █ █ █ █ █████ ██████ 
    █   █       █     █ █  ██ █  ██ █     █   █  
█████   █████   █     █ █   █ █   █ █████ █    █ 

         🔍 UDEESH PORT SCANNER v1.0 🔍
              Created by: Udeesh
           Ethical Hacking & Cybersecurity Tool
        """
        
        print("\033[96m" + banner + "\033[0m")  # Cyan color
        print("=" * 70)
    
    def worker(self, port_queue):
        """Worker thread function"""
        while True:
            try:
                port = port_queue.pop(0)
                self.scan_port(port)
            except IndexError:
                break
    
    def scan(self):
        """Main scanning function"""
        self.display_banner()
        print(f"Target: {self.target}")
        print(f"Port Range: {self.start_port}-{self.end_port}")
        print(f"Threads: {self.threads}")
        print(f"Timeout: {self.timeout}s")
        print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*70}\n")
        
        # Create port queue
        port_queue = list(range(self.start_port, self.end_port + 1))
        
        # Create and start threads
        threads = []
        for _ in range(min(self.threads, len(port_queue))):
            t = threading.Thread(target=self.worker, args=(port_queue,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Wait for all threads to complete
        for t in threads:
            t.join()
        
        # Display results
        print(f"\n{'='*70}")
        print(f"SCAN COMPLETE")
        print(f"{'='*70}")
        
        if self.open_ports:
            self.open_ports.sort()
            print(f"Found {len(self.open_ports)} open ports:")
            for port in self.open_ports:
                try:
                    service = socket.getservbyport(port)
                    print(f"  {port}/tcp - {service}")
                except:
                    print(f"  {port}/tcp - unknown")
        else:
            print("No open ports found in the specified range.")
        
        print(f"\nScan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def validate_ip(ip_string):
    """Validate IP address format"""
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

def resolve_hostname(hostname):
    """Resolve hostname to IP address"""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def display_help_menu():
    """Display help menu and usage instructions"""
    help_text = """
\033[93m📋 UPS COMMAND REFERENCE & EXAMPLES\033[0m
═══════════════════════════════════════════════════════════════════

\033[92m🎯 BASIC USAGE:\033[0m
   python3 ups.py [TARGET] [OPTIONS]

\033[92m🔧 PARAMETERS:\033[0m
   TARGET          - IP address or hostname to scan
   -p, --ports     - Port specification (default: 1-1024)
   -t, --threads   - Number of threads (default: 100)
   --timeout       - Connection timeout in seconds (default: 1)
   --common-ports  - Scan only common service ports
   -h, --help      - Show detailed help menu

\033[92m💡 EXAMPLES:\033[0m
   🏠 Local Network Scan:
      python3 ups.py 192.168.1.1
      python3 ups.py 10.0.0.1 -p 1-1000 -t 200

   🌐 Internet Targets:
      python3 ups.py google.com --common-ports
      python3 ups.py scanme.nmap.org -p 80,443,22,21

   ⚡ Fast Scans:
      python3 ups.py target.com -p 1-65535 -t 500 --timeout 0.5

   🎯 Specific Services:
      python3 ups.py server.com -p 80,443,8080,8443
      python3 ups.py database.local -p 3306,5432,1433

\033[91m⚠️  ETHICAL USAGE REMINDER:\033[0m
   • Only scan networks/systems you own or have permission to test
   • Use for legitimate security testing and education only
   • Respect rate limits and don't overload target systems

═══════════════════════════════════════════════════════════════════
"""
    print(help_text)

def interactive_mode():
    """Interactive mode for user-friendly operation"""
    print("\n\033[96m🚀 INTERACTIVE MODE\033[0m")
    print("═" * 50)
    
    while True:
        print("\n\033[93mSelect an option:\033[0m")
        print("1. Quick Scan (Common Ports)")
        print("2. Full Port Range Scan (1-65535)")
        print("3. Custom Port Range")
        print("4. Specific Ports Only")
        print("5. Show Help & Examples")
        print("6. Exit")
        
        try:
            choice = input("\n\033[96mEnter your choice (1-6):\033[0m ").strip()
            
            if choice == "6":
                print("\n\033[92m👋 Thanks for using UPS! Stay ethical! 🛡️\033[0m")
                sys.exit(0)
            elif choice == "5":
                display_help_menu()
                continue
            elif choice not in ["1", "2", "3", "4"]:
                print("\033[91m❌ Invalid choice. Please select 1-6.\033[0m")
                continue
            
            # Get target
            target = input("\n\033[93mEnter target IP/hostname:\033[0m ").strip()
            if not target:
                print("\033[91m❌ Target cannot be empty!\033[0m")
                continue
            
            # Resolve target
            target_ip = target
            if not validate_ip(target):
                print(f"\033[94m[*] Resolving hostname: {target}\033[0m")
                target_ip = resolve_hostname(target)
                if not target_ip:
                    print(f"\033[91m[-] Error: Could not resolve hostname '{target}'\033[0m")
                    continue
                print(f"\033[94m[*] Resolved to: {target_ip}\033[0m")
            
            # Configure scan based on choice
            if choice == "1":  # Quick scan
                start_port = 1
                end_port = 1024
                threads = 100
            elif choice == "2":  # Full scan
                start_port = 1
                end_port = 65535
                threads = 500
                print("\033[93m⚠️  Full port scan may take several minutes!\033[0m")
            elif choice == "3":  # Custom range
                try:
                    port_range = input("\033[93mEnter port range (e.g., 1-1000):\033[0m ").strip()
                    start_port, end_port = map(int, port_range.split('-'))
                    threads = int(input("\033[93mEnter number of threads (default 100):\033[0m ").strip() or "100")
                except ValueError:
                    print("\033[91m❌ Invalid port range format!\033[0m")
                    continue
            elif choice == "4":  # Specific ports
                try:
                    ports_input = input("\033[93mEnter ports (e.g., 80,443,22,21):\033[0m ").strip()
                    ports = [int(p.strip()) for p in ports_input.split(',')]
                    start_port = min(ports)
                    end_port = max(ports)
                    threads = 50
                except ValueError:
                    print("\033[91m❌ Invalid ports format!\033[0m")
                    continue
            
            # Validate ports
            if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
                print("\033[91m❌ Port numbers must be between 1 and 65535!\033[0m")
                continue
            
            if start_port > end_port:
                print("\033[91m❌ Start port must be less than or equal to end port!\033[0m")
                continue
            
            # Run scan
            print(f"\n\033[92m🎯 Starting scan on {target_ip}...\033[0m")
            scanner = PortScanner(target_ip, start_port, end_port, threads, 1)
            scanner.scan()
            
            # Ask if user wants to continue
            cont = input("\n\033[93mWould you like to perform another scan? (y/n):\033[0m ").strip().lower()
            if cont != 'y' and cont != 'yes':
                print("\n\033[92m👋 Thanks for using UPS! Stay ethical! 🛡️\033[0m")
                break
                
        except KeyboardInterrupt:
            print("\n\n\033[91m[-] Scan interrupted by user\033[0m")
            sys.exit(1)
        except Exception as e:
            print(f"\033[91m[-] Error: {e}\033[0m")

def main():
    # Check if arguments provided
    if len(sys.argv) == 1:
        # No arguments - show banner and run interactive mode
        banner = """
╦ ╦╔═╗╔═╗
║ ║╠═╝╚═╗
╚═╝╩  ╚═╝
        
 █    █ ██████   █████ █████  █████   █   █      
 █    █ █     █  █     █      █       █   █      
 █    █ █     █  █████ █████  █████   █████      
 █    █ █     █  █     █          █   █   █      
 ██████ ██████   █████ █████  █████   █   █      
                                        
██████   ██████  ██████  ███████       
█     █ █     █ █     █     █           
█     █ █     █ █     █     █           
██████  █     █ ██████      █           
█       █     █ █   █       █           
█       ██████  █    █      █           
                                        
 █████   █████   █████  █   █ █   █ █████ ██████ 
█       █       █     █ ██  █ ██  █ █     █     █
█████   █       ███████ █ █ █ █ █ █ █████ ██████ 
    █   █       █     █ █  ██ █  ██ █     █   █  
█████   ██████  █     █ █   █ █   █ █████ █    █ 

         🔍 UDEESH PORT SCANNER v1.1 🔍
              Created by: Udeesh
           Ethical Hacking & Cybersecurity Tool
        """
        
        print("\033[96m" + banner + "\033[0m")  # Cyan color
        print("=" * 70)
        
        interactive_mode()
        return
    
    # Command line arguments provided - use CLI mode
    parser = argparse.ArgumentParser(
        description="UPS - Udeesh Port Scanner | Scan for open ports on target systems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 ups.py 192.168.1.1
  python3 ups.py google.com -p 1-1000 -t 200
  python3 ups.py 10.0.0.1 -p 80,443,8080 -t 50
  python3 ups.py scanme.nmap.org --common-ports

Created by Udeesh - Ethical Hacking & Cybersecurity
        """
    )
    
    parser.add_argument('target', help='Target IP address or hostname')
    parser.add_argument('-p', '--ports', default='1-1024', 
                       help='Port range (e.g., 1-1000, 80,443,8080) or single port')
    parser.add_argument('-t', '--threads', type=int, default=100,
                       help='Number of threads (default: 100)')
    parser.add_argument('--timeout', type=float, default=1,
                       help='Connection timeout in seconds (default: 1)')
    parser.add_argument('--common-ports', action='store_true',
                       help='Scan common ports only')
    
    args = parser.parse_args()
    
    # Resolve target
    target_ip = args.target
    if not validate_ip(args.target):
        print(f"[*] Resolving hostname: {args.target}")
        target_ip = resolve_hostname(args.target)
        if not target_ip:
            print(f"[-] Error: Could not resolve hostname '{args.target}'")
            sys.exit(1)
        print(f"[*] Resolved to: {target_ip}")
    
    # Parse port specification
    if args.common_ports:
        # Common ports list
        ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]
        start_port = min(ports)
        end_port = max(ports)
    else:
        try:
            if ',' in args.ports:
                # Multiple specific ports
                ports = [int(p.strip()) for p in args.ports.split(',')]
                start_port = min(ports)
                end_port = max(ports)
            elif '-' in args.ports:
                # Port range
                start_port, end_port = map(int, args.ports.split('-'))
            else:
                # Single port
                start_port = end_port = int(args.ports)
        except ValueError:
            print("[-] Error: Invalid port specification")
            sys.exit(1)
    
    # Validate port range
    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
        print("[-] Error: Port numbers must be between 1 and 65535")
        sys.exit(1)
    
    if start_port > end_port:
        print("[-] Error: Start port must be less than or equal to end port")
        sys.exit(1)
    
    # Create and run scanner
    try:
        scanner = PortScanner(target_ip, start_port, end_port, args.threads, args.timeout)
        scanner.scan()
    except KeyboardInterrupt:
        print("\n[-] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error during scan: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()