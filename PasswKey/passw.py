#!  /usr/bin/python3
"""Program For A Command Line Interface Password Manager.
Currently Two Actions
passw       <-- retrieves password given Site, Username, and Keychain Password
passw -p    <-- sets a password, enter Site, Username, and the Password, Followed By Keychain Password
DEPENDENCIES:
python3 modules:
keyring, keyrings.cryptfile, keyring_jeepney, argon2-cffi, pycryptodome, SecretStorage, cryptography
    * install the python modules through WSL2 Ubuntu
    1. Get Ubuntu ready
    - sudo apt-get update
    - sudo apt-get upgrade
    - sudo apt-get install python3 python3-pip
    - sudo apt-get install python-is-python3
    - sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
            ** First two should be done before you install anything new, and the rest are making sure everything you
            need for python to behave well on WSL2
    - sudo apt-get install dos2unix
    2. Second, Then install each of the python modules, by using the "python -m pip install"  command
    examples...
    python -m pip install argon2-cffi
    python -m pip install SecretStorage
    ...
    **** At this point could run the program using /path/to/python passw.py (if you are in the main folder 'PasswKey' directory'
    *** But it can be made even better
    3. Make a copy of this file without the file extension in Ubuntu
    cp /path/to/file/filename.py /path/to/file/filename
    4. give the file executable permissions with following command
    chmod +x /path/to/file/filename
    5. *** Added step for WSL2 - Need to run following command
    dos2unix /path/to/file/filename
    6. move the file to /usr/local/bin/
    sudo mv /path/to/file/filename /usr/local/bin/
    7. Close the Ubuntu Terminal and Reopen it
    Typing only 'passw' into the terminal should initiate the program.
Linux Packages: dos2unix"""
from keyrings.cryptfile.cryptfile import CryptFileKeyring
import keyring


def add_password(keyring_instance):
    servicename = input('Enter Service or Site:\t')
    username = input('Enter Username:\t')
    password = input('Enter Password:\t')
    keyring_instance.set_password(servicename, username, password)
    print(f'Password for {servicename}\t{username} Set')


def request_password(keyring_instance):
    servicename = input('Enter Service or Site:\t')
    username = input('Enter Username:\t')
    passout = keyring_instance.get_password(servicename, username)
    if passout:
        print(f'Requested Password:\t{passout}')
    else:
        print('No password set for this Service or Username')


def keyring_cli(argument):
    """Requests methods from an instance of EncryptedKeyring, which unlocks the keyring,
    based on options given on the command line"""
    kr = CryptFileKeyring()
    keyring.set_keyring(kr)
    # keyring.keyring_key = getpass.getpass('Password', stream=sys.stderr)
    if not argument:
        request_password(kr)
    else:
        add_password(kr)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Python Keyring Program", add_help=True)
    # True false switch, -p sets to True, which then makes keyring_cli go to add_password
    parser.add_argument('-p', action='store_true', default=False, dest='boolean_t',
                        help='Sets Creat Password to True')
    results = parser.parse_args()
    keyring_cli(results.boolean_t)
