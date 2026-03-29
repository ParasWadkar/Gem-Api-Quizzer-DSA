import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Giving the API key to the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Basic introducction and asking the user for the difficulty level and topic they want to practice.
print("Hello, welcome to the DSA quizzer! Let's get you a problem to solve.")
print("Tell me the difficulty level of the questions you want to try")
user_input = input("Enter number or name:\n1. Easy \n2. Medium \n3. Hard\nYou Chose- ")
print("What topic do you want to practice?: ")
valid_topics = ["arrays", "strings", "trees", "graphs", "linked lists", 
                "stacks", "queues", "dynamic programming", "recursion", "sorting"]

for i, t in enumerate(valid_topics, 1):
    print(f"{i}. {t}")

#validating the topic input 
topic_input = input("Choose a topic (enter number or name): ").lower().strip()

# check if they typed a number
if topic_input.isdigit() and 1 <= int(topic_input) <= len(valid_topics):
    topic = valid_topics[int(topic_input) - 1]
# check if they typed a valid name
elif topic_input in valid_topics:
    topic = topic_input
else:
    print("Invalid topic, exiting.")
    sys.exit(1)

#converting user_input to lowercase and checking for the difficulty level
user_input = user_input.lower()
diff = "hard"
if user_input == "1" or user_input == "easy":
    diff = "easy"
elif user_input == "2" or user_input == "medium":
    diff = "medium"
elif user_input == "3" or user_input == "hard":
    diff = "hard"
else:
    #If the user input is invalid, we exit the program
    print ("Invalid Input, Exiting.")
    sys.exit(1)

#Generating the problem statement using the Gemini API
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Give me a {diff} difficulty DSA problem about {topic}. Just the problem statement, no solution."
)

#Printing the problem statement
print(response.text)

#Asking the user to describe their approach to solve the problem
user_answer = input("\nDescribe your approach to solve this: ")

feedback = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"DSA Problem: {response.text}\n\nStudent's approach: {user_answer}\n\nEvaluate if this approach is correct. Explain why or why not, and mention the time complexity."
)

#Printing the feedback from the model
print(feedback.text)

#Asking the user if they want to try another problem
again = input("\nWant another problem? (yes/no): ")
if again.lower() == "yes":
    print("Restart the program to go again!")
else:
    print("Thanks for using the DSA quizzer! Goodbye!")