from agent import analyze_message_with_llm
from models import MessageAnalysis
from typing import List, Dict, Any, Tuple

def process_messages(text_input: str) -> Tuple[str, List[Any]]:
    """
    Splits the input by newlines, processes each non-empty message,
    and returns a summary string and a list of parsed results.
    """
    if not text_input or not text_input.strip():
        return "No messages provided.", []

    raw_messages = [msg.strip() for msg in text_input.split('\n') if msg.strip()]
    results = []
    
    important_count = 0
    normal_count = 0

    for msg in raw_messages:
        try:
            analysis = analyze_message_with_llm(msg)
            if analysis:
                results.append(analysis)
                if analysis.importance == "Important":
                    important_count += 1
                else:
                    normal_count += 1
            else:
                results.append({
                    "message": msg,
                    "error": "Failed to analyze message. Ensure API key is valid."
                })
        except Exception as e:
            results.append({
                "message": msg,
                "error": f"Error: {str(e)}"
            })
            
    summary = (
        f"Total Messages: {len(raw_messages)} | "
        f"Important: {important_count} | "
        f"Normal: {normal_count}"
    )

    return summary, results
