fileopen = open("data\\Api.txt","r")
API = fileopen.read()
fileopen.close()
# print(API)

import openai
from dotenv  import load_dotenv


openai. api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    filelog = open("database\\chat_log.txt","r")
    # print ("hello")
    chat_log_template = filelog.read()
    filelog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\ndark : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)  
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \ndark : {answer}" 
    filelog = open("database\\chat_log.txt","w")
    filelog.write(chat_log_template_update)
    filelog.close()
    return answer



# while True:
#     kk = input("Enter : ")
#     print(ReplyBrain(kk))





# import openai

# openai.api_key = "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"

# def ReplyBrain(question):
#     model_engine = "text-davinci-002"
#     prompt = (f"{question}"
#              )

#     completions = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=60,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     message = completions.choices[0].text
#     return message

# while True:
#     question = input("You: ")
#     if question == "exit":
#         break
#     else:
#         answer = ReplyBrain(question)
#         print("AI: " + answer)




    
    

