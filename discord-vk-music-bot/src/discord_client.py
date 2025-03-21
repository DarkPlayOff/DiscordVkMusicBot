class DiscordClient(discord.Client):
    def __init__(self, command_prefix, intents):
        super().__init__(intents=intents)
        self.command_prefix = command_prefix

    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(self.command_prefix):
            command = message.content[len(self.command_prefix):].strip()
            await self.handle_command(command, message)

    async def handle_command(self, command, message):
        # Здесь будет логика обработки команд
        pass