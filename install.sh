#!/data/data/com.termux/files/usr/bin/bash

RED='\033[1;31m'
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
RESET='\033[0m'

clear
echo -e "${RED}"
cat << "EOF"
██╗    ██╗██╗  ██╗██╗███████╗██╗  ██╗███████╗██╗   ██╗
██║    ██║██║  ██║██║██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
██║ █╗ ██║███████║██║███████╗█████╔╝ █████╗   ╚████╔╝ 
██║███╗██║██╔══██║██║╚════██║██╔═██╗ ██╔══╝    ╚██╔╝  
╚███╔███╔╝██║  ██║██║███████║██║  ██╗███████╗   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
EOF
echo -e "${RESET}"
echo -e "${YELLOW}   WHISKEY MD - Installation Script${RESET}\n"

echo -e "${CYAN}[1/4]${RESET} تحديث Termux..."
pkg update -y && pkg upgrade -y

echo -e "${CYAN}[2/4]${RESET} تثبيت المتطلبات..."
pkg install -y python git

echo -e "${CYAN}[3/4]${RESET} تثبيت مكتبات Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${CYAN}[4/4]${RESET} إنشاء اختصار دائم..."
SHELL_RC="$HOME/.bashrc"
[ -f "$HOME/.zshrc" ] && SHELL_RC="$HOME/.zshrc"

if ! grep -q "whiskey-md" "$SHELL_RC" 2>/dev/null; then
    echo 'alias whiskey="cd ~/whiskey-md && python whiskey.py"' >> "$SHELL_RC"
fi

echo -e "\n${GREEN}✅ تم التثبيت بنجاح!${RESET}"
echo -e "${YELLOW}للتشغيل اكتب:${RESET} source $SHELL_RC && whiskey"
