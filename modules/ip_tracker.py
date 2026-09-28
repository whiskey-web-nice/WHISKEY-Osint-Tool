#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IP Tracker - أداة تتبع عنوان IP"""

import requests, json
from datetime import datetime

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

def track_ip(ip=None):
    url = f"http://ip-api.com/json/{ip or ''}?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
    try:
        r = requests.get(url, timeout=10)
        return r.json()
    except Exception as e:
        return {'status': 'fail', 'message': str(e)}

def main():
    ip = input(f"{CYAN}🌐 أدخل عنوان IP (أو اتركه فارغاً لعنوان جهازك): {RESET}").strip()
    print(f"\n{YELLOW}[*] جاري تتبع العنوان...{RESET}\n")

    data = track_ip(ip if ip else None)

    if data.get('status') != 'success':
        print(f"{RED}❌ فشل التتبع: {data.get('message')}{RESET}")
        return

    print(f"{YELLOW}═══════════ معلومات IP ═══════════{RESET}")
    print(f"{CYAN}📍 IP          :{RESET} {data.get('query')}")
    print(f"{CYAN}🌍 القارة       :{RESET} {data.get('continent')}")
    print(f"{CYAN}🏳️  الدولة       :{RESET} {data.get('country')} ({data.get('countryCode')})")
    print(f"{CYAN}🗺️  المنطقة      :{RESET} {data.get('regionName')}")
    print(f"{CYAN}🏙️  المدينة      :{RESET} {data.get('city')}")
    print(f"{CYAN}📮 الرمز البريدي:{RESET} {data.get('zip')}")
    print(f"{CYAN}📌 الإحداثيات   :{RESET} {data.get('lat')}, {data.get('lon')}")
    print(f"{CYAN}🕒 التوقيت      :{RESET} {data.get('timezone')}")
    print(f"{CYAN}📡 ISP          :{RESET} {data.get('isp')}")
    print(f"{CYAN}🏢 المنظمة      :{RESET} {data.get('org')}")
    print(f"{CYAN}🔢 AS           :{RESET} {data.get('as')}")
    print(f"{CYAN}📱 محمول؟       :{RESET} {'نعم' if data.get('mobile') else 'لا'}")
    print(f"{CYAN}🛡️  بروكسي؟      :{RESET} {'نعم' if data.get('proxy') else 'لا'}")
    print(f"{CYAN}🖥️  استضافة؟     :{RESET} {'نعم' if data.get('hosting') else 'لا'}")
    print(f"{CYAN}🔗 DNS عكسي    :{RESET} {data.get('reverse') or 'غير متوفر'}")

    lat, lon = data.get('lat'), data.get('lon')
    if lat and lon:
        print(f"\n{GREEN}🗺️  الخريطة: {RESET}https://www.google.com/maps?q={lat},{lon}")

    fname = f"ip_{data.get('query','unknown')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n{GREEN}💾 تم الحفظ في: {fname}{RESET}")
