# -----------------------------
# بيانات التدريب
# -----------------------------
messages = [
    ("Free gift waiting for you", "Spam"),
    ("Your account is hacked", "Spam"),
    ("Claim your reward now", "Spam"),
    ("Free gift waiting for you", "Spam"),
    ("Let's meet tomorrow", "Ham"),
    ("Call me when you are free", "Ham")
]

# -----------------------------
# فصل الرسائل
# -----------------------------
spam_messages = []
ham_messages = []

for text, label in messages:
    if label == "Spam":
        spam_messages.append(text.lower())
    else:
        ham_messages.append(text.lower())

# -----------------------------
# الاحتمالات الأولية (Prior)
# -----------------------------
p_spam = len(spam_messages) / len(messages) #4/6=0.6666
p_ham  = len(ham_messages) / len(messages) #2/6=0.3333

print("Step 1: Prior Probabilities")
print("P(Spam) =", p_spam)
print("P(Ham)  =", p_ham)
print("-" * 50)

# -----------------------------
# عدّ الكلمات
# -----------------------------
spam_words = {}
ham_words = {}

for msg in spam_messages: #msg = "free gift waiting for you"
    for word in msg.split(): #["free", "gift", "waiting", "for", "you"]
        #عدّ عدد مرات ظهور كل كلمة داخل رسائل Spam
        spam_words[word] = spam_words.get(word, 0) + 1 #spam_words = {"free": 2,    "gift": 2, "your": 2}

for msg in ham_messages:
    for word in msg.split():
        ham_words[word] = ham_words.get(word, 0) + 1

total_spam_words = sum(spam_words.values()) #18
total_ham_words  = sum(ham_words.values())#9

# -----------------------------
# Vocabulary
# -----------------------------
# set يحذف التكرار تلقائيًا
vocab = set(list(spam_words.keys()) + list(ham_words.keys())) #12+5 =19
#يحسب عدد الكلمات المختلفة
vocab_size = len(vocab) #19

print("Step 2: Vocabulary Size =", vocab_size)
print("-" * 50)

# -----------------------------
# إدخال المستخدم
# -----------------------------
user_message = input("Enter a message to classify: ")
test_words = user_message.lower().split()

print("\nMessage Words:", test_words)
print("-" * 50)

# -----------------------------
# تطبيق قانون بايز
# -----------------------------
spam_prob = p_spam #0.6666
ham_prob  = p_ham #=0.3333

print("Step 3: Bayes Calculation")
print("Word\t\tP(word|Spam)\tP(word|Ham)")
print("-" * 50)

for word in test_words:
    p_word_spam = (spam_words.get(word, 0) + 1) / (total_spam_words + vocab_size) #2+1/18+19=0.0813 #1+117+19=0.054
    p_word_ham  = (ham_words.get(word, 0) + 1) / (total_ham_words + vocab_size)#1+1/9+19=0.0714#0+19+19=0.035

    spam_prob *= p_word_spam #0.666*0.8103*0.054=0.0029
    ham_prob  *= p_word_ham#0.333*0.0714*0.035=0.00085

    print(f"{word:<10}\t{p_word_spam:.5f}\t\t{p_word_ham:.5f}")

print("-" * 50)

# -----------------------------
# النتائج النهائية
# -----------------------------
print("Final Bayes Results:")
print("Spam Probability =", spam_prob)
print("Ham Probability  =", ham_prob)

if spam_prob > ham_prob:
    print("Prediction: Spam ")
else:
    print("Prediction: Ham ")


