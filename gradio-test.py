import gradio as gr
import torch

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

x = torch.rand(5, 3)
print(x)

