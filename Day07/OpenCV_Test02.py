import cv2 

# 01. 일반 이미지
# img = cv2.imread('./Day07/test.png')

# 02. 그레이 이미지
# img = cv2.imread('./Day07/test.png', cv2.IMREAD_GRAYSCALE)

# 04. 원본을 그대로 두고 흑백을 추가
img = cv2.imread('./Day07/test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 03. 이미지 사이즈 축소
#  img_small = cv2.resize(img, (200,200))

# 05. 이미지 자르기
Height, Width, Channel = img.shape
print(Height, Width, Channel)

img_crop = img[:, :int(Width / 2)] # Height, Width
gray_crop = gray[:, :int(Width / 2)] # Height, Width

# 06. 이미지 블러 

img_blur = cv2.blur(img_crop, (5, 5)) # 숫자가 더 클수록 많이 블러 처리가 된다. (흐릿하게)

# cv2.imshow('Original', img)
# cv2.imshow('Gray', gray)

cv2.imshow('Blur half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()