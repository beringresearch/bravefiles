import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

import streamlit as st

def load_gpt2():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = TFGPT2LMHeadModel.from_pretrained("gpt2",
                                              pad_token_id=tokenizer.eos_token_id)
    return tokenizer, model

tokenizer, model = load_gpt2()
random_seed = st.sidebar.slider('seed', min_value=0, max_value=1234,
                              value=0, step=1)
max_length = st.sidebar.slider('max_length', min_value=1, max_value=100,
                               value=50, step=1)
top_p = st.sidebar.slider('top_p', min_value=0.0, max_value=1.0,
                          value=0.92, step=0.01)
top_k = st.sidebar.slider('top_k', min_value=0, max_value=100,
                          value=0, step=1)

def gpt2_generate(user_input,
                  random_seed=0,
                  max_length=50,
                  top_p=0.92,
                  top_k=0):
    input_ids = tokenizer.encode(user_input,
                                 return_tensors='tf')
    tf.random.set_seed(0)
    sample_output = model.generate(
        input_ids,
        do_sample=True,
        max_length=max_length,
        top_p=top_p,
        top_k=top_k
    )

    result = tokenizer.decode(sample_output[0], skip_special_tokens=True)
    return(result)

user_input = st.text_area('', 'I love System Containers')

if st.button('Talk to me!'):
    output = gpt2_generate(user_input,
                           random_seed=random_seed,
                           max_length=max_length,
                           top_p=top_p, top_k=top_k)
    st.write(output)
