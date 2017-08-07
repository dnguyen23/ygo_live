import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2

camera_port = 0
ramp_frames = 10

camera = cv2.VideoCapture(camera_port)
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(0, ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
path = 'bub.png'
im = Image.open(path)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
text = pytesseract.image_to_string(Image.open(path), lang='eng')
print(text)
