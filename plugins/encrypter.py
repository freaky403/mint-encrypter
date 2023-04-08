from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


class Encrypter:
    """
        This class using AES algorithm with EAX mode to
        encrypt files.
    """

    @staticmethod
    def generate_key(key_length=32):
        return get_random_bytes(key_length)

    @staticmethod
    def encrypt(content, key):
        """
            Encrypt given content with AES algorithm.
        :param content: Content to encrypt.
        :param key: The AES key.
        :return: Encrypted content, MAC tag and nonce.
        """
        encrypter = AES.new(key, AES.MODE_EAX)
        encrypted_content, tag = encrypter.encrypt_and_digest(content)

        return encrypted_content, tag, encrypter.nonce
