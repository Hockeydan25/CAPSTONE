"""dan Smestad video instructions lab2"""
import requests  #had to install request I think! program was not installing and after installing errors.
#program restart pip install completed but want pip upgrade tring to review user install. Only a warning now

question = input('Enter your question for the magic 8 ball:  ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'
try:
    responce = requests.get(magic_8_ball_url).json()
    answer = responce['magic']['answer']
    print(f'The Magic 8 Ball says....:  {answer}')
except:
    print('Sorry, magic 8  ball is out right now, please try again later!')
    #program runs well with requests installed.
