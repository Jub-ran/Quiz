import pandas as pd
import numpy as np

# إنشاء جدول البيانات (DataFrame)
data = {
    'Transaction_ID': [1001, 1002, 1003, 1004, 1005, 1006],
    'Customer_Name': ['Ahmed Ali', 'Sara Omar', 'Ali Saleh', 'Nada Hassan', 'Omar Khalid', 'Ahmed Ali'],
    'Age': [28, np.nan, 35, 42, np.nan, 28],
    'Email': ['ahmed@mail.com', 'sara@mail.com', np.nan, 'nada@mail.com', 'omar@mail.com', 'ahmed@mail.com'],
    'Join_Date': ['2025-01-10', '2025-02-15', '2025-03-20', '2025-05-05', '2025-01-10', '2025-01-10'], # Corrected dates based on common patterns
    'Total_Purchase': [250, 300, 150, 400, np.nan, 250]
}
df = pd.DataFrame(data)

print("--- الجدول الأصلي ---")
print(df)
print("\n" + "="*30 + "\n")

# --- الجزء الأول: أوامر Pandas ---

print("--- 1. تحويل عمود Join_Date إلى تاريخ ---")
df['Join_Date'] = pd.to_datetime(df['Join_Date'])
print(df.dtypes)
print("\n")

print("--- 2. تحديد الصفوف التي فيها أكثر من قيمة فارغة ---")
rows_with_more_than_one_null = df[df.isnull().sum(axis=1) > 1]
print(rows_with_more_than_one_null)
print("\n")

print("--- 3. معرفة نوع البيانات وعدد الصفوف والأعمدة ---")
df.info()
print("\n")

print("--- 4. التحقق من عدد القيم الفارغة في كل عمود ---")
null_values_per_column = df.isnull().sum()
print(null_values_per_column)
print("\n")

print("--- 5. تحديد الصفوف التي العمر فيها > من 30 سنة ---")
customers_over_30 = df[df['Age'] > 30]
print(customers_over_30)
print("\n")

print("--- 6. معرفة كم صف يتبقى بعد حذف الصفوف التي تحتوي على أي قيم فارغة ---")
rows_after_dropping_nulls = len(df.dropna())
print(f"عدد الصفوف المتبقية بعد حذف القيم الفارغة: {rows_after_dropping_nulls}")
print("\n")

print("--- 7. استبدال القيم الفارغة في عمود Age بالمتوسط ---")
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
print("القيم الفارغة في عمود Age بعد استبدالها بالمتوسط:")
print(df)
print("\n")

print("--- 8. استبدال القيم الفارغة في عمود Total_Purchase بالرقم 0 ---")
df['Total_Purchase'].fillna(0, inplace=True)
print("القيم الفارغة في عمود Total_Purchase بعد استبدالها بالصفر:")
print(df)
print("\n")

print("--- 9. معرفة الصفوف المتكررة قبل حذفها ---")
duplicated_rows_before = df[df.duplicated(keep=False)] # keep=False يظهر كل التكرارات
print(duplicated_rows_before)
print("\n")

print("--- 10. إزالة الصفوف المتكررة ---")
df.drop_duplicates(inplace=True)
print("الجدول بعد إزالة الصفوف المتكررة:")
print(df)
print("\n" + "="*30 + "\n")

# --- الجزء الثاني: إجابات الأسئلة التحليلية (مطبوعة من الكود) ---

print("--- إجابات الأسئلة التحليلية ---\n")

print("1. الأعمدة التي تحتاج تنظيف هي Age, Email, Total_Purchase لأنها تحتوي على قيم فارغة (NaN)، وعمود Join_Date لأنه من نوع نصي ويجب تحويله إلى تاريخ للتحليل الزمني.\n")

print("2. أثر الصفوف المكررة هو تضخيم النتائج التحليلية مثل إجمالي المبيعات أو عدد العملاء، مما يؤدي إلى استنتاجات خاطئة.\n")

print("3. الحل الأمثل للتعامل مع القيم الفارغة في عمود Age لتحليل المتوسط هو استبدالها بمتوسط الأعمار الأخرى للحفاظ على حجم العينة وعدم تحييز النتائج.\n")

print("4. من المهم تحويل Join_Date إلى نوع تاريخ لتسهيل التحليلات الزمنية، مثل تجميع العملاء حسب شهر الانضمام أو حساب مدة علاقتهم بالشركة.\n")

print("5. ملاحظات حول العملاء: يوجد عميل متكرر (Ahmed Ali)، والعميلة (Nada Hassan) هي صاحبة أعلى قيمة مشتريات. وجود بيانات مفقودة يدل على أهمية تنظيف البيانات قبل التحليل.\n")