"""Module `task_03` provides function `normalize_phone(phone_number)` that allows to normalize phone number
by removing all non-digit characters and adding country code if it is missing."""

import re

def normalize_phone(phone_number):
    """Normalizes phone number by removing all non-digit characters
    or `+` and adding country code if it is missing."""
    pattern = r"[+\d]"
    phone_number = "".join(re.findall(pattern, phone_number))
    phone_number = re.sub(r"^(\+38|38)?", "+38", phone_number)
    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS campaign:", sanitized_numbers)
