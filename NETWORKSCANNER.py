import tkinter as tk
from tkinter import messagebox
import socket
import threading

def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports

def scan_network():
    ip_address = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    open_ports = scan_ports(ip_address, start_port, end_port)

    messagebox.showinfo("Scan Complete", f"Open ports: {open_ports}")

def start_scan():
    thread = threading.Thread(target=scan_network)
    thread.start()

# Create GUI window
window = tk.Tk()
window.title("Network Port Scanner")

# IP Address Label and Entry
label_ip = tk.Label(window, text="IP Address:")
label_ip.pack()
entry_ip = tk.Entry(window)
entry_ip.pack()

# Start Port Label and Entry
label_start_port = tk.Label(window, text="Start Port:")
label_start_port.pack()
entry_start_port = tk.Entry(window)
entry_start_port.pack()

# End Port Label and Entry
label_end_port = tk.Label(window, text="End Port:")
label_end_port.pack()
entry_end_port = tk.Entry(window)
entry_end_port.pack()

# Start Scan Button
button_scan = tk.Button(window, text="Start Scan", command=start_scan)
button_scan.pack()

# Run the GUI window
window.mainloop()
