import os  # Import the 'os' module to interact with environment variables
from openai import OpenAI  # Import OpenAI module for interacting with the OpenAI API
from dotenv import load_dotenv  # Import 'load_dotenv' to load environment variables from a .env file

# Load environment variables from a .env file
load_dotenv()

# Initialize the Azure OpenAI client using environment variables for the API endpoint and key
client = OpenAI(
    base_url=os.environ.get("API_ENDPOINT"),  # Fetch the API endpoint from environment variables
    api_key=os.environ.get("API_KEY"),  # Fetch the API key from environment variables
)

# Initial system message to define the assistant's behavior or persona
messages = [
    {"role": "system", "content": ''' YOU ARE AN AGENT ! '''},  # Initial instruction for the AI system
]

# Inform the user how to exit
print("Type 'exit' anytime to quit the program.")  # Inform the user they can type 'exit' to exit

# Interaction loop with the user
while True:
    # Get input from the user
    user_input = input("You : ")  # Prompt the user to enter a message

    # Exit the loop if the user types "exit"
    if user_input.lower() == "exit":  # If the user inputs 'exit', break the loop
        print("Bye !")  # Say goodbye
        break  # Exit the loop

    # Add the user's message to the conversation history
    messages.append({"role": "user", "content": user_input})  # Append user's input to the messages list

    # Call the Azure OpenAI API to get a response from the assistant
    response = client.chat.completions.create(
        model=os.environ.get("MODEL"),  # Use the model defined in environment variables
        messages=messages,  # Pass the conversation history (including system and user messages)
        stream=False  # Disable streaming, wait for the full response
    )

    # Retrieve and display the assistant's response
    ai_response = response.choices[0].message.content  # Get the AI's reply from the response object
    print(f"ERIOS Assistant : {ai_response}")  # Display the AI's response to the user

    # Add the assistant's response to the conversation history to maintain context
    messages.append({"role": "assistant", "content": ai_response})  # Append AI's response to the messages list
