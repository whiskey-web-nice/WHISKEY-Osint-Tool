#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phone Scanner - أداة فحص رقم الهاتف"""

import requests, json, re, time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

class PhoneScanner:
    def __init__(self, phone):
        self.phone = re.sub(r'[^0-9+]', '', phone)
        self.results = {"number": self.phone, "timestamp": datetime.now().isoformat()}
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36'})

    def check_validity(self):
        api_key = "eb81e04cb49e52d6ca7c7c8bd97b2816"
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={self.phone}"
        try:
            r = self.session.get(url, timeout=10)
            if r.status_code == 200:
                d = r.json()
                if d.get('valid'):
                    self.results.update({
                        'valid': True,
                        'location': d.get('location'),
                        'carrier': d.get('carrier'),
                        'country': d.get('country_name'),
                        'line_type': d.get('line_type')
                    })
                    return True
        except: pass
        return False

    def check_social(self):
        plats = {
            'WhatsApp': f'https://wa.me/{self.phone.replace("+","")}',
            'Telegram': f'https://t.me/{self.phone.replace("+","")}',
            'Facebook': f'https://www.facebook.com/search/top/?q={self.phone}',
            'Twitter':  f'https://twitter.com/search?q={self.phone}',
            'Instagram':f'https://www.instagram.com/explore/tags/{self.phone.replace("+","")}',
            'TikTok':   f'https://www.tiktok.com/@{self.phone.replace("+","")}',
        }
        found = []
        for name, url in plats.items():
            try:
                r = self.session.get(url, timeout=6, allow_redirects=True)
                found.append({'platform': name, 'url': url, 'status': r.status_code})
            except:
                found.append({'platform': name, 'url': url, 'status': 'timeout'})
            time.sleep(0.3)
        self.results['social_media'] = found
        return found

    def generate_dorks(self):
        dorks = [
            f'"{self.phone}" site:facebook.com',
            f'"{self.phone}" site:twitter.com',
            f'"{self.phone}" site:linkedin.com',
            f'"{self.phone}" site:instagram.com',
            f'"{self.phone}" site:pastebin.com',
            f'"{self.phone}" filetype:pdf',
            f'"{self.phone}" filetype:docx',
            f'"{self.phone}" intext:"phone"',
        ]
        self.results['google_dorks'] = dorks
        return dorks

    def run(self):
        print(f"{CYAN}[*] جاري فحص الرقم: {YELLOW}{self.phone}{RESET}\n")
        with ThreadPoolExecutor(max_workers=2) as ex:
            futures = [
                ex.submit(self.check_validity),
                ex.submit(self.check_social),
            ]
            for f in as_completed(futures):
                try: f.result()
                except Exception as e: print(f"{RED}[!] {e}{RESET}")
        self.generate_dorks()

        print(f"\n{YELLOW}═══════════ نتيجة الفحص ═══════════{RESET}")
        if self.results.get('valid'):
            print(f"{GREEN}✅ الرقم صالح{RESET}")
            print(f"{CYAN}   الدولة    :{RESET} {self.results.get('country','?')}")
            print(f"{CYAN}   المشغل    :{RESET} {self.results.get('carrier','?')}")
            print(f"{CYAN}   الموقع     :{RESET} {self.results.get('location','?')}")
            print(f"{CYAN}   النوع      :{RESET} {self.results.get('line_type','?')}")
        else:
            print(f"{RED}❌ لم يتم التحقق من الرقم عبر API{RESET}")

        print(f"\n{YELLOW}🌐 الحسابات المرتبطة:{RESET}")
        for s in self.results.get('social_media', []):
            icon = "✅" if s['status'] == 200 else "❌"
            print(f"   {icon} {s['platform']:10} → {s['url']}")

        print(f"\n{YELLOW}🔍 Google Dorks المقترحة:{RESET}")
        for d in self.results['google_dorks']:
            print(f"   → {d}")

        fname = f"phone_{self.phone.replace('+','')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"\n{GREEN}💾 تم الحفظ في: {fname}{RESET}")


def main():
    phone = input(f"{CYAN}📱 أدخل رقم الهاتف (مثال: +201234567890): {RESET}").strip()
    if not phone:
        print(f"{RED}❌ لم تدخل رقماً!{RESET}")
        return
    PhoneScanner(phone).run()
