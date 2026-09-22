# Automated Important Message Detection Agent

## 1. Problem Statement
In the modern digital age, individuals are inundated with hundreds of notifications daily—ranging from critical alerts to casual conversations. Missing an important message regarding academics, finances, or security can have severe consequences, while checking every notification reduces productivity.

## 2. Objective
To build an AI agent that automatically analyzes incoming text messages and determines their importance, category, priority, and required action, thereby assisting users in identifying messages that require immediate attention.

## 3. Proposed Solution
A lightweight, intelligent application that uses a Large Language Model (LLM) to semantically analyze messages. The system categorizes each message and flags important ones with a recommended action and reasoning, saving time and preventing missed deadlines.

## 4. System Architecture
User Input → Gradio Interface → Message Classification (LLM Agent) → Structured Output (Pydantic) → Gradio Results Display

### File Roles:
- **`app.py`**: The Gradio interface for input, output, and button handling.
- **`classifier.py`**: Handles splitting multiple messages and generating the summary.
- **`agent.py`**: Interacts with the Gemini API to get structured JSON classification.
- **`models.py`**: Contains Pydantic models enforcing the structured output.

## 5. Technologies Used
- **Python**: Core logic.
- **Gradio**: For building a simple, intuitive GUI.
- **Pydantic**: For defining and enforcing structured outputs.
- **Google GenAI API (Gemini)**: For semantic text classification.
- **python-dotenv**: For environment variable management.

## 6. Agent Workflow
1. The user inputs one or multiple messages separated by new lines.
2. `classifier.py` parses the input and sends each message to `agent.py`.
3. The LLM (Gemini) classifies the message against a set of predefined categories, importance levels, and priority queues, using the schema defined in `models.py`.
4. The system aggregates the results, computes a summary, and formats the output into readable HTML.
5. `app.py` renders the output back to the user via Gradio.

## 7. Features
- Supports batch processing of multiple messages.
- Real-time semantic analysis (not just keyword-based).
- Summarizes total, important, and normal messages.
- Highlights "Important" messages in red and "Normal" in green.

## 8. Installation
1. Clone the repository or download the project files.
2. Ensure Python 3.8+ is installed.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 9. How to Run
1. Create a `.env` file in the root directory (copy from `.env.example`).
2. Add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the displayed local URL (e.g., `http://127.0.0.1:7860/`) in your browser.

## 10. Example
**Input:**
Your university examination fee payment is due tomorrow. Complete the payment before 5 PM.

**Output:**
- **Importance:** Important
- **Category:** Academic
- **Priority:** High
- **Action:** Notify Immediately
- **Reason:** The message contains a payment deadline and requires the user to take action.

## 11. Limitations
- Requires an active internet connection to communicate with the LLM API.
- The latency is dependent on the response time of the Gemini API.
- Cannot currently connect directly to SMS or email platforms (runs as a standalone simulator).

## 12. Future Scope
- Integration with Android SMS API or Email Services for direct fetching.
- Customizable priority filters based on user profiles.
- On-device local models for privacy-focused offline message detection.
