import cv2
roi_selected = False
roi_start = (0, 0)
roi_end = (0, 0)
def select_roi(event, x, y, flags, param):
    global roi_selected, roi_start, roi_end
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_selected = False
        roi_start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        roi_selected = False
        roi_end = (x, y)
        cv2.rectangle(frame, roi_start, roi_end, (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        roi_selected = True
        roi_end = (x, y)
        cv2.rectangle(frame, roi_start, roi_end, (0, 255, 0), 2)
        roi = frame[roi_start[1]:roi_end[1], roi_start[0]:roi_end[0]]
        cv2.imshow('ROI', roi)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(frame, roi_start, roi_end, (0, 0, 0), -1)
        cv2.destroyWindow('ROI')
Frame = cv2.VideoCapture(0)
cv2.namedWindow('Select ROI')
cv2.setMouseCallback('Select ROI', select_roi)
while True:
    ret, frame = Frame.read()
    cv2.putText(frame, 'MBS3523 Assignment 1 – Q3 Name: YEUNG YAT', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (125, 0, 125), 2)
    if roi_selected == False:
        cv2.imshow('Select ROI', frame)
    if cv2.waitKey(1) & 0xFF == ord('o'):
        break
Frame.release()
cv2.destroyAllWindows()