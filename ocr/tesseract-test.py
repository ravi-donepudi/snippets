from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open(r"C:\Users\iluvm\Desktop\github\snippets\ocr\data\simple_table.png")))

