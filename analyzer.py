import pdfplumber

# کلیدواژه‌های مربوط به یک شغل فرضی (مثلاً برنامه‌نویس پایتون)
KEYWORDS = [
    "python", "django", "fastapi", "sql", "machine learning",
    "data analysis", "git", "docker", "api"
]

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def score_resume(text):
    score = 0
    for word in KEYWORDS:
        if word in text:
            score += 1
    return score

def find_best_resume(file_paths):
    best_score = -1
    best_file = None

    for path in file_paths:
        text = extract_text_from_pdf(path)
        score = score_resume(text)
        print(f"{path} => Score: {score}")
        if score > best_score:
            best_score = score
            best_file = os.path.basename(path)

    return best_file
