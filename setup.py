import os

# Config
_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
_PUBLIC_KEY_PATH = os.path.join(_ROOT_DIR, "keys\\public_key.pem")
_PRIVATE_KEY_PATH = os.path.join(_ROOT_DIR, "keys\\private_key.pem")
_KEYSIZES = 2048  # RSA Bits size key
_PASSPHRASE = "MINT IS VERY COOL!"  # Passphrase for encrypt RSA private key.
