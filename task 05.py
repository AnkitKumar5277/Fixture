# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}


def test_invalid_creation():
    path_post = "/booking"
    full_url = base_url + path_post
    payload = {
        "*firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code == 500
    assert response_data.text == "Internal Server Error"

"""
### 🔍 Code Explanation in **Hinglish** (Test Case #5 – Invalid Creation):

Yeh test case **intentionally galat payload bhej raha hai** taaki dekhe ki API kaise respond karti hai jab **JSON galat hota hai**.

---

### 🧾 Code Breakdown:

```python
payload = {
    "*firstname": "Jim",
```

➡️ Yahaan `*firstname` likha gaya hai, jabki sahi key hona chahiye **`firstname`** (without `*`).
Yeh ek **invalid key** hai, jo server ko confuse karegi.

---

### 🧪 Test Kya Kar Raha Hai?

1. `/booking` endpoint par ek **POST request** bhej raha hai.
2. JSON payload **galat hai intentionally**.
3. **Expected response**:

   * `status_code == 500` (Server error)
   * `response.text == "Internal Server Error"`

---

### ⚠️ Expected Output:

API ko samajh nahi aayega payload, toh woh **500 Internal Server Error** return karega — matlab **server crash ya fail** hua handle karne mein.

---

### ✅ Purpose of Test:

Check karna ki agar user **wrong format ka data** bhej de, toh server ka response kya hota hai.
Yeh ek **negative test case** hai — galtiyon ko pakadne ke liye.

---

Agar aur bhi variations chahiye galat payloads ke, toh batao — main likh ke de deta hoon.

"""
