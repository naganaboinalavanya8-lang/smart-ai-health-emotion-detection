import random

def predict_emotion(text):
    text = text.lower()

    if "sad" in text or "depressed" in text:
        return random.choice([
            "I'm really sorry you're feeling this way. Want to talk about it?",
            "It sounds like you're going through a tough time. I'm here to listen."
        ])
    
    elif "happy" in text or "good" in text:
        return random.choice([
            "That's nice to hear! Keep smiling 😊",
            "I'm glad you're feeling good today!"
        ])
    
    elif "stress" in text or "tired" in text:
        return random.choice([
            "You seem stressed. Try taking a short break or deep breathing.",
            "Taking a few slow, deep breaths might help you relax."
        ])
    
    elif "sleepy" in text or "sleep" in text:
        return random.choice([
            "You might need rest 😴. Try to relax and get proper sleep.",
            "A good night's sleep can make a big difference. Take care!"
        ])
    
    elif "anxious" in text or "worried" in text:
        return random.choice([
            "It's okay to feel anxious sometimes. I'm here with you.",
            "You're not alone—would you like to share what's worrying you?"
        ])
    
    elif "headache" in text or "head pain" in text or "migraine" in text:
        return random.choice([
            "I'm sorry you're experiencing a headache. Drinking water and resting may help.",
            "You might try relaxing in a quiet, dark room. If it persists, consider consulting a doctor."
        ])
    
    elif "hi" in text or "hello" in text or "hey" in text:
        return random.choice([
            "Hello! How are you feeling today?",
            "Hi there! I'm here to listen."
        ])
    
    else:
        return random.choice([
            "I'm here for you. Can you tell me more about what you're feeling?",
            "Thank you for sharing. Would you like to tell me more?",
            "I'm listening. What's been on your mind lately?"
        ])