# Cultural greetings
CULTURAL_GREETINGS = {

    # A
    'ar': 'مرحباً! كيف يمكنني مساعدتك اليوم?',                     # Arabic

    # B
    'bg': 'Здравейте! Как мога да ви помогна днес?',               # Bulgarian
    'bn': 'হ্যালো! আজ আমি কীভাবে আপনাকে সাহায্য করতে পারি?',       # Bengali

    # C
    'cs': 'Ahoj! Jak vám mohu dnes pomoci?',                      # Czech

    # D
    'da': 'Hej! Hvordan kan jeg hjælpe dig i dag?',               # Danish
    'de': 'Guten Tag! Wie kann ich Ihnen heute helfen?',          # German

    # E
    'el': 'Γεια σας! Πώς μπορώ να σας βοηθήσω σήμερα;',           # Greek
    'en': 'Hello! How can I help you today?',                     # English
    'es': '¡Hola! ¿En qué puedo ayudarte hoy?',                   # Spanish
    'et': 'Tere! Kuidas saan teid täna aidata?',                  # Estonian

    # F
    'fa': 'سلام! امروز چگونه می‌توانم به شما کمک کنم؟',            # Persian
    'fi': 'Hei! Kuinka voin auttaa sinua tänään?',                # Finnish
    'fr': 'Bonjour! Comment puis-je vous aider?',                 # French

    # G
    'gu': 'નમસ્તે! આજે હું તમારી કેવી રીતે મદદ કરી શકું?',         # Gujarati

    # H
    'he': 'שלום! איך אני יכול לעזור לך היום?',                    # Hebrew
    'hi': 'नमस्ते (Namaste)! मैं आपकी क्या सहायता कर सकता हूँ?',   # Hindi
    'hr': 'Bok! Kako vam mogu pomoći danas?',                     # Croatian
    'hu': 'Szia! Hogyan segíthetek ma?',                           # Hungarian

    # I
    'id': 'Halo! Bagaimana saya bisa membantu Anda hari ini?',    # Indonesian
    'it': 'Ciao! Come posso aiutarti oggi?',                       # Italian

    # J
    'ja': 'こんにちは (Konnichiwa)! 何かお手伝いしましょうか？',   # Japanese

    # K
    'kn': 'ನಮಸ್ಕಾರ! ಇಂದು ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?',        # Kannadam
    'ko': '안녕하세요 (Annyeonghaseyo)! 무엇을 도와드릴까요?',      # Korean

    # L
    'lt': 'Sveiki! Kaip galiu jums padėti šiandien?',              # Lithuanian
    'lv': 'Sveiki! Kā es varu jums palīdzēt šodien?',              # Latvian

    # M
    'ml': 'ഹലോ! ഇന്ന് ഞാൻ നിങ്ങളെ എങ്ങനെ സഹായിക്കാം?',             # Malayalam
    'mr': 'नमस्कार (Namaskar)! मी तुम्हाला कशी मदत करू शकतो?',    # Marathi
    'ms': 'Halo! Bagaimana saya boleh membantu anda hari ini?',   # Malay

    # N
    'ne': 'नमस्ते! म तपाईंलाई आज कसरी मद्दत गर्न सक्छु?',           # Nepali
    'nl': 'Hallo! Hoe kan ik u vandaag helpen?',                   # Dutch
    'no': 'Hei! Hvordan kan jeg hjelpe deg i dag?',                # Norwegian

    # P
    'pa': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਅੱਜ ਤੁਹਾਡੀ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?',   # Punjabi
    'pl': 'Cześć! Jak mogę Ci dzisiaj pomóc?',                     # Polish
    'pt': 'Olá! Como posso ajudá-lo hoje?',                        # Portuguese

    # R
    'ro': 'Salut! Cum te pot ajuta astăzi?',                       # Romanian
    'ru': 'Привет! Чем я могу вам помочь сегодня?',                # Russian

    # S
    'si': 'හෙලෝ! අද මම ඔබට කෙසේ උදව් කළ හැකිද?',                  # Sinhala
    'sk': 'Ahoj! Ako vám môžem dnes pomôcť?',                      # Slovak
    'sl': 'Pozdravljeni! Kako vam lahko danes pomagam?',           # Slovenian
    'sr': 'Здраво! Како могу да вам помогнем данас?',              # Serbian
    'sv': 'Hej! Hur kan jag hjälpa dig idag?',                     # Swedish
    'sw': 'Habari! Ninawezaje kukusaidia leo?',                    # Swahili

    # T
    'ta': 'வணக்கம்! இன்று நான் உங்களுக்கு எப்படி உதவலாம்?',          # Tamil
    'te': 'హలో! ఈ రోజు నేను మీకు ఎలా సహాయం చేయగలను?',            # Telugu
    'th': 'สวัสดี! วันนี้ฉันสามารถช่วยอะไรคุณได้บ้าง?',           # Thai
    'tr': 'Merhaba! Bugün size nasıl yardımcı olabilirim?',        # Turkish

    # U
    'uk': 'Привіт! Чим я можу вам допомогти сьогодні?',            # Ukrainian
    'ur': 'ہیلو! میں آج آپ کی کیسے مدد کر سکتا ہوں؟',              # Urdu

    # V
    'vi': 'Xin chào! Hôm nay tôi có thể giúp gì cho bạn?',         # Vietnamese

    # Z
    'zh-cn': '你好 (Nǐ hǎo)! 今天我能为您做些什么？'               # Chinese (Simplified)
}


SUPPORTED_LANGS = sorted(CULTURAL_GREETINGS.keys())

print("Total Supported Languages:", len(SUPPORTED_LANGS))
print(SUPPORTED_LANGS)