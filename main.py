import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://up.smf24.cx:8088/hr.php"

params = {
    'SzRZSFBiRS9wSDZkUVk4TmhBUU13d1VnNjZibW9DVE9kWERpc3ZkQUhXWWVPaW94ZGkvN3hMbndna3V6OWZsNwo': ""
}

headers = {
    'Host': "up.smf24.cx:8088",
    'User-Agent': "84388B2359531",
    'Connection': "Keep-Alive"
}

print("[*] تم بدء تشغيل نظام الإنعاش مع مهلة قراءة موسعة...")

while True:
    try:
        # ضبط مهلة الاتصال والقراءة (connect=10, read=20) لإعطاء فرصة للسيرفر البطيء
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=(10, 20))
        
        print(f"[+] تم التنشيط بنجاح - الحالة: {response.status_code}")
        
    except requests.exceptions.RequestException:
        # تجاهل أخطاء التايم أوت المؤقتة لكي يستمر السكريبت بالعمل بسلاسة
        pass
        
    # الانتظار 120 ثانية قبل الجولة التالية
    time.sleep(120)
