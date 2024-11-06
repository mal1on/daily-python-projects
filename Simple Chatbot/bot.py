import datetime


def bot():
    '''
    Basic chatbot that can respond to a limited set of questions or keywords.
    This chatbot can analyze user input and give predefined responses based
    on keywords it detects.
    '''
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What’s on your mind?",
        "weather": "I'm not sure about the weather, but it’s always a \
good day to code!",
        "time": f"The current time is \
{datetime.datetime.now().strftime('%H:%M')}.",
        "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
        "python": "Python is a versatile programming language, great \
for web development, data science, and more.",
        "bye": "Bye! Have a great day!",
    }
    print('Chatbot: Hello! I\'m here to chat. Type "bye" to exit.')
    while True:
        answer = input('You: ').lower()
        if answer == 'bye':
            print(responses['bye'])
            break
        for key in responses.keys():
            if key in answer:
                print(f'Chatbot: {responses[key]}')


if __name__ == '__main__':
    bot()
