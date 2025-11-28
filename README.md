# 🎨 AI-Powered Image Generator

## Project Overview
This project is a locally hosted Text-to-Image generation application built using **Python**, **Streamlit**, and the **Stable Diffusion** model (via Hugging Face Diffusers). It allows users to input text prompts and generate high-quality images with customizable settings.

The system is designed with ethical AI practices in mind, featuring visible watermarking, metadata embedding, and an integrated safety checker.

## 🚀 Features
* **Text-to-Image Generation:** Converts natural language prompts into images using `stable-diffusion-v1-5`.
* **Hardware Agnostic:** Automatically detects and runs on **GPU (CUDA)** for speed or falls back to **CPU** for compatibility.
* **Customizable Settings:** Adjust the number of images, inference steps (quality), and guidance scale (creativity).
* **Image Enhancement:** Supports negative prompts to filter out unwanted elements.
* **Ethical AI Implementation:**
    * **Watermarking:** Adds a "Generated with AI" overlay to all outputs.
    * **Safety Filter:** Blocks NSFW content generation.
* **Metadata Storage:** Embeds the prompt and generation details directly into the PNG file metadata.

## 🛠️ Technology Stack
* **Language:** Python 3.8+
* **UI Framework:** Streamlit
* **ML Framework:** PyTorch
* **Generative Model:** Stable Diffusion v1-5 (Diffusers library)
* **Image Processing:** Pillow (PIL)

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url-here>
cd ai_image_generator
