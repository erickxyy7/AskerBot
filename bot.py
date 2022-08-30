'''
A bot for asker.fun (https://asker.fun) website. Use the `Bot` class to easily control the bot.
'''

from time import sleep
from random import choice
from selenium import webdriver
from ai import ai

class Bot():
  def __init__(self, sessionid):
    self.sessionid = sessionid
    self.webdriver = webdriver.Firefox()
  
  def login(self):
    self.webdriver.get('https://asker.fun')
    self.webdriver.add_cookie({"name": "sessionid", "value": self.sessionid})
  
  def get_bot_profile_url(self):
    self.webdriver.get('https://asker.fun')
    bot_profile_url = self.webdriver.find_element_by_id('pop-menu').find_elements_by_tag_name('a')[0].get_attribute('href')
    return bot_profile_url
  
  def get_last_question_id(self):
    '''
    Get the last question id.
    '''
    self.webdriver.get('https://asker.fun/news')
    while True:
      try:
        qid = self.webdriver.find_element_by_id('lista_de_questoes_recentes').find_elements_by_tag_name('li')[0].get_attribute('data-id')
        break
      except IndexError:
        continue
    return int(qid)
  
  def answer_question(self, qid):
    self.webdriver.get('https://asker.fun/question/%d' % (qid))
    try:
      self.webdriver.find_element_by_id('sua-resposta').click()
    except:
      return
    question = self.webdriver.find_elements_by_tag_name('h1')[0].text
    answer = ai(question)
    if not answer:
      return
    self.webdriver.find_element_by_id('sua-resposta').send_keys(answer)
    self.webdriver.find_element_by_id('botao_enviar_resposta').click()
  
  def continually_answer_questions(self):
    while True:
      qid = self.get_last_question_id()
      self.answer_question(qid)
      sleep(choice((5, 10, 15, 20, 25, 30)))

bot = Bot(SESSIONID)
bot.login()
bot.continually_answer_questions()
