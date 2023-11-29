import cv2
import numpy as np
import base64
import tempfile
import shutil
import os
import logging

def process_and_encode_video(file_buffer):
    """
    Process a video file buffer to extract and base64-encode frames at regular intervals.

    Args:
        file_buffer (file-like object): Buffer of the uploaded video file.

    Returns:
        list: A list of base64-encoded strings representing selected frames.
    """
    file_buffer.seek(0)  # Reset file pointer to the start

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
        shutil.copyfileobj(file_buffer, tmp_file)
        tmp_file_path = tmp_file.name

    try:
        video = cv2.VideoCapture(tmp_file_path)
        if not video.isOpened():
            raise IOError(f"Cannot open video file: {tmp_file_path}")

        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total frames {total_frames}")
        frame_rate = video.get(cv2.CAP_PROP_FPS)
        duration = total_frames / frame_rate

        frame_interval = 0.5  # seconds
        frame_sample_rate = frame_rate * frame_interval

        base64_frames = []
        for frame_index in np.arange(0, total_frames, frame_sample_rate):
            video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            success, frame = video.read()
            if success:
                _, buffer = cv2.imencode('.jpg', frame)
                base64_frames.append(base64.b64encode(buffer).decode('utf-8'))
            else:
                print(f"Failed to read frame at index {frame_index}")

        return base64_frames

    finally:
        video.release()
        os.remove(tmp_file_path)
