import gradio as gr
from transformers import pipeline

instruct_pipeline = pipeline(model="../opt/dsi5inn7aonbmv3/dolly-v2-12b", trust_remote_code=True, device_map="auto")


def infer(inp):
    return instruct_pipeline(inp)

with gr.Blocks() as main:
    description_label = """
    <p style="text-align: center;">
        <span style="font-size: 28px; font-weight: bold;">Dolly - Inference</span>
        <br>
        Databricks’ dolly-v2-12b, an instruction-following large language model trained \n
        on the Databricks machine learning platform that is licensed for commercial use. \n        
    </p>
    <p style="text-align: center;">
        <br>
        Enter your text prompt below, and hit `Run inference` to generate text.   
    </p>
    """
    gr.HTML(description_label)
    inp = gr.Textbox(label = 'Text input')
    out = gr.Textbox(label = 'Text output')
    with gr.Row():
        but = gr.Button('Run inference')
    but.click(fn = infer, inputs = inp, outputs = out)
main.launch(share = True)