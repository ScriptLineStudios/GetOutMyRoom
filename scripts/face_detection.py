import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
from scripts.notifications import send
import glob
import os
from scripts.config import WEBCAM, VIDEO_FILE

def main():
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(VIDEO_FILE, fourcc, 20.0, (640, 480))

  has_wrote_vid = False
  cap = cv2.VideoCapture(WEBCAM)
  with mp_pose.Pose(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        continue

      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = pose.process(image)

      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.pose_landmarks != None:
          out.write(image)
          has_wrote_vid = False
      else:
          if not has_wrote_vid:
              out.release()
              send(VIDEO_FILE)
              has_wrote_vid = True
              fourcc = cv2.VideoWriter_fourcc(*'XVID')
              out = cv2.VideoWriter(VIDEO_FILE, fourcc, 20.0, (640, 480))
          

      mp_drawing.draw_landmarks(
          image, 
          results.pose_landmarks,
          mp_pose.POSE_CONNECTIONS,
          landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

      if cv2.waitKey(5) & 0xFF == 27:
        break
  cap.release()