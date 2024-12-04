# import openai

# openai.api_key = ""
# def get_openai_generator(prompt: str):
#     openai_stream = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.0,
#         stream=True,
#     )
#     for event in openai_stream:
#         if "content" in event["choices"][0].delta:
#             current_response = event["choices"][0].delta.content
#             yield "data: " + current_response + "\n\n"