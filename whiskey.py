#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WHISKEY MD - OSINT TOOLKIT v1.0
أداة متكاملة لجمع المعلومات - تعمل على Termux / Pydroid3
"""

import os
import sys
import time

RED     = '\033[1;31m'
YELLOW  = '\033[1;33m'
GREEN   = '\033[1;32m'
CYAN    = '\033[1;36m'
RESET   = '\033[0m'
DIM     = '\033[2m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_skull():
    clear()
    print(f"""{RED}
    ██╗    ██╗██╗  ██╗██╗███████╗██╗  ██╗███████╗██╗   ██╗
    ██║    ██║██║  ██║██║██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
    ██║ █╗ ██║███████║██║███████╗█████╔╝ █████╗   ╚████╔╝ 
    ██║███╗██║██╔══██║██║╚════██║██╔═██╗ ██╔══╝    ╚██╔╝  
    ╚███╔███╔╝██║  ██║██║███████║██║  ██╗███████╗   ██║   
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   {RESET}
{YELLOW}                  ▓▓▓  M  D  ▓▓▓{RESET}
""")
    print(f"""{RED}                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}
{RED}                ▄▄██████████████████████▄▄{RESET}
{RED}              ▄████████████████████████████▄{RESET}
{RED}             ████████████████████████████████{RESET}
{RED}            ██████████████████████████████████{RESET}
{YELLOW}           ██████{RED}░░░░░░░░{YELLOW}██████{RED}░░░░░░░░{YELLOW}██████{RESET}
{YELLOW}           ██████{RED}░░{YELLOW}████{RED}░░{YELLOW}██████{RED}░░{YELLOW}████{RED}░░{YELLOW}██████{RESET}
{YELLOW}           ██████{RED}░░{YELLOW}████{RED}░░{YELLOW}██████{RED}░░{YELLOW}████{RED}░░{YELLOW}██████{RESET}
{YELLOW}           ██████{RED}░░░░░░░░{YELLOW}██████{RED}░░░░░░░░{YELLOW}██████{RESET}
{RED}            ██████████████████████████████████{RESET}
{RED}             ████████████████████████████████{RESET}
{YELLOW}              ██████{RED}░░░{YELLOW}██████{RED}░░░{YELLOW}██████{RESET}
{YELLOW}               ██████{RED}░{YELLOW}██████{RED}░{YELLOW}██████{RESET}
{YELLOW}                ████████████████████{RESET}
{YELLOW}                 ██{RED}▐▐▐▐{YELLOW}██{RED}▐▐▐▐{YELLOW}██{RESET}
{YELLOW}                 ██{RED}▐▐▐▐{YELLOW}██{RED}▐▐▐▐{YELLOW}██{RESET}
{YELLOW}                  ████▀▀▀▀████{RESET}
{RED}                   ▀▀▀    ▀▀▀{RESET}
""")
    print(f"{YELLOW}        ╔══════════════════════════════════════════╗{RESET}")
    print(f"{RED}        ║   🔥 WHISKEY MD - OSINT TOOLKIT 🔥       ║{RESET}")
    print(f"{YELLOW}        ║      أداة متكاملة لجمع المعلومات          ║{RESET}")
    print(f"{RED}        ║          Version 1.0 Premium             ║{RESET}")
    print(f"{YELLOW}        ╚══════════════════════════════════════════╝{RESET}")
    print()

def loading_animation():
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    messages = [
        "تحميل وحدة Phone Scanner...",
        "تحميل وحدة IP Tracker...",
        "تحميل وحدة Whisky OSINT...",
        "تحميل وحدة TikTok OSINT...",
        "تحميل وحدة Google Dorks...",
        "WHISKEY MD جاهز للإطلاق!"
    ]
    clear()
    print(f"\n\n{RED}        WHISKEY MD{RESET}\n")
    for msg in messages:
        for i in range(12):
            sys.stdout.write(f'\r{YELLOW}        {chars[i % len(chars)]} {msg}{RESET}')
            sys.stdout.flush()
            time.sleep(0.04)
    print(f'\r{GREEN}        ✅ تم تحميل جميع الأدوات بنجاح!{RESET}          ')
    time.sleep(0.7)

def run_tool(module_name, title):
    clear()
    print(f"{YELLOW}┌─────────────────────────────────────────────┐{RESET}")
    print(f"{YELLOW}│{RED}  🔧 {title:38}{YELLOW}│{RESET}")
    print(f"{YELLOW}└─────────────────────────────────────────────┘{RESET}\n")
    try:
        mod = __import__(f"modules.{module_name}", fromlist=['main'])
        if hasattr(mod, 'main'):
            mod.main()
        else:
            print(f"{RED}❌ الوحدة {module_name} لا تحتوي على دالة main(){RESET}")
    except Exception as e:
        print(f"{RED}❌ خطأ في تشغيل الأداة: {e}{RESET}")
    input(f"\n{YELLOW}اضغط Enter للعودة للقائمة الرئيسية...{RESET}")

def main_menu():
    while True:
        print_skull()
        print(f"{CYAN}  ┌──────────────────────────────────────────────┐{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[1]{RESET} 📱  Phone Scanner    {DIM}فحص رقم هاتف{RESET}       {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[2]{RESET} 🌐  IP Tracker       {DIM}تتبع عنوان IP{RESET}        {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[3]{RESET} 🔍  Whisky OSINT     {DIM}بحث متقدم عن رقم{RESET}    {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[4]{RESET} 📸  TikTok OSINT     {DIM}معلومات حساب تيك توك{RESET} {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[5]{RESET} 🕵️   Google Dorks     {DIM}توليد استعلامات بحث{RESET}  {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[6]{RESET} 🚨  Leak Checker     {DIM}فحص التسريبات{RESET}        {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[7]{RESET} ⚡  Full Scan         {DIM}تشغيل كل الأدوات{RESET}     {CYAN}│{RESET}")
        print(f"{CYAN}  │{RESET}  {RED}[0]{RESET} 🚪  Exit                                 {CYAN}│{RESET}")
        print(f"{CYAN}  └──────────────────────────────────────────────┘{RESET}")

        choice = input(f"\n{RED}  WHISKEY-MD{RESET} {YELLOW}»{RESET} ").strip()

        if   choice == '1': run_tool('phone_scanner', 'Phone Scanner')
        elif choice == '2': run_tool('ip_tracker',    'IP Tracker')
        elif choice == '3': run_tool('whisky_osint',  'Whisky OSINT')
        elif choice == '4': run_tool('tiktok_osint',  'TikTok OSINT')
        elif choice == '5': run_tool('google_dorks',  'Google Dorks Generator')
        elif choice == '6': run_tool('leak_checker',  'Leak Checker')
        elif choice == '7': run_tool('full_scan',     'Full Scan - All Tools')
        elif choice == '0':
            clear()
            print(f"\n\n{RED}        👋 إلى اللقاء يا محارب...{RESET}\n\n")
            sys.exit(0)
        else:
            print(f"{RED}  ❌ خيار غير صحيح!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        loading_animation()
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}  ⚠️ تم الإيقاف بواسطة المستخدم{RESET}\n")
        sys.exit(0)