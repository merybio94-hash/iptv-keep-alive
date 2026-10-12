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

print("[*] تم بدء تشغيل نظام الإنعاش الذكي مع حماية ضد انقطاع الاتصال...")

while True:
    try:
        # رفع مهلة الانتظار إلى 15 ثانية لمنع أخطاء التايم أوت
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=15)
        
        print(f"[+] تم التنشيط بنجاح - الحالة: {response.status_code}")
        
    except requests.exceptions.Timeout:
        print("[-] تنبيه: انتهت مهلة الاتصال بالسيرفر، سيتم إعادة المحاولة في الجولة القادمة...")
    except requests.exceptions.ConnectionError:
        print("[-] تنبيه: خطأ في الاتصال بالشبكة أو أن السيرفر مغلق مؤقتاً...")
    except Exception as e:
        print(f"[-] حدث خطأ غير متوقع: {e}")
        
    # زيادة الفاصل الزمني إلى 120 ثانية (دقيقتين) لتخفيف الضغط على السيرفر وتجنب الحظر
    time.sleep(120)
