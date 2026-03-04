from flask import Flask, render_template, request, jsonify
import urllib.request
import json
import time  # Loading delay kosam

app = Flask(__name__)

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message", "").strip()
    user_input_lower = user_input.lower()
    
    # Managers adigina loading feel kosam artificial delay (1.5 seconds)
    time.sleep(1.5) 
    
    # 1. SPECIAL CASE: Ultra-Friendly Greeting for '@'
    if user_input == "@":
        return jsonify({"reply": "✨ <b>Hey there!</b> I'm so glad you reached out. I'm your Zevoir buddy, ready to crunch some numbers for you. Whenever you're ready, just toss me any <b>User ID from 1 to 10</b> and I'll whip up a report in a flash! 🚀"})

    # 2. STANDARD GREETINGS: (Hi, Hello, Hey)
    greetings = ["hi", "hello", "hey"]
    if any(word == user_input_lower for word in greetings):
        return jsonify({"reply": "👋 <b>Hello!</b> I am Zevoir Chatbot. Please provide any <b>User ID from 1 to 10</b> to generate your data report!"})

    # 3. SMART GUIDANCE: Clear range (1 to 10) for text or 'discuss'
    if not user_input.isdigit() or "discuss" in user_input_lower or "about" in user_input_lower:
        return jsonify({"reply": """
            👋 <b>Quick Tip:</b><br>
            I need a <b>Numerical ID</b> to show my data magic. <br><br>
            <b>Try this:</b> Enter any number <b>from 1 to 10</b>. <br>
            I'll immediately fetch the task statistics for that specific user! 📊
        """})
    
    # 4. VALID ID LOGIC
    u_id = int(user_input)
    data = fetch_data()
    
    if data is None:
        return jsonify({"reply": "⚠️ <b>System Alert:</b> Data fetch failed. Please try again."})
    
    user_tasks = [task for task in data if task['userId'] == u_id]
    
    if not user_tasks:
        return jsonify({"reply": f"🚫 <b>No Records:</b> No data found for User ID {u_id}. Please try a number <b>from 1 to 10</b>."})
    
    # Statistics Calculation
    total = len(user_tasks)
    completed = len([t for t in user_tasks if t['completed']])
    pending = total - completed
    perc = (completed / total) * 100
    titles = [t['title'] for t in user_tasks[:5]]
    
    reply = f"📊 <b>Analytics Report for User {u_id}:</b><br><br>"
    reply += f"📝 <b>Total Tasks:</b> {total}<br>"
    reply += f"✅ <b>Completed:</b> {completed}<br>"
    reply += f"⏳ <b>Pending:</b> {pending}<br>"
    reply += f"📈 <b>Success Rate:</b> {perc:.2f}%<br><br>"
    reply += "📌 <b>Top 5 Tasks:</b><br>"
    for t in titles:
        reply += f"◈ {t}<br>"
        
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)