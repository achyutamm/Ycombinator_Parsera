import openai

# Set your OpenAI API key here
openai.api_key = "sk-zSxkFmYdt0vCDmzyjGbGhEjYLp8fPZE1eK9IfJHN5PT3BlbkFJgVLK_6tYc_ewieINMpHaLTLWwv5UH11B8V6ZXJfRQA"


def test_openai_api():
    try:
        # Making a simple API request to check if it is working
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a model you have access to
            messages=[{"role": "user", "content": "Hello, how are you?"}]
        )
        # Print the response from the API
        print("API request successful. Response:")
        print(response['choices'][0]['message']['content'])
        return True
    except openai.error.OpenAIError as e:
        # Catching generic OpenAI errors
        print(f"An OpenAI error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if test_openai_api():
        print("API test passed.")
    else:
        print("API test failed.")
