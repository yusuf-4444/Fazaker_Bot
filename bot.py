import asyncio
import schedule
import time
from threading import Thread
import random
from telegram import Bot
from telegram.ext import Application
from datetime import datetime

BOT_TOKEN = "8492798785:AAE3U_XrO3nz9HgEFh0RQk8gz2oIuINm8es"
CHANNEL_USERNAME = "@FazakerInNafaatAlZekra"

# الباقيات الصالحات - أذكار عامة
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

# أذكار الصباح
morning_azkar = [
    "أصبحنا وأصبح الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له",
    "اللهم بك أصبحنا، وبك أمسينا، وبك نحيا، وبك نموت، وإليك النشور",
    "اللهم إني أسألك خير هذا اليوم: فتحه، ونصره، ونوره، وبركته، وهداه",
    "رضيت بالله ربا، وبالإسلام دينا، وبمحمد صلى الله عليه وسلم نبيا",
    "اللهم عافني في بدني، اللهم عافني في سمعي، اللهم عافني في بصري",
]

# أذكار المساء
evening_azkar = [
    "أمسينا وأمسى الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له",
    "اللهم بك أمسينا، وبك أصبحنا، وبك نحيا، وبك نموت، وإليك المصير",
    "اللهم إني أسألك خير هذه الليلة: فتحها، ونصرها، ونورها، وبركتها، وهداها",
    "اللهم إنى أعوذ بك من الهم والحزن، وأعوذ بك من العجز والكسل",
    "أعوذ بكلمات الله التامات من شر ما خلق",
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

async def send_morning_azkar():
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        zikr = random.choice(morning_azkar)
        message = f"🌅 أذكار الصباح:\n{zikr}"
        await application.bot.send_message(chat_id=CHANNEL_USERNAME, text=message)
        print(f"✅ تم إرسال أذكار الصباح: {zikr}")
        print(f"⏰ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    except Exception as e:
        print(f"❌ خطأ في أذكار الصباح: {e}")

async def send_evening_azkar():
    try:
        application = Application.builder().token(BOT_TOKEN).build()
        zikr = random.choice(evening_azkar)
        message = f"🌇 أذكار المساء:\n{zikr}"
        await application.bot.send_message(chat_id=CHANNEL_USERNAME, text=message)
        print(f"✅ تم إرسال أذكار المساء: {zikr}")
        print(f"⏰ الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)
    except Exception as e:
        print(f"❌ خطأ في أذكار المساء: {e}")

def schedule_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    print("🕌 بدأ بوت الباقيات الصالحات...")
    print("📿 يرسل أذكار متنوعة حسب الوقت")
    print("🌅 أذكار الصباح: 6:00 صباحاً")
    print("🌇 أذكار المساء: 4:00 مساءً")
    print("🔄 أذكار عامة: كل 30 دقيقة")
    print("🤲 هذا البوت صدقة جارية ونشر للخير")
    print("=" * 60)

    # جدولة الأذكار العامة كل 30 دقيقة
    schedule.every(30).minutes.do(lambda: asyncio.run(send_zikr()))
    
    # جدولة أذكار الصباح الساعة 6 صباحاً
    schedule.every().day.at("06:00").do(lambda: asyncio.run(send_morning_azkar()))
    
    # جدولة أذكار المساء الساعة 4 مساءً
    schedule.every().day.at("16:00").do(lambda: asyncio.run(send_evening_azkar()))

    # بدء الجدولة في thread منفصل
    thread = Thread(target=schedule_loop)
    thread.daemon = True
    thread.start()

    # الحلقة الرئيسية
    try:
        while True:
            print("🔄 البوت شغال...")
            time.sleep(300)  # كل 5 دقائق يطبع
    except KeyboardInterrupt:
        print("🛑 تم إيقاف البوت - جزاك الله خيراً")

if __name__ == "__main__":
    main()