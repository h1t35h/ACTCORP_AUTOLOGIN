from bs4 import BeautifulSoup
import requests
import logging
import urllib3
from time import sleep

REDIRECT_ADDRESS = "http://portal.actcorp.in/web/hyd/home"
USERNAME = '<username>'
PASSWORD = '<password>'
HTTP = urllib3.PoolManager()


def post_login_request():
    """
Creates and sends the authentication requests for login
    """

    # login_url of the default redirection page
    get_request = requests.get(REDIRECT_ADDRESS)

    parsed_html = BeautifulSoup(get_request.text, 'html.parser')
    login_form = parsed_html.find('div', {'class': 'login'}).find_parent('form')

    login_url = login_form.get('action')
    user_ip = login_form.find('input', {'name': 'userIP'}).get('value')

    print("Login Url:", login_url)
    print("User IP: ", user_ip)

    # This corresponds to username,password at the time of writing this
    username_payload_key = '_login_WAR_BeamPromotionalNDownloadsportlet_uname'  # stupid though :/
    password_payload_key = 'pword'
    user_ip_payload_key = 'userIP'

    # Dynamically update the payload_keys. still not sure if it's fully reliable
    for input_element in login_form.findAll('input'):
        if input_element.get('type') == 'password':
            password_payload_key = input_element.get('name')
        if input_element.get('type') == 'text':
            username_payload_key = input_element.get('name')

    payload = {
        user_ip_payload_key: user_ip,
        username_payload_key: USERNAME,
        password_payload_key: PASSWORD
    }

    post_request = requests.post(login_url, data=payload)
    return post_request.status_code


def is_logged_in(hostname):
    try:
        get_redirect_page = requests.get(hostname)
        parsed_html = BeautifulSoup(get_redirect_page.text, 'html.parser')
        logged_in_user = parsed_html.find('div', {'class': 'logout2'}).find('input', {'name': 'loggedInUser'}).get(
            'value')
        print('logged in as: ', logged_in_user)
        return True
    except:
        logging.exception('Exception encountered')
        pass
    return False


if __name__ == '__main__':
    while True:
        if not is_logged_in(REDIRECT_ADDRESS):
            post_login_request()
        else:
            print("User logged in, skipping login.")
            sleep(5)
