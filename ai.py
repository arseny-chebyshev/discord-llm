import aiohttp
from langchain_core.messages import HumanMessage, AIMessage
from discord import User, Member
from config import BACKEND_URL


class AIService:
    def __init__(self, user: User | Member) -> None:
        if isinstance(user, Member):
            user = user._user
        self.user = user

    async def generate_message(self, input: str | HumanMessage) -> AIMessage:
        if isinstance(input, str):
            input = HumanMessage(content=input)
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url=BACKEND_URL,
                json={'input': input.content}
            )
            answer = await response.json()
            return AIMessage(
                content=answer['output']['content']
            )
