def get_plan_maker_prompt(intent: str):
    plan_maker_prompt = f"""
user_intent: {str(intent)}
Based on the user's intent, create a single, coherent chain of tasks required to fulfill the user's objective. The plan must be a sequential chain where each step logically leads to the next, and must be presented in JSON format. For each step, assign exactly one type of external tool that will be used to achieve a broad objective in that part of the chain. Please follow these guidelines for each step:
- steps: Provide a concise summary of the type of steps (e.g., data extraction tool, visualization module, language processing engine).
- Description: Offer a general overview of the overall goal that this step is intended to accomplish. Do not detail specific operations or individual actions; simply describe the broad purpose and expected outcome.
- Reason: Why we need to do this step?

** Only if the user's intent specifically involves learning, acquiring information, or expanding their knowledge base, at the end of the task chain, include the following additional step:
- additional step: "Knowledge Documentation Generation and Upload"
- Description: "Utilize the tool that generates documentation and uploads to GitBook to compile all useful and meaningful knowledge produced during the plan's execution into a document and upload it to GitBook, ensuring long-term preservation and reuse of valuable information. This step should be executed only if the user's intent involves learning, acquiring knowledge, or gaining information, and the generated knowledge is assessed to be of high value; otherwise, omit this step. Exclude any trivial or mundane everyday details."
- Reason: "Why you decide to do this step? What do you want to learn from these step?"
Do not provide multiple alternatives or choices; only generate one sequential chain of tasks.

**Output Requirements:**
Provide the result create a list strictly in the following JSON format without any additional text:
<output example>
{[
    {   "step": "step 1",
        "intent": "intent for Step 1",
        "Description": "A general overview of the objective to be achieved by this tool in the first part of the task.",
        "Reason": "Why we need to do this step?"
    },
    {   "step": "step 2",
        "intent": "intent for Step 2",
        "Description": "A general overview of the objective to be achieved by this tool in the next part of the task.",
        "Reason": "Why we need to do this step?"
    },
    ...
]}
</output example>

Now, output your result in the JSON format:
"""

    return plan_maker_prompt
