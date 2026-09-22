import gradio as gr
from classifier import process_messages

def analyze(text):
    summary, results = process_messages(text)
    
    output_html = """
    <style>
        .result-box, .result-box p, .result-box li, .result-box strong, .result-box em {
            color: black !important;
        }
    </style>
    """
    output_html += f"<h3>Summary</h3><p>{summary}</p><hr/><h3>Detailed Results</h3>"
    
    if not results:
        return output_html + "<p>No messages analyzed.</p>"
        
    for res in results:
        if isinstance(res, dict) and "error" in res:
            output_html += f"""
            <div class="result-box" style="border: 1px solid #ffcccc; padding: 10px; margin-bottom: 10px; border-radius: 5px; background-color: #fff0f0;">
                <p><strong>Message:</strong> {res.get("message")}</p>
                <p style="color: red !important;"><strong>Error:</strong> {res.get("error")}</p>
            </div>
            """
        else:
            indicator = "🔴 Important" if res.importance == "Important" else "🟢 Normal"
            bg_color = "#fff0f0" if res.importance == "Important" else "#f0fff0"
            border_color = "#ffcccc" if res.importance == "Important" else "#ccffcc"
            
            output_html += f"""
            <div class="result-box" style="border: 1px solid {border_color}; padding: 10px; margin-bottom: 10px; border-radius: 5px; background-color: {bg_color};">
                <p><strong>Message:</strong> <em>"{res.message}"</em></p>
                <p><strong>{indicator}</strong></p>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li><strong>Category:</strong> {res.category}</li>
                    <li><strong>Priority:</strong> {res.priority}</li>
                    <li><strong>Action:</strong> {res.action}</li>
                    <li><strong>Reason:</strong> {res.reason}</li>
                </ul>
            </div>
            """
            
    return output_html

with gr.Blocks(title="Automated Important Message Detection Agent") as demo:
    gr.Markdown("# Automated Important Message Detection Agent")
    gr.Markdown("An AI agent that identifies messages requiring immediate user attention.")
    
    with gr.Row():
        with gr.Column():
            input_box = gr.Textbox(
                lines=10, 
                placeholder="Enter messages here, separated by new lines...\n\nExample:\nYour assignment is due tomorrow.\nHey, are you coming to class?",
                label="Incoming Messages"
            )
            with gr.Row():
                analyze_btn = gr.Button("Analyze Messages", variant="primary")
                clear_btn = gr.Button("Clear")
        with gr.Column():
            output_box = gr.HTML(label="Analysis Results")
            
    analyze_btn.click(fn=analyze, inputs=input_box, outputs=output_box)
    clear_btn.click(fn=lambda: ("", ""), inputs=None, outputs=[input_box, output_box])

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000)),
        share=False
    )
