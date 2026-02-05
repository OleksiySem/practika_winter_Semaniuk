def process_text(text):
    if not text:
        return "Введіть текст!"
    result = text[::-1].upper()
    return result