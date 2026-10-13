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

print("[*] تم تشغيل السكريبت بنجاح، بانتظار إرسال طلبات التنشيط...")

while True:
    try:
        # إرسال الطلب مع مهلة أمان مريحة (10 ثانية اتصال، 20 ثانية قراءة)
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=(10, 20))
        
        # طباعة حالة الرد والنص لنتأكد أنه يعمل تماماً مثل الكود القديم
        print(f"[+] تم التنشيط - حالة الرد: {response.status_code} | الاستجابة: {response.text}")
        
    except Exception as e:
        # إظهار الخطأ بوضوح لكي نعرف إن حدث أي خلل بدلاً من التجاهل الصامت
        print(f"[-] تنبيه اتصال: {e}")
        
    # الانتظار لمدة 90 ثانية (أو دقيقة ونصف) لتكرار الإنعاش
    time.sleep(90)
