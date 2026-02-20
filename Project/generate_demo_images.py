import numpy as np
from PIL import Image, ImageDraw
import os

# Create demo images directory
demo_dir = 'static/images'
if not os.path.exists(demo_dir):
    os.makedirs(demo_dir)

def create_rbc_image():
    """Create a sample RBC (Red Blood Cell) image"""
    img = Image.new('RGB', (224, 224), color='white')
    draw = ImageDraw.Draw(img)
    
    # RBC is typically round and reddish
    draw.ellipse([40, 40, 180, 180], fill=(220, 80, 80), outline=(150, 30, 30))
    draw.ellipse([60, 60, 160, 160], fill=(255, 100, 100), outline=(200, 50, 50))
    
    # Add some texture
    for i in range(20):
        x = np.random.randint(50, 170)
        y = np.random.randint(50, 170)
        draw.ellipse([x, y, x+5, y+5], fill=(200, 60, 60))
    
    img.save(f'{demo_dir}/demo_rbc.png')
    print("✓ Created demo_rbc.png")

def create_wbc_image():
    """Create a sample WBC (White Blood Cell) image"""
    img = Image.new('RGB', (224, 224), color='white')
    draw = ImageDraw.Draw(img)
    
    # WBC is larger and has nucleus
    draw.ellipse([30, 30, 190, 190], fill=(200, 200, 220), outline=(100, 100, 150))
    
    # Large nucleus in center
    draw.ellipse([70, 70, 150, 150], fill=(150, 120, 200), outline=(80, 50, 150))
    
    # Add granules around nucleus
    for i in range(30):
        x = np.random.randint(40, 180)
        y = np.random.randint(40, 180)
        draw.ellipse([x, y, x+6, y+6], fill=(120, 100, 180))
    
    img.save(f'{demo_dir}/demo_wbc.png')
    print("✓ Created demo_wbc.png")

def create_platelet_image():
    """Create a sample Platelet image"""
    img = Image.new('RGB', (224, 224), color='white')
    draw = ImageDraw.Draw(img)
    
    # Platelets are small and oval-shaped
    # Create multiple small platelets
    positions = [
        (40, 50, 100, 100),
        (130, 60, 180, 110),
        (50, 130, 100, 170),
        (140, 130, 190, 170),
        (80, 80, 140, 130)
    ]
    
    for pos in positions:
        draw.ellipse(pos, fill=(220, 150, 80), outline=(180, 100, 30))
    
    # Add some texture
    for i in range(25):
        x = np.random.randint(40, 180)
        y = np.random.randint(50, 170)
        draw.ellipse([x, y, x+4, y+4], fill=(190, 120, 50))
    
    img.save(f'{demo_dir}/demo_platelet.png')
    print("✓ Created demo_platelet.png")

def create_mixed_image():
    """Create a mixed sample image"""
    img = Image.new('RGB', (224, 224), color='white')
    draw = ImageDraw.Draw(img)
    
    # RBC
    draw.ellipse([20, 20, 80, 80], fill=(220, 80, 80), outline=(150, 30, 30))
    
    # WBC
    draw.ellipse([140, 140, 200, 200], fill=(200, 200, 220), outline=(100, 100, 150))
    draw.ellipse([160, 160, 180, 180], fill=(150, 120, 200), outline=(80, 50, 150))
    
    # Platelets
    draw.ellipse([140, 30, 180, 70], fill=(220, 150, 80), outline=(180, 100, 30))
    draw.ellipse([30, 140, 70, 170], fill=(220, 150, 80), outline=(180, 100, 30))
    
    img.save(f'{demo_dir}/demo_mixed.png')
    print("✓ Created demo_mixed.png")

if __name__ == '__main__':
    print("Generating demo blood cell images...")
    create_rbc_image()
    create_wbc_image()
    create_platelet_image()
    create_mixed_image()
    print("\n✅ Demo images created successfully!")
    print(f"Location: {demo_dir}/")
    print("\nYou can now test the app with:")
    print("  - demo_rbc.png")
    print("  - demo_wbc.png")
    print("  - demo_platelet.png")
    print("  - demo_mixed.png")
