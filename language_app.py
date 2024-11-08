import speech_recognition as sr

# Function to capture audio and convert it to text
def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something in English!")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None

# Simple response generation function based on input text
def generate_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you with English?"
    elif "help" in user_input.lower():
        return "I'm here to help you practice your responses!"
    else:
        return "That's interesting! Let's keep the conversation going."

# Main function to run the app
def main():
    user_text = get_audio_input()
    if user_text:
        response = generate_response(user_text)
        print(f"AI Response: {response}")

if __name__ == "__main__":
    main()
