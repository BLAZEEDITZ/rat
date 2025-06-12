import pyttsx3
import time


def test_text_to_speech():
    """Test text-to-speech functionality"""
    print("Testing text-to-speech...")

    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Get available voices
        voices = engine.getProperty('voices')
        print(f"Found {len(voices)} voices")

        # Print voice information
        for i, voice in enumerate(voices):
            print(f"Voice {i + 1}:")
            print(f"  ID: {voice.id}")
            print(f"  Name: {voice.name}")
            print(f"  Languages: {voice.languages}")
            print(f"  Gender: {voice.gender}")
            print(f"  Age: {voice.age}")

        # Set properties
        engine.setProperty('rate', 180)  # Speed
        engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

        # Try to set a male English voice if available
        male_voice_found = False
        for voice in voices:
            if "english" in voice.name.lower() and "male" in voice.gender.lower():
                engine.setProperty('voice', voice.id)
                male_voice_found = True
                print(f"Selected voice: {voice.name}")
                break

        if not male_voice_found and voices:
            engine.setProperty('voice', voices[0].id)
            print(f"Selected default voice: {voices[0].name}")

        # Speak test message
        test_message = "Hello, I am Jarvis, your AI assistant. This is a test of the text-to-speech system."
        print(f"Speaking: '{test_message}'")

        engine.say(test_message)
        engine.runAndWait()

        print("✅ Text-to-speech test completed successfully")
        return True
    except Exception as e:
        print(f"❌ Error during text-to-speech test: {e}")
        return False


if __name__ == "__main__":
    test_text_to_speech()
