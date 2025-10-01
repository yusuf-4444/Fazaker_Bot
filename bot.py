import asyncio
import schedule
import time
from threading import Thread
import random
from telegram import Bot
from telegram.ext import Application

BOT_TOKEN = "8492798785:AAE3U_XrO3nz9HgEFh0RQk8gz2oIuINm8es"
CHANNEL_USERNAME = "@FazakerInNafaatAlZekra"

# الباقيات الصالحات - مجموعة من الأذكار والأدعية
baqiyat_salihat = [
    "أستغفر الله وأتوب إليه",
    "سبحان الله وبحمده، سبحان الله العظيم",
    # ... باقي الأذكار
]

async def send_zikr():
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        zikr = random.choice(baqiyat_salihat)
        await application.bot.send_message(chat_id=CHANNEL_USERNAME, text=zikr)
        print(f"✅ تم إرسال الذكر: {zikr}")
        print(f"⏰ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    except Exception as e:
        print(f"❌ خطأ: {e}")

def schedule_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    print("🕌 بدأ بوت الباقيات الصالحات...")
    print("📿 يرسل أذكار واستغفار كل 30 دقيقة")
    print("🤲 هذا البوت صدقة جارية ونشر للخير")
    print("=" * 60)

    # جدولة الإرسال كل 30 دقيقة
    schedule.every(30).minutes.do(lambda: asyncio.run(send_zikr()))

    # بدء الجدولة في thread منفصل
    thread = Thread(target=schedule_loop)
    thread.daemon = True
    thread.start()

    # الحلقة الرئيسية - هذا مهم!
    try:
        # طلب مستمر عشان Railway ميقفش البوت
        while True:
            print("🔄 البوت شغال...")
            time.sleep(300)  # كل 5 دقائق يطبع
    except KeyboardInterrupt:
        print("🛑 تم إيقاف البوت - جزاك الله خيراً")

if __name__ == "__main__":
    main()