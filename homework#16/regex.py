import re

print('=' * 20, 'Task #1', '=' * 20)


def search_phone(text):
    """
    1. Write a Python program which search a phone numbers.
    Valid example: Hello, my phone number is 251-65-23.

    Invalid example: Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.
    """
    text = str(text)

    pattern = r'(\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2})'
    res = re.findall(pattern, text)

    if res:
        print(f"The following phone number[s] found: {res}")
    else:
        print("No matches")


text_1 = "Hello, my phone number is 251-65-23."
text_2 = "Hello, my phone number is 251 65 23."
text_3 = "Hello, my phone number is 251.65.23."
text_4 = "Henry Ford was born July 30, 1863, on a farm in Springwells " \
         "Township, Michigan."

search_phone(text_1)
search_phone(text_2)
search_phone(text_3)
search_phone(text_4)

print('=' * 20, 'Task #2', '=' * 20)


def check_email(email):
    """
    2.   Write a Python program basic validation for email.
    Local part should be consisted of lower/upper case, number, underscore and dot.
     Domain part - the same but dot symbol could not be the first character.
    """
    email = str(email)

    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    res = re.findall(pattern, email.lower())

    if res:
        print("Email is valid!")
    else:
        print("Email is NOT valid")


email_1 = "tarasblast@gmail.com"
email_2 = "123_paraska123@bombalaboom123_ergeg.bom"
email_3 = ".bob@gmail.com"
email_4 = "john_anderson@.tcb.com"

check_email(email_1)
check_email(email_2)
check_email(email_3)
check_email(email_4)

print('=' * 20, 'Task #3', '=' * 20)


def remove_zeros_from_ip(ip_adr):
    """
    3. Write a Python program to remove redundant zeros from an IP address.
        Example: "216.008.094.196" -> "216.8.94.196
    """
    ip_adr = str(ip_adr)

    res = re.sub('(^|\.)0+(?=[^.])', r'\1', ip_adr)
    print(res)


ip_adr_1 = "216.008.094.196"
ip_adr_2 = "216.010.000.196"
ip_adr_3 = "200.100.050.000"
ip_adr_4 = "000.000.000.001"

remove_zeros_from_ip(ip_adr_1)
remove_zeros_from_ip(ip_adr_2)
remove_zeros_from_ip(ip_adr_3)
remove_zeros_from_ip(ip_adr_4)

print('=' * 20, 'Task #4', '=' * 20)


def check_ip(ip):
    """
    Write a Python program that check if IP address is valid.
    Valid Example: 216.8.94.196, 0.0.0.0, 127.0.0.1
    Invalid Example: 216.8.94, 14.0..139, 153.192.392.84
    """

    ip = str(ip)
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[" \
              r"0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if (re.search(pattern, ip)):
        print("Valid IP Address")
    else:
        print("Invalid IP Address")


ip_1 = "216.8.94.196"
ip_2 = "0.0.0.0"
ip_3 = "127.0.0.1"
ip_4 = "216.8.94"
ip_5 = "4.0..139"
ip_6 = "153.192.392.84"

check_ip(ip_1)
check_ip(ip_2)
check_ip(ip_3)
check_ip(ip_4)
check_ip(ip_5)
check_ip(ip_6)
