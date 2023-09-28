# -*- coding: utf-8 -*-
"""CSE 111: Lab06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lu_z4gfGSymdZvugg64b4bAcQ4WPY4i_

CLASSWORK
"""

class NikeBangladesh:
  Nike_Status = 'Nike Bangladesh Status:'
  Branch_num = []
  sold = 0
  di = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
  def __init__(self,loc):
    self.loc = loc
    NikeBangladesh.Branch_num.append(self.loc)
  def details(self):
    print(f'Nike {self.loc} outlet')
    print(f'Products Currently Stocked: \n{NikeBangladesh.di}')
    print(NikeBangladesh.sold)
  def restockProducts(self,d):
    for i,j in d.items():
      for x,y in NikeBangladesh.di.items():
        if i == x:
          NikeBangladesh.di[x] += j
  def productSold(self,d):
    for i,j in d.items():
      for x,y in NikeBangladesh.di.items():
        if i == x:
          diff = y - j
          NikeBangladesh.di[x] = diff
          NikeBangladesh.sold += j


  @staticmethod
  def status():
    print(NikeBangladesh.Nike_Status)
    print(f'Branches Opened:{NikeBangladesh.Branch_num}')
    print(f'Cureenty Stocked \n{NikeBangladesh.di}')
    print(f'sold: {NikeBangladesh.sold}')
print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()

# Task 2
class Question:
    def __init__(self, text, choices, correct_choice):
      self.text = str(text)
      self.choices = list(choices) #choices
      self.correct_choice = int(correct_choice)
        # Initialize three instance variables
        # text(type str), choices(type list), correct_choice(type int)

      pass

class Quiz:
    count_quiz_objects = 0
    # Initialize a static variable for counting the number of Quizzes
    # or, to count the number of Quiz class objects
    total_quizzes = 0

    def __init__(self, quiz_name):
      self.name = str(quiz_name)
      self.questions = []
      self.score = 0
      # Initialize instance variable name (type str)
      # Initialize instance variable question (type list)
      # Initialize instance variable score (type int)
      pass

    def add_question(self, *questions):
      for i in questions:
        self.questions.append(i)
      # Append the question objects in the question list
      pass

    @classmethod
    def create_from_data(cls, quiz_name, question_data_list):
      obj = cls(quiz_name)
      a = question_data_list
      for i in a:
        obj1 = i['text']
        obj2 = i['choices']
        obj3 = i['correct_choice']
        obj4 = Question(obj1,obj2,obj3)
        obj.add_question(obj4)
      return obj


      # Firstly, make a Quiz class object by passing the quiz_name parameter in the constructor
      # From the question_data_list extract the Question data
      # After that, make the Question class objects passing the extracted data in the constructor
      # Append those in the question list of the Quiz class object
      # Finally, return the Quiz class object
      pass

    def attempt(self):
      '''
      Sample printing format for attempt method.
      let's say we are calling quiz1.attempt() from the driver code.
      output:

      --- Math Quiz ---
      What is the result of 2 + 2?
      1. 3
      2. 4
      3. 5
      Your answer (enter the choice number): 2
      Correct answer! 1 point for you.
      What is the result of 3 * 6?
      1. 15
      2. 18
      3. 20
      Your answer (enter the choice number): 1
      Wrong answer!
      Your total score: 1/2
      '''
      print(f"--- {self.name} ---")

      for question in self.questions:
        print(f"{question.text}") # will print the question as shown in the output.
        for index in range(len(question.choices)):# this loop will print the choices as shown in the output.
            print(f"{index+1}. {question.choices[index]}")

        user_choice = int(input("Your answer (enter the choice number): ")) # takes the choice number from the user

        if user_choice == question.correct_choice: # calculate the quiz score
            self.score += 1
            print("Correct answer! 1 point for you.")
        else:
          print("Wrong answer!")
      print(f"Your total score: {self.score}/{len(self.questions)}") # total score gained in a quiz

# Test the Quiz Maker

# We are creating a Quiz object for the Math Quiz
quiz1 = Quiz("Math Quiz")
# Now creating two quiz question objects
# The Question class constructor takes three parameters: (Question, choices, correct answer)
# The correct answer is given as (list_index + 1)
quiz1_question1 = Question("What is the result of 2 + 2?", ["3", "4", "5"], 2)
quiz1_question2 = Question("What is the result of 3 * 6?", ["15", "18", "20"], 2)
# Adding the question objects to a question list of the Quiz class
quiz1.add_question(quiz1_question1, quiz1_question2)
# We will use this list of dictionaries to prepare the python quiz questions
python_quiz_data = [
    {
        'text': "What is the keyword to define a function in Python?",
        'choices': ["func", "def", "function"],
        'correct_choice': 2
    },
    {
        'text': "Which one is NOT a built-in data type in Python?",
        'choices': ["int", "str", "double"],
        'correct_choice': 3
    }
]
# Create another Quiz class object for the python quiz
quiz2 = Quiz.create_from_data("Python Quiz", python_quiz_data)
# Accessing static variable using the class name
print("Total no. of quizzes: ", Quiz.total_quizzes)
# Attempt Math Quiz
quiz1.attempt()
# Attempt Python Quiz
quiz2.attempt()

