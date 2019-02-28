import sys

import cv2


def align_image(img):
    return alignment.align(96, img, alignment.getLargestFaceBoundingBox(img),
                           landmarkIndices=AlignDlib.OUTER_EYES_AND_NOSE)


sys.path.insert(0, "/Users/len/ai-env/lib/python3.6/site-packages/dlib-19.16.99-py3.6-macosx-10.13-x86_64.egg/")
from align import AlignDlib

# 내장 카메라 또는 외장 카메라에서 영상을 받아옴
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
alignment = AlignDlib('models/landmarks.dat')
while True:
    # ret은 카메라의 상태가 저장되며 정상 작동할 경우 True를 반환합니다. 작동하지 않을 경우 False를 반환합니다.
    # frame에 현재 프레임이 저장됩니다.(= image)
    ret, frame = capture.read()
    bounding_box = alignment.getLargestFaceBoundingBox(frame)
    if bounding_box is not None:
        cv2.rectangle(frame, (bounding_box.left(), bounding_box.top()),
                      (bounding_box.left() + bounding_box.width(), bounding_box.top() + bounding_box.height()),
                      (0, 255, 0),
                      3, 4, 0)


        # crop_img = frame[bounding_box.top():bounding_box.top() + bounding_box.height(),
        #            bounding_box.left():bounding_box.left() + bounding_box.width()]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'who', (bounding_box.left()+20, bounding_box.top()+20), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(1) > 0: break


capture.release()
cv2.destroyAllWindows()
