import cv2
import numpy as np
def vid():
  file_name = "video location here"
  window_name = "window"
  interframe_wait_ms = 30

  cap = cv2.VideoCapture('intro.mp4')
  if not cap.isOpened():
      print("Error: Could not open video.")
      exit()

  cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
  cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

  while (True):
      ret, frame = cap.read()
      if not ret:
          print("Reached end of video, exiting.")
          break

      cv2.imshow(window_name, frame)
      if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
          print("Exit requested.")
          break

  cap.release()
  cv2.destroyAllWindows()
