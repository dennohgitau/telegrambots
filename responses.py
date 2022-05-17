from datetime import datetime


def sampleResponses(inputText):
    userMessage = str(inputText).lower()

    if userMessage in ("hello", "hey"):
        return "Hey man"

    if userMessage in ("time", "What is the time?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(dateTime)

    return "I don't understand"


