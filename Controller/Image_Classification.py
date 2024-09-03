import time
import numpy as np
from PIL import Image
from tflite_runtime.interpreter import Interpreter
import cv2
from Helpers.Dare import Dare
from Helpers.Truth import Truth



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class Image_Classification():
    def __init__(self) -> None:
        pass

    def set_input_tensor(self, interpreter, image):
        tensor_index = interpreter.get_input_details()[0]['index']
        input_tensor = interpreter.tensor(tensor_index)()[0]
        input_tensor[:, :] = image


    def classify_image(self, interpreter, image, top_k=1):
        """Returns a sorted array of classification results."""
        self.set_input_tensor(interpreter, image)
        interpreter.invoke()
        output_details = interpreter.get_output_details()[0]
        output = np.squeeze(interpreter.get_tensor(output_details['index']))
        if output_details['dtype'] == np.uint8:
            scale, zero_point = output_details['quantization']
            output = scale * (output - zero_point)
        ordered = np.argpartition(-output, top_k)
        return [(i, output[i]) for i in ordered[:top_k]]

    def Choice(self):
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        interpreter = Interpreter('model.tflite')
        interpreter.allocate_tensors()
        _, height, width, _ = interpreter.get_input_details()[0]['shape']
        # look_to_object()
        Count = 0
        while True:
            ret, frame = cap.read()
            # cv2.imshow('PiCam', frame)
            if not ret:
                continue
            
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite("frame.jpg", image)
            img_path = "frame.jpg"
            image = Image.open(img_path).resize((width, height), Image.ANTIALIAS)
            results = self.classify_image(interpreter, image)
            label_id, prob = results[0]
            if Count == 0:
                if label_id == 0:
                    TruthQ = Truth()
                    Count = Count + 1
                    cap.release()
                    cv2.destroyAllWindows()
                    return "Truth" , TruthQ;
                elif label_id == 1:
                    DareQ = Dare()
                    Count = Count + 1
                    cap.release()
                    cv2.destroyAllWindows()
                    return "Dare" , DareQ;


            # look_to_object()
            time.sleep(2)



