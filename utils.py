from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

def add_watermark(image, text="Generated with AI"):
    """Adds a visible watermark to the bottom-right corner."""
    watermarked = image.copy()
    draw = ImageDraw.Draw(watermarked)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth = bbox[2] - bbox[0]
    textheight = bbox[3] - bbox[1]
    
    width, height = image.size
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    return watermarked

def save_image_with_metadata(image, prompt, output_path):
    """Saves image with the prompt embedded in PNG metadata."""
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Prompt", prompt)
    metadata.add_text("Software", "AI Image Generator Task")
    
    image.save(output_path, "PNG", pnginfo=metadata)
