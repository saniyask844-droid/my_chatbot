# PROJECT NAME: User Todo Summary Chatbot

# DESCRIPTION:
This is a Flask-based chatbot application that fetches data from the JSONPlaceholder API. 
When a user provides a User ID (between 1-10), the bot calculates and displays a 
summary of their tasks, including total todos, completed tasks, pending tasks, 
and completion percentage.

# PREREQUISITES:
- Python 3.x installed
- Stable internet connection (to fetch real-time API data)

# HOW TO RUN:
1. Open your terminal/command prompt.
2. Install the required libraries by running: 
   pip install flask requests
3. Start the application by running: 
   python app.py
4. Open your web browser and go to: 
   http://127.0.0.1:5000

# KEY FEATURES:
- Dynamic API Filtering: Fetches and processes user-specific data in real-time.
- Interactive UI: "Bot is typing..." loading indicator for a realistic chat experience.
- Robust Validation: Handles non-integer inputs, empty fields, and API/network errors gracefully.
- Responsive Design: Clean and readable chat interface.