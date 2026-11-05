import zipfile, re, os, glob, html

outs = []
for path in glob.glob(r"E:\демоэкзамен КИП\Прил_ОЗ_КИМ_15.01.31-1-2027\**\*.docx", recursive=True):
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8")
        text = re.sub(r"<w:p[ >]", "\n", xml)
        text = re.sub(r"<[^>]+>", "", text)
        text = html.unescape(text)
        out = os.path.join("pdf_text", "docx_" + os.path.basename(path) + ".txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        outs.append(f"OK {os.path.basename(path)} chars={len(text)}")
    except Exception as e:
        outs.append(f"FAIL {path}: {e}")
with open("pdf_text/_docx_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
