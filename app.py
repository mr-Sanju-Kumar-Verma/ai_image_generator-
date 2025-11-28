import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
import os
from datetime import datetime
from utils import add_watermark, save_image_with_metadata

MODEL_ID = "runwayml/stable-diffusion-v1-5"  el
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@st.cache_resource
def load_model():
    """
    Loads the model with automatic GPU/CPU fallback.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    dtype = torch.float16 if device == "cuda" else torch.float32
    
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID, 
        torch_dtype=dtype
    )
    pipe.to(device)
    
  
    return pipe, device

st.title("🎨 AI-Powered Image Generator")
st.markdown("Generate images from text using Stable Diffusion.")

with st.sidebar:
    st.header("Settings")
    num_images = st.slider("Number of Images", 1, 4, 1)
    guidance_scale = st.slider("Guidance Scale (Creativity)", 1.0, 20.0, 7.5)
    num_steps = st.slider("Inference Steps (Quality)", 10, 100, 30)
    
    st.info("Note: Higher steps = better quality but slower generation.")

prompt = st.text_area("Enter your prompt:", placeholder="A futuristic city at sunset...")
negative_prompt = st.text_input("Negative Prompt (Optional):", placeholder="blurry, low quality, distorted")

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt first!")
    else:
        try:
            with st.spinner("Loading Model & Generating... (This may take a minute)"):
                pipe, device = load_model()
                st.success(f"Model loaded on {device.upper()}")
                
                output = pipe(
                    prompt, 
                    negative_prompt=negative_prompt, 
                    num_inference_steps=num_steps,
                    guidance_scale=guidance_scale,
                    num_images_per_prompt=num_images
                )
                
                for i, image in enumerate(output.images):
                    if output.nsfw_content_detected and output.nsfw_content_detected[i]:
                        st.error(f"Image {i+1} blocked: Content filter triggered.")
                        continue

                    watermarked_img = add_watermark(image)
                    
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"img_{timestamp}_{i}.png"
                    filepath = os.path.join(OUTPUT_DIR, filename)
                    save_image_with_metadata(watermarked_img, prompt, filepath)
                    
                    st.image(watermarked_img, caption=f"Result {i+1}", use_column_width=True)
                    
                    with open(filepath, "rb") as file:
                        st.download_button(
                            label=f"Download Image {i+1}",
                            data=file,
                            file_name=filename,
                            mime="image/png"
                        )
                        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("If you are out of memory (CUDA OOM), try restarting with fewer images or lower steps.")
