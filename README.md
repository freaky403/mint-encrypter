# MintEncrypter - Ransomware


## About this project
<p>
    MintEncrypter is a ransomware project created for educational purposes only. 
    This project is designed to demonstrate the techniques used by attackers to encrypt data and demand ransom from the victims. 
    The project should not be used for any malicious purposes, and the developers are not responsible for any damage caused by the misuse of this software.
</p>
<p>
MintEncrypter uses a hybrid cryptographic system to encrypt files. This system combines the strengths of both symmetric and asymmetric encryption algorithms to provide a secure and efficient solution for encrypting data.
</p>
<p>
The system first generates a random symmetric key using the AES (Advanced Encryption Standard) algorithm. This key is used to encrypt the data, as symmetric encryption algorithms are faster and more efficient than asymmetric algorithms.
</p>
<p>
However, the symmetric key is itself encrypted using an asymmetric encryption algorithm, specifically RSA (Rivest-Shamir-Adleman). This ensures that the symmetric key is securely transmitted to the attacker, who holds the private key to decrypt it.
</p>
<p>
RSA is a public-key cryptosystem that uses two keys, a public key for encryption and a private key for decryption. The public key can be shared with anyone, while the private key is kept secret by the owner. When a message is encrypted using the public key, only the owner of the private key can decrypt it.
</p>
<p>
MintEncrypter uses a 2048-bit RSA key pair to encrypt the symmetric key. This provides a high level of security, as cracking the encryption would require breaking the RSA algorithm's mathematical properties, which is computationally infeasible.
</p>

## Installation
To use MintEncrypter, you need to clone the project from the repository:
```bash
git clone https://github.com/freaky403/mint-encrypter.git
```
Once you have cloned the repository, navigate to the project directory and run the following command:
```bash
pip install -r requirements.txt
```
This will install all the necessary dependencies for the project.

## Usage
To run MintEncrypter, navigate to the project directory and run the following command:
```bash
py main.py
```

## Liability Disclaimer
MintEncrypter is designed for educational purposes only. The developers do not condone the use of this project for any malicious purposes. Any damage caused by the misuse of this software is the sole responsibility of the user. The developers are not liable for any damages resulting from the use of this software.

## Contributing
If you would like to contribute to the project, you can fork the repository and create a pull request. Please make sure that your changes are in line with the goals of the project and do not introduce any security vulnerabilities.

## License
MintEncrypter is released under the MIT license. See `LICENSE` for details.