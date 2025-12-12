import os #عشان اقرا الفايلات
from datetime import datetime   #عشان اقرا التاريخ 
# -------------------------------------
def quick_sort(arr, key):    #كود quick sort
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # آخر عنصر
    pivot_value = pivot[key]

    left = [] #اصغر من pivot
    mid = []  #لو = قيمة pivot
    right = [] #اكبر من pivot

    for item in arr:
        value = item[key]
        if value < pivot_value:
            left.append(item)
        elif value > pivot_value:
            right.append(item)
        else:
            mid.append(item)

    return quick_sort(left, key) + mid + quick_sort(right, key) #بنرجع array كامله

# -------------------------------------
# قراءة الملفات
# -------------------------------------
def get_files(path): # هنا بياخد مسار الفايلات
    files_info = [] #بحفظ الفايلات في اراي

    for file in os.listdir(path):  
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path) # بيحفظ الحجم 
            modified = os.path.getmtime(full_path) # بيحفظ التاريخ

            files_info.append({  #بعد قراءه كل فايل يحطه في الاراي
                "name": file,
                "size": size, #الحجم
                "modified": modified #التاريخ للتعديل 
            })

    return files_info
# -------------------------------------
# بنجرب الكود 
folder_path = r"C:\Users\m\OneDrive\Desktop\files"   #مسار الفولدر
files = get_files(folder_path) # هنا بيقرأ الملفات

sorted_by_size = quick_sort(files, "size")
sorted_by_date = quick_sort(files, "modified")

print("Sorted by SIZE:")
for f in sorted_by_size:
    print(f"{f['name']} — {f['size']} bytes")

print("\n Sorted by DATE:")
for f in sorted_by_date:
    date = datetime.fromtimestamp(f['modified'])
    print(f"{f['name']} — {date}")