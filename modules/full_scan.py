#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full Scan - تشغيل جميع الأدوات على نفس الهدف"""

import time
from modules import phone_scanner, whisky_osint, google_dorks, leak_checker, tiktok_osint

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

def main():
    print(f"{RED}⚡ وضع المسح الشامل - جميع الأدوات{RESET}\n")

    phone = input(f"{CYAN}📱 أدخل رقم الهاتف (مثال: +201234567890): {RESET}").strip()
    if not phone:
        print(f"{RED}❌ الرقم مطلوب!{RESET}")
        return

    email = input(f"{CYAN}📧 أدخل البريد الإلكتروني (اختياري - Enter للتخطي): {RESET}").strip()
    tiktok_user = input(f"{CYAN}📸 أدخل يوزر تيك توك (اختياري - Enter للتخطي): {RESET}").strip().replace('@','')

    print(f"\n{YELLOW}{'═'*50}{RESET}")
    print(f"{RED}🚀 بدء المسح الشامل{RESET}")
    print(f"{YELLOW}{'═'*50}{RESET}\n")

    print(f"\n{RED}[1/5]{RESET} {YELLOW}→ Phone Scanner{RESET}")
    print(f"{YELLOW}{'─'*50}{RESET}")
    try:
        phone_scanner.PhoneScanner(phone).run()
    except Exception as e:
        print(f"{RED}❌ {e}{RESET}")

    time.sleep(1)

    print(f"\n{RED}[2/5]{RESET} {YELLOW}→ Whisky OSINT{RESET}")
    print(f"{YELLOW}{'─'*50}{RESET}")
    try:
        whisky_osint.PhoneOSINT(phone).run_full_scan()
    except Exception as e:
        print(f"{RED}❌ {e}{RESET}")

    time.sleep(1)

    print(f"\n{RED}[3/5]{RESET} {YELLOW}→ Google Dorks{RESET}")
    print(f"{YELLOW}{'─'*50}{RESET}")
    try:
        dorks = google_dorks.generate('phone', phone)
        for d in dorks:
            print(f"   {GREEN}→{RESET} {d}")
    except Exception as e:
        print(f"{RED}❌ {e}{RESET}")

    time.sleep(1)

    if email:
        print(f"\n{RED}[4/5]{RESET} {YELLOW}→ Leak Checker{RESET}")
        print(f"{YELLOW}{'─'*50}{RESET}")
        try:
            leaks = leak_checker.check_email(email)
            if leaks:
                print(f"{RED}🚨 {len(leaks)} تسريب موجود!{RESET}")
                for l in leaks:
                    print(f"   • {l.get('Name')} ({l.get('BreachDate')})")
            else:
                print(f"{GREEN}✅ لا تسريبات{RESET}")
        except Exception as e:
            print(f"{RED}❌ {e}{RESET}")

    if tiktok_user:
        print(f"\n{RED}[5/5]{RESET} {YELLOW}→ TikTok OSINT{RESET}")
        print(f"{YELLOW}{'─'*50}{RESET}")
        try:
            data = tiktok_osint.get_tiktok_info(tiktok_user)
            r = data.get('result', {})
            print(f"   {GREEN}✅ اليوزر: @{r.get('uniqueId')}{RESET}")
            print(f"   {GREEN}✅ الاسم: {r.get('nickName')}{RESET}")
            print(f"   {GREEN}✅ المعجبون: {r.get('fans')}{RESET}")
        except Exception as e:
            print(f"{RED}❌ {e}{RESET}")

    print(f"\n{GREEN}{'═'*50}{RESET}")
    print(f"{GREEN}✅ اكتمل المسح الشامل!{RESET}")
    print(f"{GREEN}{'═'*50}{RESET}")
