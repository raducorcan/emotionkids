import cv2
import face_recognition
import numpy as np
from PIL import Image
from keras.models import load_model


class EmotionDetector:
    def __init__(self):
        self.model = load_model("./res/emotions_model.hdf5")
        emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
        self.labels = dict((k, v) for k, v in emotion_dict.items())

    def detectEmotion(self, filename):
        image = face_recognition.load_image_file(filename)
        face_locations = face_recognition.face_locations(image)
        if len(face_locations) == 0:
            return "No face detected"
        top, right, bottom, left = face_locations[0]
        face_image1 = image[top:bottom, left:right]
        image_save = Image.fromarray(face_image1)
        image_save.save(filename)

        face_image = cv2.imread(filename)
        face_image = cv2.resize(face_image, (48, 48))
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

        face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])

        predicted_class = np.argmax(self.model.predict(face_image))
        predicted_label = self.labels[predicted_class]
        return predicted_label
