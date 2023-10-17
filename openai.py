import openai

def _extract_token(response):
    if response['object'] == 'error':
        # Handle the error response
        error_message = response.get('error', {}).get('message', 'Unknown error')
        print(f'OpenAI API Error: {error_message}')
        return None  # You can choose to raise an exception or return an error message

    tokens = response.get('choices', [])[0].get('logprobs', {}).get('tokens', [])
    return tokens

# Example usage
openai.api_key = 'YOUR_API_KEY'
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: 'Hello, how are you?'",
    max_tokens=50,
    stream=True
)

for token in _extract_token(response):
    # Process the tokens as needed
    print(token)
