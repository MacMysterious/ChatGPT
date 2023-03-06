#OPENAI CHATGPT CLONE

# import onpenai library

import openai
# setup the openai API client
openai.api_key="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"
# this loop will let us ask questions continuously
# and behave like CHATGPT
while True:
    # SETUP THE MODEL AND PROMPT
    model_engine="text-davinci-003"
    prompt=input("enter new prompt: ")
    if "exit" in prompt or"quit" in prompt:
        break
    #     Generate a Response

    completion=openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,stop=None,
        temperature=0.5)

    # extracting useful part of response

    response=completion.choices[0].text
    # printing Response

    print(response)