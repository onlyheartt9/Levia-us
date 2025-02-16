import os
from engine.flow.system_prompt.system_prompt import (
    get_system_prompt,
    get_system_prompt_for_anthropic_reasoning,
    get_system_prompt_for_deepseek_reasoning,
    get_system_prompt_for_openai_reasoning,
)
from engine.llm_provider.llm import get_model_by_name
from engine.flow.chat_handler_flow.chat_handler_flow import handle_chat_flow
from memory.short_term_memory.short_term_memory import ShortTermMemory
import os

from metacognitive.stream.stream import output_stream

QUALITY_MODEL_NAME = os.getenv("QUALITY_MODEL_NAME")
CHAT_MODEL_NAME = os.getenv("CHAT_MODEL_NAME")

short_term_memory = ShortTermMemory()


def init_stream():
    """Initialize stream"""
    return output_stream("Initialized metacognitive stream.\n")

def init_short_term_memory():
    """Initialize short term memory"""
    model = get_model_by_name(CHAT_MODEL_NAME)
    if not model:
        raise ValueError(f"Model {CHAT_MODEL_NAME} not found")

    system_prompt = ""
    if model["type"] == "reasoning":
        if model["source"] == "openai":
            system_prompt = get_system_prompt_for_openai_reasoning()
        elif model["source"] == "anthropic":
            system_prompt = get_system_prompt_for_anthropic_reasoning()
        elif model["source"] == "deepseek":
            system_prompt = get_system_prompt_for_deepseek_reasoning()
    else:
        system_prompt = get_system_prompt()

    short_term_memory.add_context(system_prompt)

def terminal_chat():
    """Start interactive chat"""
    init_short_term_memory()
    init_stream()
    print("\033[93mWelcome to Levia Chat!\033[0m", flush=True)
    print("Enter 'quit' to exit, 'clear' to reset current conversation")

    while True:
        try:
            user_input = input("\033[94mYou: \033[0m").strip()
            if user_input.lower() == "quit":
                print("\033[93mGoodbye!\033[0m")
                break

            if not user_input:
                continue

            reply = handle_chat_flow(user_input, "local-dev")
            print("\033[92mLevia:\033[0m: ", reply)
            print("\n")
        except KeyboardInterrupt:
            print("\n\033[93mProgram terminated\033[0m")
            break
        except Exception as e:
            print(f"\033[91mError occurred: {str(e)}\033[0m")

