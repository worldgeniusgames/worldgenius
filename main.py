import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("Y Frosty big P1nes")

bot.run("NzU1NzQ2MTc2NjA2NjY2Nzk1.GQefEK.IU9DmcvMFo8vUQaCrPervJP9wa0wNQLv2F7OhM")