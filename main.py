import time
import requests

url = "http://up.smf24.cx:8088/hr.php"

params = {
    'SzRZSFBiRS9wSDZkUVk4TmhBUU13d1VnNjZibW9DVE9kWERpc3ZkQUhXWWVPaW94ZGkvN3hMbndna3V6OWZsNwo': ""
}

headers = {
    'Host': "up.smf24.cx:8088",
    'User-Agent': "66482B2359531",
    'Connection': "Keep-Alive"
}

print("جاري بدء التكرار كل ثانيتين... اضغط Ctrl+C للإيقاف.")

counter = 0

try:
    while True:
        counter += 1
        try:
            response = requests.get(url, params=params, headers=headers, timeout=5)
            print(f"[{counter}] حالة الطلب: {response.status_code} - الرد: {response.text[:100]}")
        except requests.exceptions.RequestException as e:
            print(f"[{counter}] حدث خطأ في الاتصال: {e}")
        
        # الانتظار لمدة ثانيتين قبل الطلب التالي
        time.sleep(2)

except KeyboardInterrupt:
    print("\nتم إيقاف البرنامج بواسطة المستخدم.")
