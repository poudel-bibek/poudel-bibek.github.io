from PIL import Image, ImageDraw, ImageFont
import os

def create_dummy_thumbnail(title, output_path, size=(350, 350)):
    # Create a new image with a light gray background
    img = Image.new('RGB', size, (240, 240, 240))
    draw = ImageDraw.Draw(img)
    
    # Draw a border
    draw.rectangle([(0, 0), (size[0]-1, size[1]-1)], outline=(200, 200, 200), width=2)
    
    # Add text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        font = ImageFont.load_default()
    
    # Split title into multiple lines if needed
    words = title.split()
    lines = []
    current_line = []
    current_width = 0
    
    for word in words:
        word_width = draw.textlength(word + " ", font=font)
        if current_width + word_width > size[0] - 40:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width
    
    if current_line:
        lines.append(" ".join(current_line))
    
    # Draw text
    y = (size[1] - len(lines) * 25) // 2
    for line in lines:
        text_width = draw.textlength(line, font=font)
        x = (size[0] - text_width) // 2
        draw.text((x, y), line, fill=(100, 100, 100), font=font)
        y += 25
    
    # Save the image
    img.save(output_path)

def main():
    # Create thumbnails directory if it doesn't exist
    thumbnails_dir = "content/posts/publications/thumbnails"
    os.makedirs(thumbnails_dir, exist_ok=True)
    
    # List of publications with their short names
    publications = {
        "joint-pedestrian": "Joint Pedestrian and Vehicle Traffic Optimization in Urban Environments using Reinforcement Learning",
        "vibrun": "VibRun: Real-time Contactless Gait Analysis for Treadmill Running via Footstep Vibrations",
        "pulseride": "PulseRide: A Robotic Wheelchair for Personalized Exertion Control with Human-in-the-Loop Reinforcement Learning",
        "endurl": "EnduRL: Enhancing Safety, Stability, and Efficiency of Mixed Traffic Under Real-World Perturbations Via Reinforcement Learning",
        "autojoin": "AutoJoin: Efficient Adversarial Training for Robust Maneuvering via Denoising Autoencoder and Joint Learning",
        "carl": "CARL: Congestion-Aware Reinforcement Learning for Imitation-based Perturbations in Mixed Traffic Control",
        "mtc-pixels": "Mixed Traffic Control and Coordination from Pixels",
        "chatgpt-its": "Can ChatGPT Enable ITS? The Case of Mixed Traffic Control via Reinforcement Learning",
        "dqs": "Efficient Quality-Diversity Optimization through Diverse Quality Species",
        "dc-motor": "Learning to Control DC Motor for Micromobility in Real Time with Reinforcement Learning",
        "black-box": "Black-box Adversarial Attacks on Network-wide Multi-step Traffic State Prediction Models"
    }
    
    # Generate thumbnails for each publication
    for short_name, full_title in publications.items():
        output_path = os.path.join(thumbnails_dir, f"{short_name}.png")
        create_dummy_thumbnail(full_title, output_path)
        print(f"Created thumbnail for {short_name}")

if __name__ == "__main__":
    main() 