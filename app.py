import streamlit as st
import pandas as pd

from llava import LLAVA

st.set_page_config(layout="wide")
st.title("LLAVA vs DALLE Image and Prompts")


#def read_midjourney_file():
#    return pd.read_parquet("C:/MyTemp/LLaVA/data/000000.parquet")

#df = read_midjourney_file()
#row = df.sample()
prompt_text = "A neon-lit cyberpunk city at night, filled with towering skyscrapers, flying cars, and busy streets, neon signs reflecting off the wet pavement, and people walking around in futuristic attire, with glowing lights everywhere."
image_url = "C:/MyTemp/LLaVA/data/cyberpunk.jpg"

image, prompt, lvm = st.columns(3)

with image:
    st.markdown("## Image")
    st.image(image_url, width=300)

with prompt:
    st.markdown("## Prompt")
    st.markdown(f"{prompt_text}")

with lvm:
    st.markdown("## LLAVA Description")    
    chat_box = st.empty()   
    with chat_box:
        content = ""
        first_chunk_rendered = False
        waiting = st.spinner("Generating description...")
        for chunk in LLAVA().complete(image_path=image_url, stream=True):
            content += f"{chunk}"
            if not first_chunk_rendered:
                first_chunk_rendered = True
            chat_box.markdown(content)
