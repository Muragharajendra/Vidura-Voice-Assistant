import google.generativeai as genai

# Setup Gemini API key
genai.configure(api_key="AIzaSyCUkveVkumefvziKzFx_TYdD1FlKOB0GDs")  # Replace with your Gemini API key

# Create model instance
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Ask a question
response = model.generate_content(
    [
        {"role": "system", "parts": ["You are a virtual assistant named Vidhura skilled in general tasks like Alexa and Google Cloud. Please give short, clear answers without any markdown or formatting."]},
        {"role": "user", "parts": ["what is coding"]}
    ],
    generation_config={
        "temperature": 0.3,
        "max_output_tokens": 100,
        "top_p": 1,
        "top_k": 10
    }
)

# Print the response
print(response.text)
