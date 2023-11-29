import base64
import logging
import cv2
import numpy as np

def decode_base64_to_image(base64_string):
    """
    Decode a base64 string to an image.
    """
    try:
        frame_data = base64.b64decode(base64_string)
        nparr = np.frombuffer(frame_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is not None:
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            logging.warning("Failed to decode base64 string to image.")
            return None
    except Exception as e:
        logging.error(f"Error decoding base64 string: {e}")
        return None
