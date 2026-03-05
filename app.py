import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message", "").strip()

    # 1. SYMBOLS CHECK (@, #, @@@)
    if not any(char.isalnum() for char in user_input) and user_input != "":
        response = "Oops! Those symbols look cool, but I'm better at handling numbers. ✨ Could you please try a numeric value instead?"

    # 2. TEXT CHECK (hello saniya, abcdefg)
    elif any(char.isalpha() for char in user_input):
        response = "Hello there! That's actually beyond my current research. 😊 Could you please try asking me something in a numeric value?"

    # 3. DECIMAL CHECK (2.5, 2.5555)
    elif "." in user_input and user_input.replace(".", "", 1).isdigit():
        response = "I see a decimal there! 😊 While that's a precise number, I currently only work with whole numeric values to show you the data magic."

    # 4. LARGE NUMBERS CHECK (999999999999...)
    elif user_input.isdigit() and len(user_input) > 2:
        response = "That's a huge number! 😲 My current system is designed to handle specific short numeric IDs. Could you try a smaller numeric value?"

    # 5. CORRECT IDs (1-10) - REAL STATISTICS WITH EMOJIS
    elif user_input.isdigit() and 1 <= int(user_input) <= 10:
        try:
            user_id = user_input
            api_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
            res = requests.get(api_url)
            todos = res.json()

            if todos:
                total = len(todos)
                completed = len([t for t in todos if t['completed']])
                pending = total - completed
                percent = (completed / total) * 100
                titles = [t['title'] for t in todos[:5]]  # First 5 titles

                # Meeru adigina statistics format with emojis
                response = (
                    f"<b>📊 User ID {user_id} Task Statistics:</b><br><br>"
                    f"🔢 Total Tasks: {total}<br>"
                    f"✅ Completed: {completed}<br>"
                    f"⏳ Pending: {pending}<br>"
                    f"🏆 Completion Rate: {percent:.2f}%<br><br>"
                    f"<b>📝 First 5 Titles:</b><br>"
                    + "".join([f"🔹 {title}<br>" for title in titles])
                )
            else:
                response = "No tasks found for this User ID. ❌"
        except Exception as e:
            response = "Error fetching data. Please try again later. ⚠️"

    # Default fallback
    else:
        response = "I'm still learning! 😊 Please enter a valid User ID to see the statistics."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)