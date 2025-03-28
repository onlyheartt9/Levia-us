from engine.llm_provider.llm import chat_completion
from metacognitive.stream.stream import output_stream
import os
CHAT_MODEL_NAME = os.getenv("CHAT_MODEL_NAME")

def backup_reply(chat_messages, user_id="local-dev", ch_id=""):
    try:
        prompt = [
            {"role": "user", "content": chat_messages}
        ]
        result = chat_completion(prompt, CHAT_MODEL_NAME, config={"temperature": 0}, user_id=user_id, ch_id=ch_id)
        return result
    except Exception as e:
        output_stream(log=f"Error: {e}", user_id=user_id, type="error", ch_id=ch_id)
        backup_reply = "Our system is currently experiencing high traffic. We kindly ask that you please try again later."
        return backup_reply
