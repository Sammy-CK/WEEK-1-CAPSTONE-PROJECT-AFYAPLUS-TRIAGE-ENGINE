from util.prompt import PROMPT_V3

def define_messages(user_request):
    return [
        {
            "role": "system",
            "content": PROMPT_V3
        },

        # Few-shot example 1
        {
            "role": "user",
            "content": "I have chest pain and I'm struggling to breathe."
        },
        {
            "role": "assistant",
            "content": """
{
  "is_critical_emergency": true,
  "detected_symptoms": ["chest pain", "difficulty breathing"],
  "clinical_reasoning_summary": "Symptoms may indicate a life-threatening emergency requiring immediate medical attention.",
  "routing_destination": "Emergency Department"
}
"""
        },

        # Few-shot example 2
        {
            "role": "user",
            "content": "I am pregnant and have a severe headache, blurry vision, and swelling in my feet."
        },
        {
            "role": "assistant",
            "content": """
{
  "is_critical_emergency": true,
  "detected_symptoms": ["severe headache", "blurry vision", "swelling in feet"],
  "clinical_reasoning_summary": "Reported symptoms suggest a potentially serious maternal-health risk requiring urgent assessment.",
  "routing_destination": "Emergency Department"
}
"""
        },

        # Actual patient message
        {
            "role": "user",
            "content": user_request
        }
    ]