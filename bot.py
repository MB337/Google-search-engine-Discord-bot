import discord
from apiclient.discovery import build

# Custom search Google ID (https://programmablesearchengine.google.com/cse/all)
cx_stackoverflow = 'YOUR_STACKOVERFLOW_CUSTOM_SEARCH_ID'
cx_github = 'YOUR_GITHUB_CUSTOM_SEARCH_ID'
cx_youtube = 'YOUR_YOUTUBE_CUSTOM_SEARCH_ID'
cx_wikipedia = 'YOUR_WIKIPEDIA_CUSTOM_SEARCH_ID'
cx_reddit = 'YOUR_REDDIT_CUSTOM_SEARCH_ID'
cx_google = 'YOUR_GOOGLE_CUSTOM_SEARCH_ID'

# Your discord API token
token = 'YOUR_TOKEN'
client = discord.Client()

# Your google custom search API key
api_key = 'YOUR_API_KEY'

# Emoji for the reactions 
stackoverflow_emoji = '<:stackoverflow:801910018898526249>'
github_emoji = '<:github:801910018365849622>'
youtube_emoji = '<:youtube:801910018416574475>'
wikipedia_emoji = '<:wikipedia:802278334964170762>'
reddit_emoji = '<:reddit:801910018634940426>'
google_emoji = '<:google:802276663274635314>'

# Start the discord bot
lista = []
@client.event
async def on_message(message):
  global api_key, cx_stackoverflow, cx_github, cx_youtube, cx_reddit

  # If the message author = the discord bot --> ignore it
  if message.author == client.user:
    return
  
  # If the message starts with the command q?: 
  if message.content.startswith('q? '):

    # Add reactions on the message    
    await message.add_reaction(stackoverflow_emoji)
    await message.add_reaction(github_emoji)
    await message.add_reaction(google_emoji)
    await message.add_reaction(wikipedia_emoji)
    await message.add_reaction(youtube_emoji)
    await message.add_reaction(reddit_emoji)

    # Take what the user write (without q?)
    multiple_query = message.content.split("q? ")[1]

    # Listen if someone add reactions:
    @client.event
    async def on_raw_reaction_add(payload):
      reaction = str(payload.emoji)
      if payload.user_id == client.user.id:
        return
      
      # If someone add the stackoverflow reaction: 
      if reaction == stackoverflow_emoji:
        embed = discord.Embed(title="From StackOverflow:", color=0xc17e64)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/801910018898526249.png")
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_stackoverflow).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)

      # If someone add the github reaction:
      if reaction == github_emoji:
        embed = discord.Embed(title="From GitHub:", color=0x000000)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/801910018365849622.png')
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_github).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)
        
      # If someone add the google reaction:
      if reaction == google_emoji:
        embed = discord.Embed(title="From Google:", color=0x34a853)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/802276663274635314.png')
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_google).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)

      # If someone add the youtube reaction:
      if reaction == youtube_emoji:
        embed = discord.Embed(title="From YouTube:", color=0xb22d2e)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/801910018416574475.png')
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_youtube).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)
      
      # If someone add the wikipedia reaction:
      if reaction == wikipedia_emoji:
        embed = discord.Embed(title="From Wikipedia:", color=0xeeeeee)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/802278334964170762.png')
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_wikipedia).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)

      # If someone add the reddit reaction:
      if reaction == reddit_emoji:
        embed = discord.Embed(title="From Reddit:", color=0xdc7143)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/801910018634940426.png')
        embed.set_footer(text=f'Powered by Google API',icon_url="https://media.discordapp.net/attachments/799231729965072395/802555907207856138/logo.png")
        resource = build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=multiple_query, cx=cx_reddit).execute()
        for x in range(0, 3):
          try:
            lista.append(result['items'][x]['link'])
          except:
            pass
        if len(lista) == 3:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1]+"\n\n"+lista[2], inline=False)
        if len(lista) == 2:
          embed.add_field(name="\u200b", value=lista[0]+"\n\n"+lista[1], inline=False)
        if len(lista) == 1:
          embed.add_field(name="\u200b", value=lista[0], inline=False)
        if len(lista) == 0:
          embed.add_field(name="\u200b", value="I'm sorry, i didn't found anything about this", inline=False)
        await message.channel.send(embed=embed)


      lista.clear()

# Run the bot
client.run(token)
