
#!/usr/bin/env python3
import os
import time
from modules.network_monitor import monitor_network
from modules.ai_threat_detector import analyze_traffic
from modules.tor_vpn_handler import ensure_anonymity
from modules.alert_system import send_alert
from modules.file_integrity import check_integrity

def main():
    print("[*] Starting LuciGuard Sentinel AI...")
    ensure_anonymity()
    while True:
        threats = analyze_traffic()
        if threats:
            send_alert(threats)
        monitor_network()
        check_integrity()
        time.sleep(5)

if __name__ == "__main__":
    main()
