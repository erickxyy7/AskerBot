import json
import random

with open('conversations.json', 'r') as file:
  conversations = json.loads(file.read().lower())

'''
Dice's coefficient implementation.
'''
def string_similarity(a, b):
    """dice coefficient 2nt/(na + nb)."""
    if not len(a) or not len(b): return 0.0
    if len(a) == 1:  a=a+u'.'
    if len(b) == 1:  b=b+u'.'
    
    a_bigram_list=[]
    for i in range(len(a)-1):
      a_bigram_list.append(a[i:i+2])
    b_bigram_list=[]
    for i in range(len(b)-1):
      b_bigram_list.append(b[i:i+2])
      
    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)
    dice_coeff = overlap * 2.0/(len(a_bigrams) + len(b_bigrams))
    return dice_coeff

# answers a question using artificial intelligence.
def ai(question):
  question = question.lower()
  
  possible_answers = []
  for conversation in conversations:
    if string_similarity(question, conversation[0]) > 0.6:
      possible_answers.append([string_similarity(question, conversation[0])] + conversation[1:])
  
  if not possible_answers:
    return None
  
  biggest = 0
  for answer in possible_answers:
    if answer[0] > biggest:
      biggest = answer[0]
      result = random.choice(answer[1:]) if answer[1:] else None
  
  return result
