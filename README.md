# mac-changer

A simple Python script to change the MAC address of your active network interface on Linux systems.

## Features

- Automatically detects the first active non-loopback network interface.
- Retrieves and displays the current MAC address.
- Generates a random, locally administered, unicast MAC address.
- Changes the MAC address using ip commands (requires sudo).
- Displays the new MAC address after the change.

## Requirements

- Python 3.x
- Linux system with ip command available (iproute2 package)
- sudo privileges to change network settings

## Usage

Clone the repository:


    git clone https://github.com/your-username/mac-changer.git
    cd mac-changer

Run the script with sudo:

    sudo python3 change_mac.py

## The script will:

  Detect your active network interface.

  Show the current MAC address.

  Generate and apply a new random MAC address.

  Confirm the change by displaying the new MAC address.


## How it works

  The script uses subprocess to run ip commands and regular expressions to parse MAC addresses.

  It generates a MAC address that is locally administered and unicast, ensuring it’s valid and doesn’t conflict       with manufacturer-assigned addresses.

  The network interface is temporarily brought down before changing the MAC, then brought back up.

## Notes

  This script requires administrative privileges; hence, use sudo.

  Changing your MAC address can disrupt active network connections temporarily.

  Test responsibly and only on interfaces you control.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Beau-commits

## Example Output:

    Your interface name is: eth0
    Current MAC: 00:1a:2b:3c:4d:5e
    Changing MAC to: 02:00:00:3a:7f:1b...
    New MAC: 02:00:00:3a:7f:1b
    Thank you for using this service
