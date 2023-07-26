from transformers import pipeline, Conversation

pipe = pipeline("conversational", model="PygmalionAI/pygmalion-6b")

persona = Conversation('''
hello, what is your name?   

''')


print(pipe(persona))