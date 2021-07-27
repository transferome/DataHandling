# Keychain Backbone For Windows10, 
# Program tocreate and store passwords, via a master password

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
