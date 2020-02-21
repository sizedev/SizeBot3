from sizebot.globalsb import *
import sizebot.digilogger as logger

launch = datetime.now()

os.system("")

# Get authtoken from file.
with open("../_authtoken.txt") as f:
    authtoken = f.readlines()
authtoken = [x.strip() for x in authtoken]
authtoken = authtoken[0]

# Predefined variables.
prefix = '&'
description = '''SizeBot3 is a complete rewrite of SizeBot for the Macropolis and, later, Size Matters server.
Written by DigiDuncan.
The SizeBot Team: DigiDuncan, Natalie, AWK_, Benyovski, Arceus3521, Surge The Raichu.'''
initial_extensions = [
    'cogs.change',
    'cogs.dm',
    'cogs.fun',
    'cogs.mod',
    'cogs.monika',
    'cogs.register',
    'cogs.roleplay',
    'cogs.set',
    'cogs.stats',
    'cogs.winks',
    'cogs.christmas'
]

# Obviously we need this printed in the terminal.
print(bg(24) + fg(202) + style.BOLD + ascii + style.RESET + " v" + version)

bot = commands.Bot(command_prefix=prefix, description=description)
bot.remove_command("help")
bot.add_check(check)


@bot.event
# Output header.
async def on_ready():
    print(fore.CYAN + 'Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------' + style.RESET)
    await bot.change_presence(activity=discord.Game(name="Ratchet and Clank: Size Matters"))
    logger.warn("Warn test.")
    logger.crit("Crit test.")
    logger.test("Test test.")
    finishlaunch = datetime.now()
    elapsed = finishlaunch - launch
    logger.test(f"SizeBot launched in {round((elapsed.total_seconds() * 1000), 3)} milliseconds.")
    print()


@bot.event
async def on_message(message):
    if message.content.startswith("&") and message.content.endswith("&"): return #Ignore Tupperboxes being mistaken for commands.
    if not message.content.startswith(allowbrackets): message.content = removebrackets(message.content)
    await bot.process_commands(message)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        # try:
        bot.load_extension(extension)


bot.run(authtoken)