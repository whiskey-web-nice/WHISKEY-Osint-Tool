#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Whisky OSINT - بحث متقدم عن رقم الهاتف"""

import requests, json, re, time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
except ImportError:
    phonenumbers = None

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36",
]

class PhoneOSINT:
    def __init__(self, phone_number):
        self.phone = self.clean_phone(phone_number)
        self.results = {
            'phone': self.phone,
            'metadata': {},
            'api_results': {},
            'timestamp': datetime.now().isoformat()
        }
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENTS[0]})

    def clean_phone(self, phone):
        phone = str(phone).strip()
        phone = re.sub(r'[^\d+]', '', phone)
        if not phone.startswith('+'):
            if phone.startswith('00'):
                phone = '+' + phone[2:]
            else:
                phone = '+' + phone
        return phone

    def get_metadata(self):
        if not phonenumbers:
            return {'error': 'phonenumbers not installed'}
        try:
            parsed = phonenumbers.parse(self.phone)
            metadata = {
                'country_code': phonenumbers.region_code_for_number(parsed),
                'country_name_ar': geocoder.description_for_number(parsed, 'ar'),
                'country_name_en': geocoder.description_for_number(parsed, 'en'),
                'carrier_en': carrier.name_for_number(parsed, 'en'),
                'carrier_ar': carrier.name_for_number(parsed, 'ar'),
                'timezones': list(timezone.time_zones_for_number(parsed)),
                'is_valid': phonenumbers.is_valid_number(parsed),
                'is_possible': phonenumbers.is_possible_number(parsed),
                'international_format': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                'e164_format': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
            }
            self.results['metadata'] = metadata
            return metadata
        except Exception as e:
            return {'error': str(e)}

    def search_truecaller(self):
        try:
            url = f"https://www.truecaller.com/search/eg/{self.phone.replace('+','')}"
            r = self.session.get(url, timeout=10)
            if r.status_code == 200:
                return {'status': 'checked', 'url': url}
            return None
        except Exception as e:
            return {'error': str(e)}

    def search_telegram(self):
        try:
            username = self.phone.replace('+', '')
            url = f"https://t.me/{username}"
            r = self.session.get(url, timeout=10)
            if r.status_code == 200 and 'tgme_page_title' in r.text:
                return {'username': username, 'found': True, 'url': url}
            return None
        except Exception as e:
            return {'error': str(e)}

    def search_whatsapp(self):
        try:
            url = f"https://wa.me/{self.phone.replace('+','')}"
            r = self.session.get(url, timeout=10)
            if r.status_code == 200:
                self.results['api_results']['whatsapp'] = {'status': 'exists', 'url': url}
                return {'status': 'exists', 'url': url}
            return None
        except Exception as e:
            return {'error': str(e)}

    def run_full_scan(self):
        print(f"\n{CYAN}🔍 بدء OSINT للرقم: {YELLOW}{self.phone}{RESET}")
        print("=" * 60)

        print(f"{CYAN}📊 جلب المعلومات الأساسية...{RESET}")
        metadata = self.get_metadata()
        if metadata and 'error' not in metadata:
            print(f"   {GREEN}✅ الدولة: {metadata.get('country_name_ar', '?')}")
            print(f"   {GREEN}✅ المشغل: {metadata.get('carrier_ar', metadata.get('carrier_en', '?'))}")
            print(f"   {GREEN}✅ صالح: {'نعم' if metadata.get('is_valid') else 'لا'}")

        print(f"{CYAN}✈️  التحقق من Telegram...{RESET}")
        tg = self.search_telegram()
        if tg and tg.get('found'):
            print(f"   {GREEN}✅ موجود على Telegram{RESET}")

        print(f"{CYAN}💬 التحقق من WhatsApp...{RESET}")
        wa = self.search_whatsapp()
        if wa and wa.get('status') == 'exists':
            print(f"   {GREEN}✅ موجود على WhatsApp{RESET}")

        print("=" * 60)
        print(f"{GREEN}✅ اكتمل OSINT!{RESET}")
        return self.results


def main():
    phone = input(f"{CYAN}🔍 أدخل رقم الهاتف (مثال: +201234567890): {RESET}").strip()
    if not phone:
        print(f"{RED}❌ الرقم مطلوب!{RESET}")
        return

    osint = PhoneOSINT(phone)
    result = osint.run_full_scan()

    filename = f"whisky_{phone.replace('+','')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n{GREEN}💾 تم حفظ التقرير في: {filename}{RESET}")
