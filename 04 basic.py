import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests

def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

def test_update_req_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

def test_update_req_3(create_token, create_booking_id, read_csv_file_data):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)

# Is Python code mein humne `pytest`, `allure`, aur `requests` libraries ka use kiya hai.
# Ye teenon modules automated testing ke liye kaafi popular hain, especially APIs ke test cases banane mein.
# Code mein teen test functions hain — `test_update_req_1`, `test_update_req_2`, aur `test_update_req_3`. 
# In test functions mein hum fixtures ka use kar rahe hain: `create_token`, `create_booking_id`, aur `read_csv_file_data`.
# Fixtures ek tarah ka helper function hote hain jo test case run hone se pehle kuch specific data ya setup return karte hain. 
# Jaise `create_token` fixture se ek authorization token milta hoga, `create_booking_id` se booking ka ID milta hoga, 
# aur `read_csv_file_data` se koi external CSV file ka data return ho raha hoga. In teen test functions mein yeh values sirf print ho rahi hain, 
# lekin actual use-case mein inka use API request bhejne ya validate karne ke liye hota hai.
# Allure library ka use testing ke results ka graphical report banane ke liye hota hai, 
# jo ki readable aur shareable hoti hai. Is tarah ka setup test automation process ko efficient aur maintainable banata hai. Ye approach software testing mein standard practice hai.
