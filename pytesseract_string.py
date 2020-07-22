try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


#tesseract path
pytesseract.pytesseract.tessreact_cmd=r'C:\Program Files\Tesseract-OCR'


#simple image to string
#영어 사진은 lang 안써도 되지만, 한글 사진은 lang을 써야지 한글로 판독하여 나타냄
print(pytesseract.image_to_string(Image.open('poster_1.jpg'), lang='eng+kor'))

print('\n\n')
