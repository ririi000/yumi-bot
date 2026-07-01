from discord.ext import commands
from discord import app_commands
import aiosqlite

DATABASE = "yumi.db"

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="balance")
    async def balance(self, interaction):
        async with aiosqlite.connect(DATABASE) as db:
            cursor = await db.execute(
                "SELECT coins FROM users WHERE user_id=?",
                (interaction.user.id,)
            )
            data = await cursor.fetchone()

        coins = data[0] if data else 0
        await interaction.response.send_message(f"💰 You have {coins} coins")

async def setup(bot):
    await bot.add_cog(Economy(bot))
