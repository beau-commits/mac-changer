import subprocess
import re
import random

def get_mac(interface):
    """
    Retrieve the MAC address of the given network interface.

    Args:
        interface (str): The name of the network interface.

    Returns:
        str or None: The MAC address in string format if found, else None.
    """
    result = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
    match = re.search(r"link/ether ([\da-fA-F:]{17})", result.stdout)
    return match.group(1) if match else None

def generate_mac():
    """
    Generate a random, locally administered, unicast MAC address.

    Returns:
        str: The generated MAC address in standard colon-separated format.
    """
    mac = [0x02, 0x00, 0x00,  # Locally administered, unicast
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(f"{b:02x}" for b in mac)

def change_mac(interface, new_mac):
    """
    Change the MAC address of the specified network interface.

    Args:
        interface (str): The network interface name.
        new_mac (str): The new MAC address to set.

    Returns:
        None
    """
    try:
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"], check=True)
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac], check=True)
        subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error changing MAC address: {e}")

def get_interface_name():
    """
    Detect the name of the first active, non-loopback network interface.

    Returns:
        str or None: The name of the active interface, or None if not found.
    """
    result = subprocess.run(["ip", "link"], capture_output=True, text=True)
    interfaces = re.findall(r'^\d+: ([^:]+): <([^>]+)>', result.stdout, re.MULTILINE)
    
    for iface, flags in interfaces:
        flags_set = set(flags.split(','))
        if iface != "lo" and "UP" in flags_set:
            return iface
    return None

def main():
    """
    Main execution function that retrieves the interface,
    displays the current MAC address, generates a new MAC,
    applies it, and shows the result.
    """
    interface = get_interface_name()
    print(f"Your interface name is: {interface}")
    
    current_mac = get_mac(interface)
    if not current_mac:
        print(f"Could not read MAC address for interface {interface}")
        return

    print(f"Current MAC: {current_mac}")
    new_mac = generate_mac()
    print(f"Changing MAC to: {new_mac}...")
    
    change_mac(interface, new_mac)

    updated_mac = get_mac(interface)
    print(f"New MAC: {updated_mac}")
    print("Thank you for using this service")

if __name__ == "__main__":
    main()

