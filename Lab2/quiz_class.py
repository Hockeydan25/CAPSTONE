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
    
    def __init__(self, questions, answers):#initilized object, name instant variable.
        self.questions = questions     #setting the object parameters
        self.answers = answers


    def publish(self, correct_answer ):        
        self.correct_answer 

    def __str__(self):      #data = a or b = truthy a falsy b is set. # does the same as above less code more consice
        
        return f'Question: {self.questions} Books Published: {}' 

def main ():

    for k,v in question_bank.items(): # reads the question bank key names and print for user to select one.
        print(k)
    get_quiz()
    ('Harry Potter books 1')  #aurthors book titles.


    
    
main()    
