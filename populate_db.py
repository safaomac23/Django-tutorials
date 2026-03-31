import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anket_sistemi.settings')
django.setup()

from django.contrib.auth.models import User
from anketler.models import Poll, Question, Choice

# Veritabanını temizle
Poll.objects.all().delete()
Question.objects.all().delete()
Choice.objects.all().delete()

# Superuser oluştur
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# Yeni Futbol Anketi oluştur
p = Poll.objects.create(title="Büyük Futbol Anketi", pub_date=timezone.now())

futbol_sorulari = [
    {
        "soru": "Tüm zamanların en iyi futbolcusu (GOAT) kimdir?",
        "secenekler": ["Lionel Messi", "Cristiano Ronaldo", "Pele", "Diego Maradona"]
    },
    {
        "soru": "Size göre dünyanın en rekabetçi ligi hangisidir?",
        "secenekler": ["Premier Lig", "La Liga", "Serie A", "Süper Lig"]
    },
    {
        "soru": "Türkiye'nin Avrupa'daki en başarılı kulübü hangisidir?",
        "secenekler": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"]
    },
    {
        "soru": "Tarihteki en unutulmaz Şampiyonlar Ligi finali hangisiydi?",
        "secenekler": ["2005 İstanbul (Milan 3-3 Liverpool)", "1999 Camp Nou (Man Utd 2-1 Bayern)", "2014 Lizbon (Real Madrid 4-1 Atletico)"]
    },
    {
        "soru": "Etkileyici taraftar atmosferine sahip stadyum hangisidir?",
        "secenekler": ["Anfield (Liverpool)", "Signal Iduna Park (Dortmund)", "Santiago Bernabeu (Real Madrid)", "Nef Stadyumu (Galatasaray)"]
    },
    {
        "soru": "Modern futbolun en iyi teknik direktörü kimdir?",
        "secenekler": ["Pep Guardiola", "Carlo Ancelotti", "Jurgen Klopp", "Jose Mourinho"]
    },
    {
        "soru": "Hangi mevkide oynamak oyun zekasını daha çok ön plana çıkarır?",
        "secenekler": ["Oyun Kurucu / 10 Numara", "Stoper / Oyun Kuran Defans", "Merkez Orta Saha (Box to box)", "Kaleci"]
    },
    {
        "soru": "Futbol tarihinde en estetik çalımları atan oyuncu kimdir?",
        "secenekler": ["Ronaldinho", "Neymar", "Zinedine Zidane", "Lionel Messi"]
    },
    {
        "soru": "Dünya futbol tarihindeki en dominant takım hangisiydi?",
        "secenekler": ["2009-2011 Barcelona", "2016-2018 Real Madrid", "1970 Brezilya Milli Takımı", "1990'lar Milan"]
    },
    {
        "soru": "VAR (Video Yardımcı Hakem) sistemi sizce futbola iyi mi geldi?",
        "secenekler": ["Evet, oyunu adilleştirdi.", "Hayır, futbolun ruhunu ve akışını öldürdü.", "Kısmen, ama daha fazla geliştirilmeli."]
    }
]

for item in futbol_sorulari:
    q = Question.objects.create(poll=p, question_text=item['soru'])
    for secenek in item['secenekler']:
        Choice.objects.create(question=q, choice_text=secenek, votes=0)

print("Database populated successfully with Football Poll Data.")
