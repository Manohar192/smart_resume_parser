import fitz  # PyMuPDF
import docx
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "".join([page.get_text() for page in doc])
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def parse_resume(text):
    doc = nlp(text)
    result = {
        "Name": "",
        "Email": "",
        "Skills": []
    }
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            result["Name"] = ent.text
            break
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    result["Email"] = emails[0] if emails else "Not Found"
    skills = ["python", "java", "sql", "flask", "html", "css"]
    result["Skills"] = [skill for skill in skills if skill in text.lower()]
    return result
