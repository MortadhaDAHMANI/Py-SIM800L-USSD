# Py-SIM800L :radio: :computer: :phone:

## Summary
#### What is USSD?
USSD (*Unstructured Supplementary Service Data*) is an interactive, menu-based technology communication protocol available on every GSM-enabled mobile device.

It is a session-based text communication without a store-and-forward mechanism (unlike SMS) that is practical for interactive communication, such as banking or education.

USSD messages can have up to **182 alphanumeric characters** and the time it takes from a request to a response is 2 seconds while it takes 6 seconds for an SMS to reach a mobile phone.

#### What is the difference between USSD and SMS?

While SMS is a store and forward technology, USSD texts and interactions are not stored on the mobile phone. SMS content remains stored in the mobile phone memory.

#### Examples of USSD usage

Some examples of service usage are airtime top-ups, *"please call me"* services, balance checking and mini statements delivery.

#### What about USSD short codes?

USSD short code format is defined by the __* and #__ signs at the beginning and the end of the series of digits.

There are three types of USSD short codes available. The standard rate USSD short code is charged the standard fee for the USSD menu usage by the end-user. Reverse-billed short codes are free for the end-user. Premium rate USSD short codes are charging the end user a premium price for short code triggering. Generally, USSD short codes are either reverse-billed or standard rate. 

## Requirements
- ``Python 2.7 or Python 3.4 and newer``

- ``If running on Windows: Windows 7 or newer``

## Installation

This installs a package that can be used from Python:

```python
   import serial
```
### From PyPI

pySerial can be installed from PyPI:

    python -m pip install pyserial

Using the `python`/`python3` executable of the desired version (2.7/3.x). 

Developers also may be interested to get the source archive, because it
contains examples, tests and the this documentation. By using PyPI, you will be using the latest stable version.

--------------------

## Pinout
![alt iviny](https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/original.jpg)

```diff
- NOTICE: Be prepared to handle huge power consumption with peek up to 2A. Maximum voltage on UART in this module is 2.8V. Higher voltage will kill the module.
```

### My Hackster Tutorial
<a href="https://www.hackster.io/mortadhadahmani/py-sim800l-ussd-167cc8" rel="Hack"> <img src="https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/hackster.png" alt="Donation" height="50"></a>

### Useful links
* [AT Commands](https://nettigo.eu/attachments/386 "AT Commands")
* [Hardware Design](https://nettigo.eu/attachments/385 "Hardware Design")
* [Specification](https://nettigo.eu/products/sim800l-gsm-grps-module "Specification")
* [Tutorial Arduino](https://lastminuteengineers.com/sim800l-gsm-module-arduino-tutorial/ "Arduino")
* [Arduino Library](https://github.com/cristiansteib/Sim800l "Arduino Lib.")
* [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html "PySerial")
* [PySerial Git](https://github.com/pyserial/pyserial "PySerial Git")

### Donation
If this project help you, you can give me a tip ;)

<!---
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg?style=for-the-badge&logo=paypal&link=https://www.paypal.com/paypalme2/billzgithub)](https://paypal.me/mamdpay)
-->

<a href="https://paypal.me/mamdpay" rel="In"> <img src="https://www.pngarts.com/files/4/Paypal-Donate-PNG-High-Quality-Image.png" alt="Donation" height="70"></a>

<!--a href="https://www.linkedin.com/in/mortadhadahmani" rel="In"> <img src="https://ps.w.org/button-paypal-donation/assets/icon-256x256.jpg" alt="Donation" height="150"></a-->

<!--a href="https://paypal.me/mamdpay" rel="In"> <img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donation" height="100"></a-->

<!--a href="https://paypal.me/mamdpay" rel="In"> <img src="https://wildflowercottage.org/wp-content/uploads/2019/03/paypal_donate_button_png_996391.png" alt="Donation" height="150"></a-->

### Author
* This version has been created by: [**Mortadha DAHMANI**](mailto:mortadha.dahmani@gmail.com)

<a href="https://www.linkedin.com/in/mortadhadahmani" rel="In"> <img src="https://github.com/MortadhaDAHMANI/Py-SIM800L/raw/master/in2.jpg" alt="In" height="40"></a>

### Revision History
* Initial Release : 25 Mars 2020

### License
* _Py-SIM800L_ is distributed under the **LGPL** version 3 license.
