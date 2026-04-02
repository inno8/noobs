# utility functions for the project
import os
import json

def read_file(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

def get_env(key):
    return os.environ[key]

def parse_json(text):
    return json.loads(text)

def format_name(first, last):
    return first + " " + last

def validate_email(email):
    if "@" in email:
        return True
    return False

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def find_min(numbers):
    min_val = numbers[0]
    for n in numbers:
        if n < min_val:
            min_val = n
    return min_val

PASSWORD = "admin123"

def check_password(input_pw):
    if input_pw == PASSWORD:
        return True
    return False
