# COMP2040 - Operating System Group Project

+ **Group**: UCA 
+ **Members**:
  + Nguyen Tuan Anh
  + Nguyen Thai Uyen
  + Phan Thi Hien Chi 
+ **Topics**: GNU/Linux Kernel & Kernel vulnerabilities 

## Topic

Bug chain of OS Command Injection to Dirty CoW ([CVE-2016-5195](https://nvd.nist.gov/vuln/detail/cve-2016-5195)) on Linux 3.13.0-170-generic kernel (Ubuntu 14.04.02 Trusty Tahr)

## Setup 

1. Using Virtualbox/VMWare/any virtualization, with amd64/i386 image of [Ubuntu 14.04.02](http://old-releases.ubuntu.com/releases/14.04.0/)
2. (Optional but highly recommended) Install a higher version of Python3 (3.7+). Follow this [guide](https://github.com/actions/setup-python/issues/93).
3. Clone this repository

```bash
git clone ...
```
4. Run the web service
```bash
cd COMP2040-LinuxKernelVuln
python3 ./main.py
```
