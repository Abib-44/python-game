
from browser import document, alert
from javascript import Math


number = int(Math.floor(Math.random() * 100)) + 1
attempts = 0

def check_guess(event):
    global attempts
    user_input = document["guessInput"].value
    feedback = document["feedback"]

    try:
        guess = int(user_input)
        attempts += 1
        diff = guess - number
        abs_diff = abs(diff)

        if abs_diff == 0:
            feedback.text = f"🎉 Congratulations! You've guessed the number {number} in {attempts} attempts."
        elif abs_diff >= 40:
            feedback.text = "🚀 Way off!"
        elif abs_diff >= 30:
            feedback.text = "🌋 Very far!"
        elif abs_diff >= 20:
            feedback.text = "⚡ Far!"
        elif abs_diff >= 10:
            feedback.text = "🔹 Getting closer!"
        elif abs_diff >= 5:
            feedback.text = "🔥 Close!"
        else:  # 1-4
            feedback.text = "✨ Very close!"
    except ValueError:
        feedback.text = "⚠️ Please enter a valid number."





document["submitBtn"].bind("click", check_guess)