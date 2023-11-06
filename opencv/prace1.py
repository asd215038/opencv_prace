import cv2

# 圖片
# img = cv2.imread('colorcolor.jpg')
# img = cv2.resize(img, (300, 300))
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img = cv2.resize(img, (0, 0), fx=2, fy=2)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# 影片
cap = cv2.VideoCapture('thumb.mp4')#讀取影片

# cap = cv2.VideoCapture(0)  VideoCapture也可以讀取視訊鏡頭預設鏡頭為0外接為1


while True:
    ret, frame = cap.read() #read()函式會回傳兩個值
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break 