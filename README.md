## Keychain Backbone For Windows10
* DEPENDENCIES BELOW

## python3 keyring module installation on WSL2
** Packages:
* keyring, keyrings.cryptfile, keyring_jeepney, 
* argon2-cffi, pycryptodome, SecretStorage, cryptography
# Install Commands

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3 python3-pip
    sudo apt-get install python-is-python3
    sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
    sudo apt-get install dos2unix

    python -m pip install argon2-cffi
    python -m pip install SecretStorage
    
# Turning .py into Executable Program Steps
* Assuming your current directory is PasswKey (Example: C:/Users/name/PyCharmProjects/PasswKey
  Instead of needing to reference the program in Ubuntu with the command
  
      /path/to/python passw.py (if you are in the main folder 'PasswKey'
      
* You can simply give the command

      cp /path/to/file/filename.py /path/to/file/filename
         
1. Give the file executable permissions with following command

         chmod +x /path/to/file/filename
2. Run the dos2unix program on the file you just created

         dos2unix /path/to/file/filename
         
3. Move the file to /usr/local/bin/

         sudo mv /path/to/file/filename /usr/local/bin/
         
* Finally Close the Ubuntu Terminal and Reopen it, try typing 'passw' in Ubuntu and see what happens
