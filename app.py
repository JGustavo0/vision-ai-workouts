from config import setup_logging
from services.openai_services import OpenAIService
import streamlit as st
import numpy as np
from utils.decoders import decode_base64_to_image
from utils.video_processor import process_and_encode_video
import logging
from dotenv import load_dotenv

setup_logging()
load_dotenv()

def display_results(text):
    # Use Markdown for better formatting
    st.markdown("### Video Feedback:")
    
    # Use an expander for long text
    #with st.expander("See detailed analysis"):
    st.markdown(text)  # Assuming 'text' is in Markdown format

    # For very long outputs
    if len(text) > 1000:  # adjust the length as needed
        st.text_area("Full Report", text, height=300)  # Scrollable text area


def main():
    st.title('AI Vision Workout Coach')

    uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])
    
    if uploaded_file is not None:
        with st.spinner('Processing the video...'):
            try:
                base64_frames = process_and_encode_video(uploaded_file)
                st.success(f"Processed {len(base64_frames)} frames")
                
                with st.expander("Show Frames Sent to chatGTP Vision"):
                    for base64_frame in base64_frames[:10]:  # Display first 10 frames
                        frame_rgb = decode_base64_to_image(base64_frame)
                        if frame_rgb is not None:
                            st.image(frame_rgb, use_column_width=True)
                        else:
                            st.error("Failed to display one or more frames.")

                result = OpenAIService.process_content(base64_frames)
                display_results(result)

            except Exception as e:
                logging.error(f"An error occurred: {e}")
                st.error("Failed to process the video.")

if __name__ == "__main__":
    main()

