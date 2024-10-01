import os
import gradio as gr
import google.generativeai as genai

api_key = "YOUR_AISTUDIO_API_KEY_HERE"

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

def ask_question(question):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(question)
    return f"**AI**:\n\n{response.text}"

with gr.Blocks() as demo:
    gr.Markdown("# AI Chatbot Application by github.com/turhanenes")

    question_input = gr.Textbox(label="Write your question", placeholder="Write your question here...")
    
    output_text = gr.Markdown(label="AI")

    process_button = gr.Button("Send")

    process_button.click(ask_question, inputs=question_input, outputs=output_text)

demo.launch()