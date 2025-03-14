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
    thumbnails_dir = "content/posts/projects/thumbnails"
    os.makedirs(thumbnails_dir, exist_ok=True)
    
    # List of projects with their names
    projects = {
        "documint": "DocuMint: Docstring Generation for Python using Small Language Models",
        "ai-assignments": "Artificial Intelligence Assignments",
        "barterbaron": "BarterBaron: A commerce app based on barter system trade",
        "steering-angle": "Robustness to Input Corruptions and Adversarial Examples in Steering Angle Prediction via Self-Supervision",
        "latent-representation": "Latent Representation of Inputs: A Defense Against Adversarial Examples in DQN",
        "hyperparameter": "Distributed Hyper-paramter tuning of Neural Networks",
        "3d-printer": "Delta Design 3D Printer"
    }
    
    # Generate thumbnails for each project
    for short_name, full_title in projects.items():
        output_path = os.path.join(thumbnails_dir, f"{short_name}.png")
        create_dummy_thumbnail(full_title, output_path)
        print(f"Created thumbnail for {short_name}")

if __name__ == "__main__":
    main() 