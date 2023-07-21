import gradio as gr
from fastai import learner 
# from fastbook import *
# import pathlib


# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

bear_id = learner.load_learner(r'bear_identifier.pkl')
categories = ['black', 'grizzly', 'teddys']


def classify_bear(img):
    pred, pred_idx, probs = bear_id.predict(img)
    return dict(zip(categories, map(float,probs)))

image = gr.inputs.Image(shape=(224, 224))
label= gr.outputs.Label()

iface = gr.Interface(fn=classify_bear, inputs=image, outputs=label)
iface.launch()