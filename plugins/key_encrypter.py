from Crypto.PublicKey.RSA import RsaKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from mint_encrypter.setup import _KEYSIZES, _PUBLIC_KEY_PATH, _PRIVATE_KEY_PATH, _PASSPHRASE


class KeyEncrypter:
    """
        This class using RSA algorithm with 2048 bits-key to
        encrypt AES key that used to encrypted files.
    """

    @staticmethod
    def generate_keys():
        """
            Generate RSA public and private keys with 2048 bit-keys
        :return: public and private RSA keys.
        """
        key = RSA.generate(_KEYSIZES)
        private_key, public_key = key, key.public_key()

        return public_key, private_key

    @staticmethod
    def export_keys(public_key: RsaKey, private_key: RsaKey):
        """
            Export public and private keys to files.
        :param public_key: The public key to export.
        :param private_key: The private key to export.
        """

        with open(_PUBLIC_KEY_PATH, "wb") as pub_key:
            pub_key.write(public_key.export_key("PEM"))
            pub_key.close()

        with open(_PRIVATE_KEY_PATH, "wb") as prv_key:
            prv_key.write(private_key.export_key("PEM", _PASSPHRASE, 8))
            prv_key.close()

    @staticmethod
    def get_public_key(path):
        """
            Get public RSA key from file.
        :param path: Path of the file that contain public RSA key.
        :return: The public RSA key.
        """
        with open(path, "r") as pub_key:
            public_key = RSA.import_key(pub_key.read())

        return public_key

    @staticmethod
    def encrypt(aes_key, public_key: RsaKey):
        """
            Encrypt the AES key with public RSA key.
        :param aes_key: The AES key to encrypt.
        :param public_key: The public RSA key.
        :return: Encrypted AES key.
        """

        encrypter = PKCS1_OAEP.new(public_key)
        encrypted_key = encrypter.encrypt(aes_key)

        return encrypted_key
