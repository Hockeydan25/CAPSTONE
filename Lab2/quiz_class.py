"""Project1 Quiz Program Dan Smestad ITEC 2905-80 Software Dev. Capstone Clara James.
version one
 A quiz program. written for student editing """

#data structue Dicionary to hold data that can be interchanged. May have to rethink the my list names. 

question_bank = {   
"art": 
        {   
        "questions": 
        [
        "Who painted the Mona Lisa?",
        "What precious stone is used to make the artist\'s pigment ultramarine?",
        "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?"
        ],
        "correct_answers" : 
        [
        "Leonardo Da Vinci",
        "Lapiz lazuli",
        "Chicago"
        ]
        },
"space": 
        {   
        "questions" :
        [
        "Which planet is closest to the sun?", 
        "Which planet spins in the opposite direction to all the others in the solar system?",
        "How many moons does Mars have?"
        ],
        "correct_answers" : 
        [
        "Mercury",
        "Venus",
        "2"
        ]
        }
}

#from dataclasses import dataclass

class Question:
    
    def __init__(self, questions, answers, topics ):#initilized object, name instant variable.
        
        self.questions = questions    #setting the object parameters
        self.answers = answers
        self.topics = topics    

        self.bookstore = question_bank()


    def triva_questions(self,new_question  ):        
        self.questions.questions_for_topic['questions'] = new_question


    def __str__(self):      #data = a or b = truthy a falsy b is set. # does the same as above less code more consice
        
        return f'Question: {self.questions} Books Published: ' 

def main():

        print('Welcome to my Triva Quiz program!Topic options are: ')                         
        for k,v in question_bank.items(): # reads the question bank key names and print for user to select one.
            print(k)        
        selected_topic= get_input()# simple instructions to start.
        questions_for_topic = question_bank[selected_topic] # variable to hold list of questions from dictionary question_bank.
        quiz_answers = question_bank[selected_topic] # variable to hold list of correct answers from dictinary question_bank.
        score = get_quiz(questions_for_topic, quiz_answers)
        outputs(score, selected_topic) 

def get_input():  
    while True:
        selected_topic = input('Please choose a trvia selection topic? ')
        # simple instructions to start, user selects a triva topic.
        # vaildating that they select one of the choices. will keep in While loop until uset types topic in list.        
        if selected_topic not in question_bank.keys():                      
            print('that was not in our choices') 
        else:
            print(f'{selected_topic} is your choice')
            # simple instructions to help show users selection is being used.        
            return selected_topic  

def get_quiz(questions_for_topic, quiz_answers):# argumants needed to setup questions and answers.
    #variables set to use an loop through questions answers. localized function variables. 
    quiz_questions = questions_for_topic['questions']  # variables list of question strings.
    quiz_answers = questions_for_topic['correct_answers']  # variables list of correct answer.
    score = 0  #initalize score for tracking users total score. set to zero at start of quiz.
    for question, correct_answer in zip(quiz_questions, quiz_answers):        
        print(question) 
        #asking user question, to answer the question. 
        users_answer = input('enter your answer here: ') #variable and input function to prompt top user pregroam ready for there input.
        if users_answer.lower()  == correct_answer.lower(): #need to accept any case and validate correct answer.   
            score +=1  #point for correct answer.
            print(f'correct, current points earned = {score}.')#staement that qustion  was answered with correct answer.         
        else:      #message that answer is incorrect, points earned given too.
            print(f'Oops, sorry that was incorrect answer, current points earned = {score}.')
            # could have a retry here to give user another try or add a hint to user to get correct anwser.
    return score # returns score to main and outputs will use.

def outputs(score, selected_topic):      
    print('End of quiz!')# simple note that quiz has ended. total good byt message follows
    print(f'Your total score today in Quiz Triva is {score} out of 3.')
    if score == 3:
            print(f'You got all the Quiz Triva answers on {selected_topic} Triva correct! See you next time!')
    # extra statement to congratulate user on a well played game, 
    # possible to give extra points if all 3 correct
    return score,     

    
main()    
