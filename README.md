# rbx-user-checker

A simple tool to check the availability of Roblox usernames in bulk.

## Features

- Bulk username availability checking
- Proxy support for rate limiting protection
- Organized input/output file structure
- Automatic filtering of available usernames

## Setup

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Add usernames to check:**
   - Open `input/usernames.txt`
   - Add one username per line

2. **Configure proxy (optional but recommended):**
   - Open `main.py`
   - Add your proxy configuration in the designated section

3. **Run the checker:**
   ```bash
   python main.py
   ```

4. **Check results:**
   - Available usernames will be saved to `output/untaken.txt`
   - One available username per line

## File Structure

```
rbx-user-checker/
├── input/
│   └── usernames.txt      # Input file - add usernames here
├── output/
│   └── untaken.txt        # Output file - available usernames
├── main.py                # Main script
└── README.md             # This file
```

## Notes

- Using a proxy is recommended to avoid rate limiting
- The tool respects Roblox's API limitations
- Large batches may take time to process

## Disclaimer

This tool is for educational purposes only. Please respect Roblox's Terms of Service and API usage guidelines.
