import sys
import os
from pdfminer.high_level import extract_text

src_dir = r"E:\демоэкзамен КИП"
out_dir = r"C:\Users\Бардаковы\AppData\Local\Temp\opencode\pdf_text"
os.makedirs(out_dir, exist_ok=True)

pdfs = [
    r"E:\демоэкзамен КИП\Метод_рекомендации_СПО_15.01.31-1-2027.pdf",
    r"E:\демоэкзамен КИП\Метод_рекомендации_Выпуск_15.01.31-1-2027.pdf",
    r"E:\демоэкзамен КИП\КИМ 15.01.31-1-2027 Том 1.pdf",
    r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\БУ\Задание 2\Прил_2_ОЗ_КИМ_15.01.31-1-2027\Прил_2_ОЗ_КИМ_15.01.31-1-2027\Монтажная схема.pdf",
    r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\БУ\Задание 3\Прил_3_ОЗ_КИМ_15.01.31-1-2027\Прил_3_ОЗ_КИМ_15.01.31-1-2027\Принципиальная электрическая схема.pdf",
    r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\БУ\Задание 1\Прил_1_ОЗ_КИМ_15.01.31-1-2027\Прил_1_ОЗ_КИМ_15.01.31-1-2027\ШПН МС.pdf",
    r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\БУ\Задание 1\Прил_1_ОЗ_КИМ_15.01.31-1-2027\Прил_1_ОЗ_КИМ_15.01.31-1-2027\ШПН ПЭС.pdf",
    r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\БУ\Задание 1\Прил_1_ОЗ_КИМ_15.01.31-1-2027\Прил_1_ОЗ_КИМ_15.01.31-1-2027\ШПН ПЭС Эталон.pdf",
]

report = []
for pdf_path in pdfs:
    name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_path = os.path.join(out_dir, name + ".txt")
    try:
        text = extract_text(pdf_path)
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        report.append(f"OK: {os.path.basename(pdf_path)} chars={len(text)}")
    except Exception as e:
        report.append(f"FAIL: {os.path.basename(pdf_path)}: {e}")

with open(os.path.join(out_dir, "_report.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(report))
