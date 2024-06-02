Sure! Here's a detailed README file for your project:

```markdown
# Basic Network Scanner

The Basic Network Scanner is a Python script designed to scan a specified network range for open ports. It leverages multi-threading for efficient scanning and provides real-time control to stop the scan by pressing 'x' on the keyboard.

## Features

- **Network Range Scanning**: Scans all IP addresses within a given network range.
- **Port Scanning**: Checks multiple ports (1-1024 by default) on each IP address for open connections.
- **Multi-threading**: Uses threading to speed up the scanning process.
- **Real-time Control**: Allows the user to interrupt and stop the scan at any time by pressing 'x'.
- **User-Friendly Input**: Prompts the user to input the network range to scan.

## Requirements

- Python 3.x
- `keyboard` library

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/basic_network_scanner.git
   cd basic_network_scanner
   ```

2. **Install the required library**:
   ```sh
   pip install keyboard
   ```

## Usage

1. **Run the script**:
   ```sh
   python network_scanner.py
   ```

2. **Enter the network range**:
   - When prompted, enter the network range to scan (e.g., `192.168.1.0/24`).

3. **Monitor the output**:
   - The script will display open ports as it scans.

4. **Stop the scan**:
   - Press 'x' at any time to stop the scan gracefully.

## Example

```sh
$ python network_scanner.py
Enter the network to scan (e.g., 192.168.1.0/24): 192.168.1.0/24
Press 'x' to stop the scan.
Scanning 192.168.1.0...
Port 22 is open on 192.168.1.1
Port 80 is open on 192.168.1.1
...
```

## Contributing

Feel free to submit issues or pull requests if you have any improvements or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

This README file includes sections for the project description, features, requirements, installation steps, usage instructions, an example session, contributing guidelines, and the license. Adjust the repository URL and any other details as needed.