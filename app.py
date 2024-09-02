import google.generativeai as ai
import os


ai.configure(api_key="add you API key here")

model = ai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("what was the first question i asked you?")
print(response.text) 
