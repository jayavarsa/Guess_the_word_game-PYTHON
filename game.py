import random
import time
records={}
my_words=(('questionnaire','noun','a list of question survey'),
          ('unconscious','adjective','not consicous or without awareness'),
          ('precocious','adjective','unsually nature,espically in mental development'),
          ('liaison','noun','a person who maintains a connection between a people or group'),
          ('surveillance','noun','continous observation of a person,place or activity in order to gather information'),
          ('malfeasance','noun','conduct by a public offical that violates the public trust or is aganist the law'),
          ('irascible','adjective','irratable,quick-tempered'),
          ('idiosyncrasy','noun','a tendency,habit or mannerism that is peacullar to an individual; a quick'),
          ('foudroyant','adjective','sudden and overwhelming or stunning'),
          ('eudemonic','adjective','pertaining to conducive to happiness'),
          ('ephemeral', 'adjective', 'lasting for a very short time'),
          ('vicarious', 'adjective', 'experienced in the imagination through the feelings or actions of another person'),
          ('ubiquitous', 'adjective', 'present, appearing, or found everywhere'),
          ('quixotic', 'adjective', 'exceedingly idealistic, unrealistic, and impractical'),
          ('facetious', 'adjective', 'treating serious issues with deliberately inappropriate humor'),
          ('obfuscate', 'verb', 'to deliberately make something unclear or difficult to understand'),
          ('ubiquity', 'noun', 'the state of being everywhere at once'),
          ('plethora', 'noun', 'an excess of something'),
          ('ubiquitarian', 'noun', 'one who believes that Christ is present everywhere'),
          ('peregrinate', 'verb', 'to travel or wander around from place to place'))
def shuffle(w):
  list_w=list(w)
  random.shuffle(list_w)
  re=' '.join(list_w)
  return re
def gameplay():
  name='GUESS A WORD GAME'
  print(name.center(120,'-'))
  player_name=input('enter your name ')
  print(' enter s to stop the in the mid way')
  player_count=0
  player_time=time.time()
  for i in my_words:
    print(f' Jumbled Letters: {shuffle(i[0]).upper()} \n Part of speech: {i[1].upper()} \n Meaning: {i[2].upper()} \n ')
    player_input=input(' guess the word').lower()
    if player_input=='s':
      break
    elif player_input==i[0]:
      print('correct answer')
      player_count+=1
    else:
      print(f'wrong answer \n the correct answer is {i[0]}')
  end_time=time.time()
  timetaken=end_time-player_time
  print(f'you took {timetaken//60} minutes and {timetaken%60:.2f} seconds to guess {player_count} words  ')
  print(f' THE COMPLETE SET OF WORDS')
  length=0
  for i in my_words:

   if len(i[0])>length:
     length=len(i[0])
  length=length+5
  print(f' COMPLETE WORD LIST \n {"-"*120} \n {"##|"} {"word|".rjust(length," ")} {"part of speech|".rjust(length," ")} {"meaning".ljust(length," ")} \n {"-"*120}')
  num=1
  for i in my_words:
   print(f' {num:02}| {i[0].rjust(length," ")}| {i[1].rjust(length," ")}| {i[2].ljust(length," ")} \n {"-"*120}')
   num+=1
  records['name']=player_name
  records['guess count']=player_count
  records['guess time']=timetaken\



gameplay()
