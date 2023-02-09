# SQLMAP TamperScripts

This repository contains a collection of custom SQLmap tamper scripts, designed to evade simple signature-based and pattern-based detection mechanisms. These scripts offer advanced payload manipulation techniques, making it easier to identify and exploit SQL injection vulnerabilities.


## Base64.py

  Base64 encoding and decoding

   Description: This tamper script encodes the payloads in base64 format before sending them to the target, and then decodes them on the server side. This technique could potentially evade simple signature-based detection mechanisms.
   
   Working: This script takes in a payload as an argument, encodes the payload using base64 encoding, and then returns the encoded payload. The .encode() and .decode() methods are used to convert the payload to and from byte strings, respectively, to ensure that the payload can be processed correctly by the base64 encoding and decoding functions.


 ## Regexman.py
 
   Regex manipulation
   
   Description: This tamper script manipulates the payloads by changing the regular expressions used to match specific patterns in the payloads. This could be used to evade pattern-based detection mechanisms.
    
   Working: This script takes in a payload as an argument and uses the re.sub method from the re (regular expression) module in Python to search for instances of the word AND in the payload and replace them with OR. This could be used to evade simple signature-based detection mechanisms that rely on matching specific keywords in payloads.

 ## Chainer.py
 
   Chained encoding
    
   Description: This tamper script encodes the payloads multiple times, using different encoding techniques, before sending them to the target. This could potentially make it more difficult for the target to detect the payloads.
    
   Working: This script takes in a payload as an argument and uses the quote_plus method from the urllib.parse module in Python to perform URL encoding on the payload twice. This can be used to evade security measures such as WAFs that rely on detecting specific characters in payloads.

 ## Usage

   To use these scripts, simply copy the desired script(s) into the SQLmap's tamper directory. Then, during the SQLmap scan, use the --tamper option to specify which tamper script(s) to use (without adding .py extension). For example, to use the Base64 encoding and decoding tamper script, run the following command:
   
    python sqlmap.py -u <target_url> --tamper=scriptname

 ## Contributions

   Feel free to submit pull requests with your own custom tamper scripts or improvements to the existing scripts. Your contributions are greatly appreciated!
