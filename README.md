# FERNET encrypt/\decrypt file

Fernet (symmetric encryption)¶
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via MultiFernet.


 for more datail please check the documentation ==> [Fernet Documentation](https://cryptography.io/en/latest/fernet/).
 


>>>>>/
>>>>>>>>>>/ 
>>>>>>>>>>>>>>>/ 


## Idea of script

idea of the script and that when we have a file that contains login credentials 

Example:  in the field of automation network, we have files that contain login credentials via ssh for cisco devices

therefore it is better not to keep the files in clear text


## Installation

Use the package manager [pip](https://pypi.org/project/fernet/) to install fernet.

```bash
pip install fernet
```


## Usage

the script from two operations:

First = decrypt the file >>/ Two = decrypt the file 

**note** we have to keep the key to be able to decroipt the file
