import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()


# Giving the API key to the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Basic introducction and asking for difficulty level of the question
print("Hello, welcome to the DSA quizzer! Let's get you a problem to solve.")
print("Tell me the difficulty level of the questions you want to try")
strin = input("1. Easy \n2. Medium \n3. Hard\nYou Chose- ")

#converting response to lowercase and checking for the difficulty level
strin = strin.lower()
diff = "hard"
if strin == "1" or strin == "easy":
    diff = "easy"
elif strin == "2" or strin == "medium":
    diff = "medium"
elif strin == "3" or strin == "hard":
    diff = "hard"
else:
    #If the user input is invalid, we exit the program
    print ("Invalid Input, Exiting.")
    sys.exit(1)

#Generating the problem statement using the Gemini API
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a "+diff+" difficulty DSA problem about arrays. Just the problem statement, no solution."
)

#Printing the problem statement
print(response.text)