import discord
from discord.ext import commands
import random
player1 = ""
player2 = ""
turn = ""
gameover = True
board = []
count = 0
client = commands.Bot(command_prefix='#')
win = [[0,1,2],
       [3,4,5],
       [6,7,8],
       [0,3,6],
       [1,4,7],
       [2,5,8],
       [0,4,8],
       [2,4,6]]
@client.event
async def on_ready():
  print("Ready")
@client.command()
async def tictactoe(ctx,p1:discord.Member,p2:discord.Member):
  global player1
  global player2
  global turn
  global gameover
  global count

  if gameover:
    global board
    board = [":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:",":white_large_square:"]
    turn = ''
    gameover = False
    count = 0
    player1 = p1
    player2 = p2
    line = ""
    for i in range(len(board)):
      if i == 2 or i == 5 or i == 8:
        line += " " + board[i]
        await ctx.send(line)
        line = ""
      else:
        line += " " + board[i]
    
    num = random.randint(1,2)
    if num == 1:
      await ctx.send("It's <@" + str(player1.id) + "> turn")
      turn = player1
    else:
      await ctx.send("It's <@" + str(player2.id) + "> turn")
      turn = player2

@client.command()
async def p(ctx,pos:int):
  mark = ''
  global player1
  global player2
  global turn
  global board
  global gameover
  global count
  global win

  if not gameover:
    if turn == ctx.author:
      if turn == player1:
        mark  = ":regional_indicator_x:"
      elif turn == player2:
        mark = ":o2:"
      if 0 < pos < 10 and board[pos - 1] == ":white_large_square":
        board[pos - 1] = mark
        count += 1
        line = ""
        for i in range(len(board)):
          if i == 2 or i == 5 or i == 8:
            line += " " + board[i]
            await ctx.send(line)
            line = ""
          else:
            line += " " + board[i]
        check(mark,win)
        if gameover:
          await ctx.send(mark + "Wins!")
        elif count >= 9:
          await ctx.send("It's a tie")
          gameover = True
        if turn == player1:
          turn = player2
        elif turn == player2:
          turn = player1
      
      else:
        await ctx.send("please choose a number between 1 and 9")
    else:
      await ctx.send("Its not you turn")
  else:
    await ctx.send("Please start a new game")

def check(mark,win):
  global gameover
  for i in win:
    if board[i[0]] == mark and board[i[1]] == mark and board[i[2]] == mark:
      gameover = True



client.run("OTMyMTQxMzkyNDk3NjE5MDE0.YeOqUg.WRaxtEOxwfZDRa1-_08KKYIHpGI")

