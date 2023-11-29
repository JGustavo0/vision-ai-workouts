import openai
import os
import base64
import cv2

class OpenAIService:
    @staticmethod
    def process_content(base64_frames):
        """
        Process the given frames using OpenAI's API with LangChain for prompt construction.

        Args:
        frames: List of video frames to be processed.

        Returns:
        The result from the OpenAI API.
        """
        openai.api_key = os.getenv('OPENAI_API_KEY')
          
        PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                """I dont want identifying or making assumptions about people.
                Analyze these frames from a workout video. 
                Ignore the surronding and clothes.
                Focus on the workout type
                evaluate the execution quality in these workout""",
                *map(lambda x: {"image": x, "resize": 768}, base64_frames[0:50]),
            ],
        },]
        params = {
                "model": "gpt-4-vision-preview",
                "messages": PROMPT_MESSAGES,
                "max_tokens": 100,
            }

        result = openai.chat.completions.create(**params)

        return result.choices[0].message.content
