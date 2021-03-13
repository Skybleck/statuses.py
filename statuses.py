MADE BY SKYBLECK

https://github.com/Skybleck
https://bit.ly/3eLQiQ3

#Changes the presence to .commands | and then how many servers it's in.
await client.change_presence(activity=discord.Game(name=".commands " f"| watching {len(client.guilds)} servers"))

#Watching a video. The link can be twitch or youtube video. And then name=is the name.
await client.change_presence(activity=discord.Streaming(name="Sky's youtube.", url="https://www.youtube.com/watch?v=qTAiDZMpLlE"))

#Listening to a song or something.
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song or what ever"))

#The bot's watching something.
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="A movie or video."))
