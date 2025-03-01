import random
import string

def generate_combo(count, length, include_letters=False):
    combo_list = []
    
    for _ in range(count):
        if include_letters:
            characters = string.ascii_letters + string.digits  # أرقام + أحرف
        else:
            characters = string.digits  # أرقام فقط
        
        combo = ''.join(random.choice(characters) for _ in range(length))
        combo_list.append(combo)
    
    return combo_list

# استقبال إدخال المستخدم
count = int(input("كم عدد الكمبوهات التي تريد توليدها؟ "))
length = int(input("كم عدد الأحرف/الأرقام في كل كمبو؟ "))
include_letters = input("هل تريد تضمين الأحرف؟ (نعم/لا): ").strip().lower() == "نعم"

# توليد الكمبوهات
combos = generate_combo(count, length, include_letters)

# عرض النتائج
print("\n=== الكمبوهات المولدة ===")
for combo in combos:
    print(combo)