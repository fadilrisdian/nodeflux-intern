import cv2
import numpy as np
import streamlit as st
from PIL import Image
import urllib.request



# @st.cache(allow_output_mutation=True)
def resize_image(image, scale_percent):
    width, height = image.size
    width = int(width * scale_percent / 100)
    height = int(height * scale_percent / 100)
    newsize = (width, height)
    resized = image.resize(newsize)
    return resized


def gray_image(image):
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img_grey


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (5, 5), amount)
    return blur_img


def dilated_image(image, size):
    dilated = cv2.dilate(image, np.ones(size))
    return dilated


def morphology_image(image, ksize):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closing


def cascade(image):
    # Detecting cars using car cascade
    car_cascade_src = 'cars.xml'
    car_cascade = cv2.CascadeClassifier(car_cascade_src)
    cars = car_cascade.detectMultiScale(image, 1.1, 1)
    return cars


def result(cascade, resized_image):
    cnt = 0
    for (x, y, w, h) in cascade:
        cv2.rectangle(resized_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cnt += 1
    return [resized_image, cnt]


def show_image(image):
    im = Image.fromarray(image)
    im.show()


def main_loop():
    st.title("Car Detection & Counting Apps")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")

    st.sidebar.title("Setting")
    scale_percent = st.sidebar.slider("Image Scaling", min_value=0.5, max_value=100.0, value=50.0)
    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5, value=1.7)
    kernel_size = st.sidebar.radio("Dilate Kernel Size", [(2,2),(3,3),(4,4),(5,5)])
    ksize = st.sidebar.radio("Morphology Kernel Size", [(2,2),(3,3),(4,4)])

    # image_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    # if not image_file:
    #     return None
    image_url = st.text_input('Enter Car Image URL to count.. ',
                         'https://images.unsplash.com/photo-1589828155685-83225f7d91f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=410&q=80 ')
    if not image_url:
        return None
    urllib.request.urlretrieve(image_url, "image.png")

    # new_im = Image.open("image.png")
    # st.image(new_im)
    # # image_file = requests.get(path).content
    # # st.write(image_file)
    # st.write(new_im)

    org_image = Image.open("image.png")
    org_image_rz = resize_image(org_image, scale_percent)
    resized_img_arr = np.array(org_image_rz)
    gray_img = gray_image(resized_img_arr)
    blur_img = blur_image(gray_img, blur_rate)
    dilated_img = dilated_image(blur_img, kernel_size)
    morphology_img = morphology_image(dilated_img, ksize)
    cascade_img = cascade(morphology_img)
    results = result(cascade_img, resized_img_arr)
    # show_image(results[0])
    # print(results[1], " cars found")
    # resized_img.show()

    st.text("Original Image vs Processed Image")
    st.image([org_image_rz, results[0]])
    st.write(str(results[1]) + " cars found ")


if __name__ == '__main__':
    main_loop()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
