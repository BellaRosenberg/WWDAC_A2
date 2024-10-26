
# AI Book Recommender

This project is an AI-based book recommendation system that allows users to input their favorite book titles and receive tailored book recommendations based on their preferences. The project uses the **Google Books API** to retrieve book data and the **Anthropic Claude API** to generate recommendations.

## Setup

### Requirements

To run this project, you need the following dependencies, which are listed in the `requirements.txt` file:

- `requests`: Used to send HTTP requests to the Google Books API.
- `anthropic`: The Python package used to interface with the Claude API for generating recommendations.

The `requirements.txt` file is located in the root directory of this project.

You will also need an Anthropic API key. Once retrieved you need to make a file named ".env" with the following line:

ANTHROPIC_API_KEY=<PASTE YOUR API KEY HERE>

Note that the API key must be a string.

### Installation Steps

1. **Clone the repository** to your local machine:

```bash
git clone https://github.com/your-repository-url.git
```

2. **Create a virtual environment** to manage dependencies:

```bash
python -m venv ai_book_recommender_env
```

3. **Activate the virtual environment and initialise environment variables**:

   - On macOS/Linux:
     ```bash
     source ai_book_recommender_env/bin/activate && source .env
     ```

4. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

5. **Obtain API keys**:
   - Sign up for the **Google Books API** [here](https://developers.google.com/books/docs/v1/using).
   - Obtain an API key from **Anthropic Claude** by creating an account at [Anthropic's website](https://www.anthropic.com).

6. **Create a `.env` file** in the root of your project folder and store your API keys like this:

```
GOOGLE_BOOKS_API_KEY=your-google-books-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

7. **Run the project**:

```bash
python main.py
```

## Usage

Once you have successfully set up the project and obtained the necessary API keys, you can use the AI Book Recommender by following these steps:

### Example Use Case

1. **Greet the user** and ask how many books they want to enter:

```python
def greeting():
    print("Welcome to the AI Book Recommender!")
    # More code...
```

2. **User inputs favorite book titles**:

```python
# Gather number of books the user wants to input
num_books = get_num_books()

# Collect the user's favorite books
fav_books = collect_fav_books(num_books=num_books)
```

3. **Retrieve book details** using the Google Books API:

```python
# Fetch details like author and genre
fav_details = get_books_details(book_titles=fav_books)
```

4. **Generate recommendations** using Claude API:

```python
# Generate recommendations based on the user's input
prompt = generate_prompt(fav_details=fav_details)
recommendations = get_claude_recommendations(api_key=anthropic_api_key, prompt=prompt)
print(recommendations)
```

### Example Output

```
How many book preferences would you like to enter (Please enter a number)? 3
Title: To Kill a Mockingbird
Title: 1984
Title: Pride and Prejudice

Searching for 'To Kill a Mockingbird' on Google Books...
Searching for '1984' on Google Books...
Searching for 'Pride and Prejudice' on Google Books...

Generating recommendations based on your input...
Here are your recommendations:
1. "Book Title A" by Author X
2. "Book Title B" by Author Y
3. "Book Title C" by Author Z
```

## Project Status

**Project Status**: In progress

The project is currently functional but still being actively developed. The core functionality (retrieving book data and generating recommendations) works as intended, but there are some areas that need improvement.

## Room for Improvement

### Improvements Needed
1. **Improve the recommendation model**: Right now, the recommendations rely on data provided by the Google Books API and Claude. A more sophisticated recommendation algorithm that takes into account additional factors like user ratings, review sentiment, or reading history would improve results.
2. **Enhance user experience**: The command-line interface could be expanded to include more features such as filtering recommendations by genre or length.

### Future To-Dos
1. **Add user accounts**: Let users save their preferences and book recommendations across sessions.
2. **Introduce pagination**: Handle larger datasets when fetching books from Google Books.
3. **Optimize API usage**: Implement better error handling and optimization for the Google Books API to avoid exceeding quotas.

## Acknowledgements

- This project was inspired by various **AI recommendation systems** and **book API projects**.
- The initial setup for the **Claude API** was guided by **Anthropic's official documentation**.
- Many thanks to **peers and instructors** for their valuable feedback throughout the project development process. 

Feel free to contribute or raise issues to improve the project!
