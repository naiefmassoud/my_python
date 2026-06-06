from google import genai

client = genai.Client(api_key="$GEMINI_API_KEY") # Replace with your actual API key. Steps in https://ai.google.dev/gemini-api/docs/quickstart#before_you_begin

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Who is the president of the Egypt?"
)
print(response.text)