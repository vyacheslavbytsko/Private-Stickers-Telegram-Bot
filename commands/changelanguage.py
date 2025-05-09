from commands import chooselanguage
from misc import Message

async def command_changelanguage(message: Message) -> None:
    await chooselanguage.choose_language(message)