"""SECOND_SAME"""

class Question:
    def __init__(self, text, choices, correct_choice):
      self.text = str(text)
      self.choices = list(choices)
      self.correct_choice = int(correct_choice)

      pass

class Quiz:
    count_quiz_objects = 0

    total_quizzes = 0

    def __init__(self, quiz_name):
      self.name = str(quiz_name)
      self.questions = []
      self.score = 0

      pass

    def add_question(self, *questions):
      for i in questions:
        self.questions.append(i)
      pass

    @classmethod
    def create_from_data(cls, quiz_name, question_data_list):
      obj = cls(quiz_name)
      a = question_data_list
      for i in a:
        obj1 = i['text']
        obj2 = i['choices']
        obj3 = i['correct_choice']
        obj4 = Question(obj1,obj2,obj3)
        obj.add_question(obj4)
      return obj


    def attempt(self):
      '''
      Sample printing format for attempt method.
      let's say we are calling quiz1.attempt() from the driver code.
      output:

      --- Math Quiz ---
      What is the result of 2 + 2?
      1. 3
      2. 4
      3. 5
      Your answer (enter the choice number): 2
      Correct answer! 1 point for you.
      What is the result of 3 * 6?
      1. 15
      2. 18
      3. 20
      Your answer (enter the choice number): 1
      Wrong answer!
      Your total score: 1/2
      '''
      print(f"--- {self.name} ---")

      for question in self.questions:
        print(f"{question.text}") # will print the question as shown in the output.
        for index in range(len(question.choices)):# this loop will print the choices as shown in the output.
            print(f"{index+1}. {question.choices[index]}")

        user_choice = int(input("Your answer (enter the choice number): ")) # takes the choice number from the user

        if user_choice == question.correct_choice: # calculate the quiz score
            self.score += 1
            print(f"Correct answer! {self.score} point for you.")
        else:
          print("Wrong answer!")
      print(f"Your total score: {self.score}/{len(self.questions)}") # total score gained in a quiz

# Test the Quiz Maker

# We are creating a Quiz object for the Math Quiz
quiz1 = Quiz("Math Quiz")

quiz1_question1 = Question("What is the result of 2 + 2?", ["3", "4", "5"], 2)
quiz1_question2 = Question("What is the result of 3 * 6?", ["15", "18", "20"], 2)

quiz1.add_question(quiz1_question1, quiz1_question2)

python_quiz_data = [
    {
        'text': "What is the keyword to define a function in Python?",
        'choices': ["func", "def", "function"],
        'correct_choice': 2
    },
    {
        'text': "Which one is NOT a built-in data type in Python?",
        'choices': ["int", "str", "double"],
        'correct_choice': 3
    }
]
# Create another Quiz class object for the python quiz
quiz2 = Quiz.create_from_data("Python Quiz", python_quiz_data)
# Accessing static variable using the class name
print("Total no. of quizzes: ", Quiz.total_quizzes)
# Attempt Math Quiz
quiz1.attempt()
# Attempt Python Quiz
quiz2.attempt()

class Foodiz:
  total_sell = 0
  branch_info = []
  def __init__(self,branch_name):
    self.branch_name = branch_name
    branch_sell = 0
    Foodiz.branch_info.append(self)
  def sellQuantity(self,quantity):
    self.branch_sell = quantity*300
    Foodiz.total_sell += quantity*300
  def branchInformation(self):
    print(f'Branch Name: {self.branch_name}')
    print(f'Branch Sell:{self.branch_sell}')
  @classmethod
  def details(cls):
    print(f'total Number of branch(s): {len(Foodiz.branch_info)}')
    print(f"total sell: {Foodiz.total_sell} Taka")
    for i in Foodiz.branch_info:
      print('########################')
      print(f'Branch name: {i.branch_name}')
      print(f'Branch Sell: {i.branch_sell}')
      print(f"Branch consists of total sell's: {(i.branch_sell/Foodiz.total_sell)*100}%")


Foodiz.details()
print('1----------------------------------')
mohakhali = Foodiz('Mohakhali')
mohakhali.sellQuantity(25)
mohakhali.branchInformation()
print('2----------------------------------')
Foodiz.details()
print('3========================')
banani = Foodiz('Banani')
banani.sellQuantity(15)
banani.branchInformation()
print('4----------------------------------')
Foodiz.details()
print('5========================')
gulshan = Foodiz('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('6----------------------------------')
Foodiz.details()

def function(a):
  l = []
  var = ""
  for i in range(len(a)):
    if len(a)-1 != i:
      if a[i] == 'i' and a[i+1] == " ":
        d = a[i].upper()
        var += d
      else:
        if a[i] == '.' or a[i] == '?' or a[i] == '!':
          var+=a[i]
          l.append(var)
          var = ''
        else:
          var+=a[i]
  l.append(var)
  word = ''
  for i in l:
    if len(word)==0:
      b = i[0].upper()+i[1:]
      word+=b
    else:
      c = i[0]+i[1].upper()+i[2:]
      word += c

  print(word)
  print(l)
function("my fav animal is a dog. a dog has sharp teeth so that i can eat flesh very easily! do u know my dog's name? i love my dog.")

