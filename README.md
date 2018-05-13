# ACTCORP AUTO-LOGIN SCRIPT
This script can be use to setup auto-login on the ACT Corp network
without having the need to going to the redirect page entering password
and again. The script ensures that when the user gets logged out of the 
network they get automatically logged in 1 second (easily modifiable interval).

## Requirements
1. Python3
2. Other dependencies as listed in `requirements.txt`.

## Installation
Download the script using git/other means. 

### 1. Setup dependencies
Run the following command for setting dependencies in place:
```bash
pip install -r requirements.txt
```

### 2. Update username and password
Update the USERNAME and PASSWORD variables in `autologin_actcorp.py` file.

```python
USERNAME = '<username>'
PASSWORD = '<password>'
```

### 3. Run the script.

Run the script as a demon process.

```bash
python3 autologin_actcorp.py &
```

### 4. Optional set it up for autostart on login

[AutoStart on login(Ubuntu)](https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu)

