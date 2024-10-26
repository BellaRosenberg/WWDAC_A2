import requests
import os
import anthropic
from dotenv import load_dotenv

def greeting():
    # print text to format and greet the user
    print("\n" + "+++" * 10 + "\n")
    print("      Welcome to the AI Book Recommender!" "\n")
    print("""Looking for your next great read? I am Ethan the Librarian, and I'm here to help you discover books you'll love based on your preferences. 
Whether you're into thrilling mysteries, heartwarming romances, or insightful non-fiction, we've got recommendations just for you!
          
      Ready to start?
          """)
    return

def get_num_books():
    # create a loop to ensure the input is a number
    while True:
        # ask for user input
        num_books = input("How many book preferences would you like to enter (Please enter a number)? ")
        # check if number
        try:
            num_books = int(num_books)
            break  # if input is a valid integer, break out of the loop
        # if not a number, print error message and loop again
        except ValueError:
            print("Please try again, and enter a number.")
    return num_books

def collect_fav_books(num_books):
    print("\n      Now let's find out what are some of your favourite books! \n")
    print("\n      One by one, enter the title of your favourite book/s \n")
    # create a list to store the books a user enters
    book_storage = []
    # loop through the amount of books that user wants to enter
    for i in range(num_books):
        book = input("Title: ")
        book_storage.append(book)

    return book_storage
    

def search_google_books(book_title, api_key):
    # define the Google Books API endpoint
    search_url = "https://www.googleapis.com/books/v1/volumes"

    # set up query parameters
    params = {
        'q': book_title,
        'maxResults': 1,          
        'key': api_key # input API key
    }

    try:
        # send a GET request to the Google Books API
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Books API: {e}")
        return None

    # parse the JSON response
    data = response.json()

    # check if any items were returned
    if 'items' in data and len(data['items']) > 0:
        first_result = data['items'][0]['volumeInfo']

        # extract necessary details
        book_details = {
            'title': first_result.get('title', 'Title not found'),
            'author': first_result.get('authors', ['Unknown'])[0],  # get the first author name
            'genres': first_result.get('categories', []) # list of subjects or genres
        }

        return book_details
    else:
        print(f"No results found for '{book_title}'")
        return None
    
def get_books_details(book_titles):
    books_details = []
    
    for title in book_titles:
        print(f"Searching for '{title}' on Google Books...")
        details = search_google_books(title, api_key="AIzaSyC3VVyEymkVwD9POP2HAoT9Ouh3XTpMCGY")
        
        if details:
            books_details.append(details)
    
    return books_details

# function to format the data from Open Library into a better format for the prompt
def format_book_details_for_prompt(book_details_list):
    return "\n".join([
        f"Title: {book['title']}\nAuthor: {book['author']}\nGenres: {', '.join(book['genres'])}\n"
        for book in book_details_list
    ])

# # function to generate prompt for claude
def generate_prompt(fav_details):
    prompt_begin = "Please produce book recommendations based on the following data:"

    prompt_end = "Please be eloquent in your answers, and provide clear reasons as to why these recommendations are made based on the inputted data."
    
    prompt = f"{prompt_begin}\n{fav_details}\n{prompt_end}"

    return prompt

# function to create an instance of Claude and get recommendations
def get_claude_recommendations(api_key, prompt):

    # set up the client
    client = anthropic.Anthropic(api_key=api_key)
    
    # send a message to Claude
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content


def main():

    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
    # greet the user
    greeting()
    # gather how many books user wants to input
    num_books = get_num_books()
    # collect titles/authors of user's fav books
    fav_books = collect_fav_books(num_books=num_books)
    # get book details from fav books
    fav_details = get_books_details(book_titles=fav_books)
    # generate prompt from favourite book details
    prompt = generate_prompt(fav_details=fav_details)
    # now pass the information into the anthropic API
    reco = get_claude_recommendations(api_key=anthropic_api_key, prompt=prompt)
     
    
    for chunk in reco:
        print(chunk.text)


    return

load_dotenv()

if __name__=="__main__":

    main()
