#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Leak Checker - فحص التسريبات"""

import requests, json, hashlib
from datetime import datetime

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

def check_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            for line in r.text.splitlines():
                h, count = line.split(':')
                if h == suffix:
                    return int(count)
        return 0
    except:
        return -1

def check_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    headers = {'User-Agent': 'WHISKEY-MD-OSINT'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 404:
            return []
        else:
            return None
    except:
        return None

def main():
    print(f"{YELLOW}اختر نوع الفحص:{RESET}")
    print(f"  {RED}[1]{RESET} 📧 بريد إلكتروني (HaveIBeenPwned)")
    print(f"  {RED}[2]{RESET} 🔑 كلمة مرور (PwnedPasswords)")

    choice = input(f"\n{CYAN}اختر [1-2]: {RESET}").strip()

    if choice == '1':
        email = input(f"{CYAN}📧 أدخل البريد الإلكتروني: {RESET}").strip()
        if not email:
            print(f"{RED}❌ لم تدخل بريداً!{RESET}")
            return

        print(f"\n{YELLOW}[*] جاري الفحص...{RESET}")
        leaks = check_email(email)

        if leaks is None:
            print(f"{RED}❌ فشل الاتصال بـ HaveIBeenPwned{RESET}")
            return

        if not leaks:
            print(f"\n{GREEN}✅ ممتاز! البريد غير مسرّب{RESET}")
        else:
            print(f"\n{RED}🚨 تحذير! تم العثور على {len(leaks)} تسريب:{RESET}\n")
            for leak in leaks:
                print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                print(f"{CYAN}📛 الاسم    :{RESET} {leak.get('Name','?')}")
                print(f"{CYAN}📅 التاريخ  :{RESET} {leak.get('BreachDate','?')}")
                print(f"{CYAN}👥 المتأثرون:{RESET} {leak.get('PwnCount','?'):,}")

            fname = f"leak_{email.replace('@','_at_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(fname, 'w', encoding='utf-8') as f:
                json.dump(leaks, f, ensure_ascii=False, indent=2)
            print(f"\n{GREEN}💾 تم الحفظ في: {fname}{RESET}")

    elif choice == '2':
        import getpass
        password = getpass.getpass(f"{CYAN}🔑 أدخل كلمة المرور (لن تظهر): {RESET}")
        if not password:
            print(f"{RED}❌ لم تدخل كلمة مرور!{RESET}")
            return

        print(f"\n{YELLOW}[*] جاري الفحص...{RESET}")
        count = check_password(password)

        if count == -1:
            print(f"{RED}❌ فشل الاتصال بالخادم{RESET}")
        elif count == 0:
            print(f"{GREEN}✅ كلمة المرور آمنة{RESET}")
        else:
            print(f"{RED}🚨 كلمة المرور مسربة! ظهرت {count:,} مرة{RESET}")
    else:
        print(f"{RED}❌ خيار غير صحيح!{RESET}")
