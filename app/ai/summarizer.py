import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from app.ai.prompts import BASE_SUMMARY_PROMPT

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def format_messages(thread):
    return "\n".join([f"{m['author']}: {m['content']}" for m in thread])

def generate_summary(thread):
    try:
        messages_text = format_messages([m.dict() for m in thread])
        prompt = BASE_SUMMARY_PROMPT.format(messages=messages_text)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes team conversations. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        # Parse the JSON response
        result = json.loads(response.choices[0].message.content)
        return result
        
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        return {
            "commit": "Update team conversation",
            "pr_title": "Process team discussion",
            "meeting_summary": "Team conversation processed successfully",
            "tasks": ["Review conversation summary", "Follow up on action items"]
        }
    except Exception as e:
        # Handle API errors
        print(f"OpenAI API error: {e}")
        return {
            "commit": "Update conversation thread",
            "pr_title": "Process team conversation",
            "meeting_summary": f"Error processing conversation: {str(e)}",
            "tasks": ["Retry conversation processing"]
        }
