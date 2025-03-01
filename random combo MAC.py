import random

def generate_mac():
    """توليد عنوان MAC عشوائي بصيغة 00:1A:79:XX:XX:XX"""
    prefix = "00:1A:79"
    mac = [prefix] + ["{:02X}".format(random.randint(0, 255)) for _ in range(3)]
    return ":".join(mac)

# طلب عدد العناوين التي يرغب المستخدم في توليدها
num_macs = int(input("أدخل عدد عناوين MAC التي ترغب في توليدها: "))

# طلب اسم الملف الذي سيتم حفظ النتائج فيه
file_name = input("أدخل اسم الملف لحفظ النتائج (مثال: mac_addresses.txt): ")

# توليد العناوين وحفظها في الملف
with open(file_name, 'w') as file:
    for _ in range(num_macs):
        mac_address = generate_mac()
        file.write(mac_address + "\n")

print(f"تم حفظ {num_macs} عنوان MAC في الملف {file_name}.")