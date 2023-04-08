from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class KeyDecrypter:
    """
        This class using RSA algorithm with 2048 bits-key to
        decrypt AES key that used to encrypted files.
    """

    @staticmethod
    def get_private_key(path, passphrase):
        """
            Get the private AES key from file.
        :param path: Path of the file that contain the private AES key.
        :param passphrase: The passphrase used to encrypted private key.
        :return: The private AES key.
        """

        with open(path, "r") as prv_key:
            private_key = RSA.import_key(prv_key.read(), passphrase)

        return private_key

    @staticmethod
    def decrypt(encrypted_aes_key, private_key):
        """
            Decrypt the AES key with private AES key.
        :param encrypted_aes_key: The encrypted AES key to decrypt.
        :param private_key: The private AES key.
        :return: Decrypted AES key.
        """
        decrypter = PKCS1_OAEP.new(private_key)
        decrypted_key = decrypter.decrypt(encrypted_aes_key)

        return decrypted_key
