from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)
def GenerateResponse(input_text):
    response = model.generate_content([
    "input: Hi",
    "output: Hi, how i can help you?",
    "input: I am looking for a place in Vietnam, can you list any famous places?",
    "output: Here are some of the most famous places in Vietnam:\n: A network of 5 marble mountains with multiple caves, elaborate temples & viewing outlooks. It is located 12.7 km away from you.\n: A mountain resort with a cable car, amusement park, and French village. It is located 20.1 km away from you.\n: The remains of Hindu temples built between the 4th & 14th centuries, with red brick & ornate carvings. It is located 33.8 km away from you.\n: The tomb of a storied Vietnamese emperor, with elaborate architecture & ornate details. It is located 71.7 km away from you.\n: A sprawling national park in lush surrounds featuring a network of wet caves, rivers & waterfalls. It is located 267 km away from you.",
    "input: Can you help to find a hotel?"
    "output: "
    f"input: {input_text}",
    "output: ",
    ])
    return response.text

# while True:
#     string = str(input("Enter your prompt: "))
#     print("Bot: ", GenerateResponse(string))