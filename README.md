
# AI Book Recommender

This project is an AI book recommender that provides users with personalised book recommendations based on their preferences. It uses the **Google Books API** to retrieve book data and the **Anthropic Claude API** to generate recommendations.

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/BellaRosenberg/WWDAC_A2.git
```

2. **Create a virtual environment** to manage dependencies:

```bash
python -m venv ai_book_venv
```

3. **Activate the virtual environment and initialise environment variables**:

   - On macOS/Linux:
     ```bash
     source ai_book_venv/bin/activate && source .env
     ```

4. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

5. **Obtain API keys**:
   - Sign up for the **Google Books API** 
   - Obtain an API key from **Anthropic Claude** 

6. **Create a `.env` file** in the root of your project folder and store your API keys like this:

```
GOOGLE_BOOKS_API_KEY=your-google-books-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

7. **Run the project**:

```bash
python main.py
```