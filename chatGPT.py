

# format
# company
# 
import openai
from docureader import *
import os
    
filename = 'Islam_Emadul_Resume_FINAL.docx'
resume = checkerfunc(filename)
openai.api_key = os.environ.get('OPENAI_API_KEY')
fileDatas = ''
coverLetter = ''
company = 'EY'

def auto_format(message2):
    model = "gpt-3.5-turbo"
    messages = [{"role": "system", "content": "Format this resume"},
            {"role": "user", "content": message2}]
    temperature = 0.3
    response = openai.ChatCompletion.create(model=model, messages = messages, temperature = temperature)
    return response['choices'][0]['message']['content']

def generate_response(resume):
    model = "gpt-3.5-turbo"
    if len(company) == 0:
        messages = [{"role": "system", "content": "You are acting as a hiring manager for a company. Evaluate this resume and provide a score on it on a scale of 100 and state what could be improved. Be brutally honest and detailed"},
                     {"role": "user", "content": auto_format(resume)}]
    elif len(coverLetter) == 0:
        messages = [{"role": "system", "content": "You are acting as a hiring manager for {company}. Evaluate this resume and provide a score on it on a scale of 100 and state what could be improved. Be brutally honest and detailed"},
                     {"role": "user", "content": auto_format(resume)}]
    else:
        messages = [{"role": "system", "content": "You are acting as a hiring manager for {company}. Evaluate this resume and cover letter. Provide a score on it on a scale of 100 and state what could be improved. Be brutally honest and detailed, taking account of the company applied for."},
                     {"role": "user", "content": auto_format(resume)}]
    temperature = 0.3
    response = openai.ChatCompletion.create(model=model, messages = messages, temperature = temperature)
    return response['choices'][0]['message']['content']      


## Make cover letter and company implementation

# Generate a response to the user input
response = generate_response(resume)

# Print the response
print(response)
