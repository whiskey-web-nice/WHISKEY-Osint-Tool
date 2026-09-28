#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TikTok OSINT - جلب معلومات حساب تيك توك"""

import requests, json, os
from datetime import datetime

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

# ═══════════════════════════════════════════════════
# 🔑 المفتاح يُقرأ من متغير البيئة أو يُدخل يدوياً
# ═══════════════════════════════════════════════════
def get_api_key():
    """جلب مفتاح Firebase من متغير البيئة"""
    # 1. جرّب من متغير البيئة
    key = os.environ.get('TIKTOK_API_KEY')
    if key:
        return key
    
    # 2. جرّب من ملف config.ini (اختياري)
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                for line in f:
                    if line.startswith('TIKTOK_API_KEY'):
                        return line.split('=')[1].strip()
        except:
            pass
    
    # 3. اطلب من المستخدم
    print(f"{YELLOW}⚠️  مفتاح API غير موجود في متغيرات البيئة{RESET}")
    key = input(f"{CYAN}🔑 أدخل Firebase API Key (أو Enter لاستخدام الافتراضي): {RESET}").strip()
    if not key:
        # القيمة الافتراضية العامة (موجودة في تطبيقات كثيرة على الإنترنت)
        key = "AIzaSyAZqmylIOE4fQmf0pemugc2iBH33rSeMkg"
    return key


def get_tiktok_info(username):
    api_key = get_api_key()
    
    ur = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser"
    dat = {'key': api_key}
    dataa = json.dumps({"returnSecureToken": True})
    he = {
        'User-Agent': "okhttp/3.12.1",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-client-version': "ReactNative/JsCore/7.8.1/FirebaseCore-web"
    }
    res = requests.post(ur, params=dat, data=dataa, headers=he, timeout=15)
    res.raise_for_status()
    token = res.json().get("idToken")

    url = "https://us-central1-tikfans-prod-a3557.cloudfunctions.net/getTikTokUserInfo"
    data = json.dumps({"data": {"username": username}})
    he = {
        'User-Agent': "okhttp/3.12.1",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'authorization': f"Bearer {token}"
    }
    re = requests.post(url, data=data, headers=he, timeout=15)
    re.raise_for_status()
    return re.json()


def main():
    username = input(f"{CYAN}📸 أدخل يوزر تيك توك (بدون @): {RESET}").strip().replace('@','')
    if not username:
        print(f"{RED}❌ لم تدخل يوزر!{RESET}")
        return

    print(f"\n{YELLOW}[*] جاري جمع المعلومات...{RESET}\n")

    try:
        data = get_tiktok_info(username)
        r = data.get('result', {})

        print(f"{YELLOW}═══════════ معلومات الحساب ═══════════{RESET}")
        print(f"{CYAN}👤 اليوزر       :{RESET} @{r.get('uniqueId','?')}")
        print(f"{CYAN}🆔 User ID      :{RESET} {r.get('userId','?')}")
        print(f"{CYAN}📛 الاسم        :{RESET} {r.get('nickName','?')}")
        print(f"{CYAN}📝 البايو        :{RESET} {r.get('signature','') or 'فارغ'}")
        print(f"{CYAN}👥 المتابِعون   :{RESET} {r.get('following','?')}")
        print(f"{CYAN}💚 المعجبون     :{RESET} {r.get('fans','?')}")
        print(f"{CYAN}🎬 الفيديوهات   :{RESET} {r.get('video','?')}")
        print(f"{CYAN}❤️  القلوب       :{RESET} {r.get('heart','?')}")
        print(f"{CYAN}👍 الإعجابات    :{RESET} {r.get('digg','?')}")
        print(f"{CYAN}🔒 حساب سري؟    :{RESET} {'نعم' if r.get('isSecret') else 'لا'}")
        print(f"{CYAN}⭐ مفضلة مفتوحة؟:{RESET} {'نعم' if r.get('openFavorite') else 'لا'}")
        print(f"{CYAN}🔑 SecUID       :{RESET} {r.get('secUid','?')}")

        covers = r.get('coversMedium', [])
        if covers:
            print(f"\n{GREEN}🖼️  صورة البروفايل: {RESET}{covers[0]}")
        print(f"{GREEN}🔗 رابط الحساب: {RESET}https://tiktok.com/@{r.get('uniqueId','')}")

        fname = f"tiktok_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n{GREEN}💾 تم الحفظ في: {fname}{RESET}")

    except requests.exceptions.HTTPError as e:
        print(f"{RED}❌ الحساب غير موجود أو تم حظره: {e}{RESET}")
    except Exception as e:
        print(f"{RED}❌ خطأ: {e}{RESET}")
