import requests
import datetime
import pytz
import jdatetime
from config import ASSETS, BOT_TOKEN_BALE, CHANNEL_ID_BALE, TOKEN_RUBIKA, CHANNEL_ID_RUBIKA, TOKEN_TELEGRAM, CHAT_ID_TELEGRAM


def get_persian_datetime_str():
    tehran_tz = pytz.timezone("Asia/Tehran")
    now = datetime.datetime.now(tehran_tz)
    shamsi = jdatetime.datetime.fromgregorian(datetime=now)
    return shamsi.strftime("%Y-%m-%d %H:%M")


def get_category_emoji(key):
    if key in ["ounce", "silver"]:
        return "🥇"
    if key in ["geram18", "geram740", "bazartehran", "shemsh1", "parsian1"]:
        return "🟡"
    if key in ["sekkejad", "sekkenim", "sekkerob", "sekkegad", "sekke-arzesh", "hobab"]:
        return "🪙"
    if key == "BTC_USDT": return "₿"
    if key == "ETH_USDT": return "✳️"
    if key in ["USDT_IRT", "try", "omr"]: return "💵"
    if key == "ENERGY_BRENT": return "🛢"
    return "▫️"


def format_message(data_pairs):
    msg = "📊 گزارش لحظه‌ای بازار\n"
    msg += "────────────────────\n"
    
    for key, name, rate in data_pairs:
        emoji = get_category_emoji(key)
        msg += f"{emoji} {name}: {rate}\n"
    
    msg += "────────────────────\n"
    msg += "🕒 آپدیت خودکار\n"
    msg += f"🕒 {get_persian_datetime_str()}\n"
    msg += "🆔 @dolarrr_online"
    
    return msg


def send_to_bale(message):
    url = f"https://tapi.bale.ai/bot{BOT_TOKEN_BALE}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID_BALE, "text": message, "parse_mode": "HTML"})


def send_to_rubika(message):
    url = f"https://botapi.rubika.ir/v3/{TOKEN_RUBIKA}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL_ID_RUBIKA, "text": message, "parse_mode": "HTML"})


def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    data = {
        "chat_id": CHAT_ID_TELEGRAM,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    requests.post(url, data=data, timeout=15)


def fetch_prices():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "fa,en;q=0.9",
    })

    try:
        response = session.get("https://www.tala.ir/banner/", timeout=30)
        data = response.json()
        prices = data.get("price", {})

        collected = [(key, name, prices.get(key, "ناموجود")) for key, name in ASSETS.items()]

        message = format_message(collected)
        print(message)

        send_to_bale(message)
        send_to_rubika(message)
        send_to_telegram(message)

    except Exception as e:
        print(f"خطا: {e}")


if __name__ == "__main__":
    fetch_prices()
