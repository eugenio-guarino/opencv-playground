import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# grab the reference to the webcam
vs = cv2.VideoCapture(0)

f = open('counter.txt', 'rt+')
firstLine = f.readline()
img_counter = int(firstLine)


# keep looping
while True:
    # grab the current frame
    ret, frame = vs.read()

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if frame is None:
        break

    faces = faceCascade.detectMultiScale(frame, scaleFactor=1.05)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    # show the frame to our screen
    cv2.imshow('Video', frame)

    # if the 'ESC' key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    # SPACE pressed
    elif key == 32:
        img_name = 'facedetect_webcam_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('{} saved.'.format(img_name))
        img_counter += 1
        f.close()
        f = open('counter.txt', 'w')
        f.write(f'{img_counter}')
# close all windows
f.close()
vs.release()
cv2.destroyAllWindows()
