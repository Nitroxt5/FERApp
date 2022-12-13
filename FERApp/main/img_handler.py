import cv2
import numpy as np
from PIL import Image
from keras import backend, models
from mtcnn import MTCNN
import logging


def evaluate_emotions(instance):
    img = Image.open(instance.image.path).convert('RGB')
    pixels = np.array(img)  # NOQA

    faces = _detect_faces(pixels)
    if len(faces) == 0:
        return
    cut_faces = _cut_faces(pixels, faces)
    emotions = _recognize_emotions(cut_faces)
    img = _update_image_with_emotions(instance.image.path, faces, emotions)

    cv2.imwrite(instance.image.path, img)  # NOQA
    return len(faces)


def _detect_faces(pixels: np.ndarray):
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    faces = list(filter(lambda face: face['confidence'] > 0.95, faces))  # NOQA
    log_faces = "\n".join(map(str, faces))
    logging.info(f'Found faces:\n{log_faces}')
    return faces


def _cut_faces(pixels: np.ndarray, faces: list):
    cut_faces = []
    for face in faces:
        x, y, width, height = face['box']
        f = pixels[y: y + height, x: x + width]
        f = np.array(Image.fromarray(f).convert('L').resize((48, 48)))  # NOQA
        cut_faces.append(f)
    return np.array(cut_faces).reshape((len(cut_faces), 48, 48, 1))


def _recognize_emotions(cut_faces: np.ndarray):
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    nn_model = models.load_model('nn_model')
    nn_model.compile()
    emotions = backend.argmax(nn_model.predict(cut_faces), axis=-1)
    return [labels[e] for e in emotions]


def _update_image_with_emotions(path_to_img: str, faces: list, emotions: list) -> np.ndarray:
    img = cv2.imread(path_to_img)  # NOQA
    red_BGR = (0, 0, 255)
    blue_BGR = (255, 0, 0)
    for face, emotion in zip(faces, emotions):
        x, y, width, height = face['box']
        img = cv2.rectangle(img, (x, y), (x + width, y + height), red_BGR, 2)  # NOQA
        img = cv2.putText(img, emotion, (x + 1, y + height - 1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, blue_BGR, 1)  # NOQA
    return img
