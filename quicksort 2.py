import os #عشان اقرأ الفايلات 
from datetime import datetime    #عشان اخد الوقت بتاريخ مفهوم
# -------------------------------------

def quick_sort(arr, key, left, right): #ال quick sort
    if left < right:

        pivot = partition(arr, key, left, right)
        quick_sort(arr, key, left, pivot - 1)
        quick_sort(arr, key, pivot + 1, right)

# تقسيم الاراي 
def partition(arr, key, left, right):
    pivot_value = arr[right][key]   # آخر عنصرg
    i = left - 1
# بعمل لوب مقارنه ب الpivot 
    for j in range(left, right):
        if arr[j][key] <= pivot_value:
            i += 1
            # بعمل swap
            arr[i], arr[j] = arr[j], arr[i]
            # بعمل swap لل pivot نفسه
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
# برجع index pivot
    return i + 1

# -------------------------------------

def get_files(path): # عشان اقرأ الفايلات
    files_info = [] #هنا بضيف الملفات في array

    for file in os.listdir(path): #هنا لوب عشان كل الفايلات تتقرا
        full_path = os.path.join(path, file) #بجيب مسار كل فايل

        if os.path.isfile(full_path): 
            size = os.path.getsize(full_path) #بحفظ حجم الفايل
            modified = os.path.getmtime(full_path) #بحفظ الوقت اللي اتعدل فيه

            files_info.append({
                "name": file, #اسم الفايل
                "size": size, # حجم الفايل
                "modified": modified #تاريخ التعديل
            })

    return files_info # برجع الاراي بتاعت الفايلات
# -------------------------------------
# تشغيل الكود
folder_path = r"C:\Users\m\OneDrive\Desktop\files" #مسار الفولدر الكبير
files = get_files(folder_path) #دي الفايلات نفسها

# بعرف متغير علي حسب ال sort
sorted_by_size = files.copy()
sorted_by_date = files.copy()

# array = files , key=size 
# left 0 , right الحجم -1 
# عشان قرأ كل الفايلات
quick_sort(sorted_by_size, "size", 0, len(sorted_by_size) - 1) 
# array = files , key=modified 
# left 0 , right الحجم -1 
# عشان قرأ كل الفايلات
quick_sort(sorted_by_date, "modified", 0, len(sorted_by_date) - 1)

# هنا ب لطبع الترتيب تبعا للحجم
print("Sorted by size:")
for f in sorted_by_size:
    print(f"{f['name']} — {f['size']} bytes")#بطبع اسم الفايل وحجمه


print("\nSorted by date:")
for f in sorted_by_date:
    date = datetime.fromtimestamp(f['modified']) #بحول الوقت لتاريخ مفهوم
    print(f"{f['name']} — {date}") #بطبع اسم الفايل وتاريخ تعديله