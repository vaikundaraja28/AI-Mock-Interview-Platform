import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=30
        )

    try:

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:

        return "ERROR: Could not understand audio."

    except sr.RequestError:

        return "ERROR: Speech service unavailable."

    except Exception as e:

        return f"ERROR: {e}"