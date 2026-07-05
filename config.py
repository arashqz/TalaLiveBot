import os
from dotenv import load_dotenv

load_dotenv()

# ================== تنظیمات ==================
BOT_TOKEN_BALE = os.getenv("BOT_TOKEN_BALE")
CHANNEL_ID_BALE = os.getenv("CHANNEL_ID_BALE")

TOKEN_RUBIKA = os.getenv("TOKEN_RUBIKA")
CHANNEL_ID_RUBIKA = os.getenv("CHANNEL_ID_RUBIKA")

TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
CHAT_ID_TELEGRAM = os.getenv("CHAT_ID_TELEGRAM")

# لیست دارایی‌ها
ASSETS = {
    "USDT_IRT": "تتر",
    "ounce": "اونس طلا",
    "bazartehran": "مثقال طلا",
    "geram18": "طلای 18 عیار",
    "sekkejad": "سکه امامی",
    "sekkegad": "سکه بهار آزادی",
    "sekkenim": "نیم سکه",
    "sekkerob": "ربع سکه",
    "silver": "اونس نقره",
    "shemsh1": "شمش 1 گرمی",
    "parsian1": "طلای پارسیان",
    "geram740": "طلای آبشده",
    "BTC_USDT": "بیت کوین",
    "ETH_USDT": "اتریوم",
    "ENERGY_BRENT": "نفت برنت",
    "try": "لیر ترکیه",
    "omr": "ریال عمان",
    "hobab": "حباب سکه",
    "sekke-arzesh": "ارزش ذاتی سکه"
}
