from pprint import pprint
from cryptography.fernet import Fernet, InvalidToken


input_file = 'business'
output_file = 'outpitfile'


def keyz():
    key = Fernet.generate_key()
    with open('keys.key', 'wb') as damage:
        damage.write(key)
        pprint(damage.write(key))


def load_key():
    return open('keys.key', 'rb').read()

#encrypt file

with open(input_file, 'rb') as filo:
    out = filo.read()

key = load_key()
fernet = Fernet(load_key())
dropkey = fernet.encrypt(out)

with open(output_file, 'wb') as filesave:
    filesave.write(dropkey)
    pprint(filesave.write(dropkey))


with open(output_file, 'rb') as f:
    data = f.read()

# decrypt file 
    
    
try:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open('clearfile', 'wb') as fs:
        fs.write(decrypted)


except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")
