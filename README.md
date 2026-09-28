# 🥃 WHISKEY MD

**أداة OSINT متكاملة لجمع المعلومات — تعمل على Termux / Linux / Pydroid3**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Termux](https://img.shields.io/badge/Platform-Termux-green.svg)](https://termux.com/)

---

## 📌 نظرة عامة

**WHISKEY MD** أداة OSINT متكاملة تحتوي على 7 أدوات مستقلة في واجهة واحدة.

> ⚠️ **للأغراض التعليمية واختبار الاختراق الأخلاقي فقط**

---

## 🔧 الأدوات المتوفرة

| # | الأداة | الوصف |
|---|--------|-------|
| 1 | 📱 **Phone Scanner** | فحص رقم الهاتف + كشف الحسابات المرتبطة |
| 2 | 🌐 **IP Tracker** | تتبع عنوان IP مع الموقع والخريطة |
| 3 | 🔍 **Whisky OSINT** | بحث متقدم عبر Truecaller + منصات التواصل |
| 4 | 📸 **TikTok OSINT** | جلب معلومات كاملة عن حساب تيك توك |
| 5 | 🕵️ **Google Dorks** | توليد استعلامات بحث متقدمة |
| 6 | 🚨 **Leak Checker** | فحص تسريبات البريد وكلمة المرور |
| 7 | ⚡ **Full Scan** | تشغيل جميع الأدوات على نفس الهدف |

---

## ⚙️ التثبيت

### على Termux

```bash
pkg update && pkg upgrade -y
pkg install -y python git
git clone https://github.com/USERNAME/whiskey-md.git
cd whiskey-md
pip install -r requirements.txt
python whiskey.py
```

### اختصار دائم

```bash
echo 'alias whiskey="cd ~/whiskey-md && python whiskey.py"' >> ~/.bashrc
source ~/.bashrc
whiskey
```

---

## ⚠️ إخلاء المسؤولية

هذه الأداة مخصصة للأغراض التعليمية واختبار الاختراق الأخلاقي فقط.
- لا تستخدمها ضد أهداف بدون إذن كتابي مسبق.
- المطوّر غير مسؤول عن أي سوء استخدام.

---

**Made with ❤️ by WHISKEY MD**
