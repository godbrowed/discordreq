# Discord Invite Spammer

A Python script that automates sending invite requests to a Discord server and handles different response scenarios.

## Features
- Sends repeated invite requests to a specified Discord invite link
- Handles errors such as invalid/expired invites, full channels, and other rejections
- Implements a delay between requests to prevent rate limiting

## Requirements
- Python 3.8+
- Required Python libraries:
  ```sh
  pip install requests
  ```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/godbrowed/Discord_Invite_Spammer.git
   cd Discord_Invite_Spammer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure the script by updating the `url` variable with your target invite link.

## Usage
- Run the script:
  ```sh
  python invite_spammer.py
  ```
- The script will continuously send requests and print the status of each attempt.

## Deployment
You can deploy the script on a VPS for continuous execution:
```sh
nohup python invite_spammer.py &
```

## Author
[GodBrowed](https://github.com/godbrowed)

