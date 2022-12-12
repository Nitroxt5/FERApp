import cv2
import numpy as np
from PIL import Image
from keras import backend, models
from mtcnn import MTCNN
import logging


def evaluate_emotions(instance):
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    img = Image.open(instance.image.path).convert('RGB')
    pixels = np.array(img)  # NOQA
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    faces = list(filter(lambda face: face['confidence'] > 0.95, faces))  # NOQA
    log_faces = "\n".join(map(str, faces))
    logging.info(f'Found faces:\n{log_faces}')
    cut_faces = []
    for face in faces:
        x, y, width, height = face['box']
        f = pixels[y: y + height, x: x + width]
        f = np.array(Image.fromarray(f).convert('L').resize((48, 48)))  # NOQA
        cut_faces.append(f)

    cut_faces = np.array(cut_faces).reshape((len(cut_faces), 48, 48, 1))

    nn_model = models.load_model('nn_model')
    nn_model.compile()
    emotions = backend.argmax(nn_model.predict(cut_faces), axis=-1)
    emotions = [labels[e] for e in emotions]

    img = _update_image_with_emotions(instance.image.path, faces, emotions)
    cv2.imwrite(instance.image.path, img)  # NOQA


def _update_image_with_emotions(path_to_img: str, faces: list, emotions: list) -> np.ndarray:
    img = cv2.imread(path_to_img)  # NOQA
    red_BGR = (0, 0, 255)
    thickness = 2
    for face, emotion in zip(faces, emotions):
        x, y, width, height = face['box']
        img = cv2.rectangle(img, (x, y), (x + width, y + height), red_BGR, thickness)  # NOQA
        img = cv2.putText(img, emotion, (x + 1, y + height - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red_BGR, thickness)  # NOQA
    return img
