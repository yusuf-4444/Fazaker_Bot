import os
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
    "لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير",
    "لا حول ولا قوة إلا بالله العلي العظيم",
    "الله أكبر كبيراً، والحمد لله كثيراً، وسبحان الله بكرة وأصيلاً",
    "سبحان الله، والحمد لله، ولا إله إلا الله، والله أكبر",
    "اللهم صل وسلم وبارك على نبينا محمد و آله",
    "رب اغفر لي وتب علي إنك أنت التواب الرحيم",
    "اللهم إني أسألك العفو والعافية في الدنيا والآخرة",
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

    # الحلقة الرئيسية
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 تم إيقاف البوت - جزاك الله خيراً")

if __name__ == "__main__":
    main()