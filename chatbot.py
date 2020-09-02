# chatbot.py
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import asyncio

class Cbot:
    def __init__(self, name):
        self.chatbot = ChatBot(name, storage_adapter='chatterbot.storage.SQLStorageAdapter')
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )

    async def train(self, ws):
        while True:
            await ws.send_text("Begin with something: ")
            data = await ws.receive_text()
            input = Statement(data)
            response = self.chatbot.generate_response(input)
            await ws.send_text('\n Is "{}" a coherent response to "{}"? yes or no \n'.format(
                response.text,
                input.text
            ))
            data = ws.receive_text()
            if await self.__get_feedback(ws) is False:
                await ws.send_text('please input the correct one')
                correct_response = await ws.receive_text()
                self.chatbot.learn_response(correct_response, input)
                await ws.send_text('Responses added to bot! \n Send another question if wanted: ')

    async def __get_feedback(self, ws):
        fb = await ws.receive_text()
        print(fb)
        if 'yes' in fb.lower():
            return True
        elif 'no' in fb.lower():
            return False
        else:
            await ws.send_text('Please type either "Yes" or "No"')
            return get_feedback()
