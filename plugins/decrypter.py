from Crypto.Cipher import AES


class Decrypter:
    """
        This class using AES algorithm with EAX mode to
        decrypt files.
    """
    @staticmethod
    def decrypt(content, tag, nonce, key):
        """
            Decrypt given content with AES algorithm.
        :param content: Content to decrypt.
        :param tag: The length of the MAC tag.
        :param nonce: The value of the fixed nonce.
        :param key: The private AES key.
        :return: Decrypted content.
        """
        decrypter = AES.new(key, AES.MODE_EAX, nonce)
        decrypted_content = decrypter.decrypt_and_verify(content, tag)

        return decrypted_content
