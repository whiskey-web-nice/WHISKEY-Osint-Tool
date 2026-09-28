#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google Dorks Generator - توليد استعلامات بحث متقدمة"""

from datetime import datetime

RED, YELLOW, GREEN, CYAN, RESET = '\033[1;31m','\033[1;33m','\033[1;32m','\033[1;36m','\033[0m'

def generate(target_type, value):
    dorks = {
        'phone': [
            f'"{value}" site:facebook.com',
            f'"{value}" site:twitter.com',
            f'"{value}" site:instagram.com',
            f'"{value}" site:linkedin.com',
            f'"{value}" site:youtube.com',
            f'"{value}" site:tiktok.com',
            f'"{value}" site:pastebin.com',
            f'"{value}" site:github.com',
            f'"{value}" filetype:pdf',
            f'"{value}" filetype:docx',
            f'"{value}" filetype:xlsx',
            f'"{value}" intext:"phone"',
            f'"{value}" intext:"contact"',
            f'"{value}" inurl:"contact"',
        ],
        'email': [
            f'"{value}" site:facebook.com',
            f'"{value}" site:twitter.com',
            f'"{value}" site:linkedin.com',
            f'"{value}" site:github.com',
            f'"{value}" site:pastebin.com',
            f'"{value}" filetype:pdf',
            f'"{value}" intext:"password"',
            f'"{value}" ext:sql',
            f'"{value}" ext:log',
            f'"{value}" ext:env',
        ],
        'name': [
            f'"{value}" site:facebook.com',
            f'"{value}" site:linkedin.com',
            f'"{value}" site:twitter.com',
            f'"{value}" site:instagram.com',
            f'"{value}" filetype:pdf',
            f'"{value}" intitle:"CV"',
            f'"{value}" intitle:"resume"',
        ],
        'domain': [
            f'site:{value}',
            f'site:{value} filetype:pdf',
            f'site:{value} filetype:doc',
            f'site:{value} intitle:"index of"',
            f'site:{value} inurl:admin',
            f'site:{value} inurl:login',
            f'site:{value} ext:sql',
            f'site:{value} ext:env',
            f'site:{value} ext:log',
            f'site:{value} ext:bak',
            f'site:{value} inurl:"phpinfo.php"',
        ],
        'username': [
            f'"{value}" site:facebook.com',
            f'"{value}" site:twitter.com',
            f'"{value}" site:instagram.com',
            f'"{value}" site:github.com',
            f'"{value}" site:reddit.com',
            f'"{value}" site:stackoverflow.com',
        ]
    }
    return dorks.get(target_type, [])


def main():
    print(f"{YELLOW}اختر نوع الهدف:{RESET}")
    print(f"  {RED}[1]{RESET} 📱 رقم هاتف")
    print(f"  {RED}[2]{RESET} 📧 بريد إلكتروني")
    print(f"  {RED}[3]{RESET} 👤 اسم شخص")
    print(f"  {RED}[4]{RESET} 🌐 نطاق/موقع")
    print(f"  {RED}[5]{RESET} 🆔 يوزر نيم")

    choice = input(f"\n{CYAN}اختر [1-5]: {RESET}").strip()
    types = {'1':'phone', '2':'email', '3':'name', '4':'domain', '5':'username'}

    if choice not in types:
        print(f"{RED}❌ خيار غير صحيح!{RESET}")
        return

    value = input(f"{CYAN}أدخل القيمة: {RESET}").strip()
    if not value:
        print(f"{RED}❌ لم تدخل قيمة!{RESET}")
        return

    dorks = generate(types[choice], value)

    print(f"\n{YELLOW}═══════════ Google Dorks ═══════════{RESET}")
    for i, d in enumerate(dorks, 1):
        print(f"{GREEN}[{i:02d}]{RESET} {d}")

    print(f"\n{CYAN}💡 انسخ أي Dork والصقه في Google{RESET}")

    fname = f"dorks_{value.replace(' ','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(dorks))
    print(f"\n{GREEN}💾 تم الحفظ في: {fname}{RESET}")
