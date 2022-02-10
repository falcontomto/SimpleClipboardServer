# SimpleClipboardServer

## Description
This is a simple HTTP server for receiving text to clipboard.
I made this to share OTPs from my iPhone.
Use the iOS shortcut below to quickly send text to the clipboard of a PC.

## Requirement
- Python 3 or above

## Setup
- Open `cmd` and `ipconfig` to find your local IP address
- Change `hostName` in ClipboardServer.py (line 9) to the IP address you just found and save
- Run the script

## Usage
Get the iOS shortcut here: https://www.icloud.com/shortcuts/cd5db9787ca44f1889e69cc116ab731e
Share the text using the provided shortcut to send it to the server's clipboard.

Alternatively, you can also make a GET request to the URL `http://{hostName}:4646/clipboard/{urlEncodedText}` to achieve the same.
