import azure.cognitiveservices.speech as speechsdk
from openai import OpenAI

# ----- User Input -----

speech_key = input("Speech Key: ").strip()
speech_region = input("Speech Region: ").strip()

project_endpoint = input("Project Endpoint: ").strip().rstrip("/")
api_key = input("API Key: ").strip()
deployment = input("Model Deployment Name: ").strip()

# ----- Speech Config -----

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    region=speech_region
)

speech_config.speech_recognition_language = "en-US"

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config
)

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

# ----- Foundry Client -----

client = OpenAI(
    api_key=api_key,
    base_url=f"{project_endpoint}/openai/v1/"
)

print("\nVoice Chat Ready")
print("Say 'goodbye' to quit.\n")

# ----- Conversation Loop -----

while True:

    print("Listening...")

    result = recognizer.recognize_once()

    if result.reason != speechsdk.ResultReason.RecognizedSpeech:
        print("Could not understand audio.\n")
        continue

    user_text = result.text.strip()

    print(f"\nYou: {user_text}")

    if "goodbye" in user_text.lower():
        print("Ending session.")
        break

    try:

        response = client.responses.create(
            model=deployment,
            input=user_text
        )

        ai_text = response.output_text

        print(f"\nAI: {ai_text}\n")

        synthesizer.speak_text_async(ai_text).get()

    except Exception as ex:
        print(f"\nError: {ex}\n")