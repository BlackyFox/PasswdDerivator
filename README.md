ATTENTION!! This script is still under production, please be aware you might encounter some bugs... Also, now, it will produce really big files while using it on real life sized passwords... (I'm talking Gb files)
# PasswdDerivator
This script aim is to derivate a string. This can be usefull when using a bruteforce solution on a based string (default password derivated by users).

## Installation
Get the latest version:
``` bash
git clone https://github.com/BlackyFox/PasswdDerivator
cd PasswdDerivator
```

## Usage
``` bash
./PasswdDerivator.py [-h] [-o OUTPUT] input

positional arguments:
  input                 The string to derivate

optional arguments:
  -h, --help                    show this help message and exit
  -o OUTPUT, --output OUTPUT    Specify a file to write the results
```

### Example
Derivation of the password *password*:
``` bash
./PasswdDerivator.py password
```
This wil give you an output like:
``` bash
Password
PAssword
PASsword
PASSword
PASSWord
PASSWOrd
PASSWORd
PASSWORD
PASSWOR|)
passworD
...
```
