# ACTCORP AUTO-LOGIN SCRIPT
This script can be use to setup auto-login on the ACT Corp network
without having the need to going to the redirect page entering password
and again. The script ensures that when the user gets logged out of the 
network they get automatically logged in 5 second (easily modifiable interval).

## The easy way out
If your router is supported you should go for the easy solution:
1. Go to your routers login page.
2. Set Internet Connection Type to PPPoE.
3. Enter username and password and you're done.

If you are one of the unlucky one's for which this doesn't work use the
below scripts.

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

if you are trying to use this outside of hyd circle you might need to update
the REDIRECT_ADDRESS address.
```python
REDIRECT_ADDRESS = '<redirect server>'
```

### 3. Run the script.

Run the script as a demon process.

```bash
python3 autologin_actcorp.py &
```

### 4. Optional set it up for autostart on login

[AutoStart on login(Ubuntu)](https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu)

