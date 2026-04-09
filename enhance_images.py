from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance
import os

def enhance_image(input_path, output_path=None, operations=None):
    """
    Enhance an image with various operations:
    - sharpen: Apply sharpening filter
    - brightness: Adjust brightness (1.0 = original, >1 = brighter)
    - contrast: Adjust contrast (1.0 = original, >1 = more contrast)
    - resize: Resize to max width/height while maintaining aspect ratio
    - format: Convert to different format (webp, jpg, png)
    - quality: JPEG/WebP quality (1-100)
    """
    if operations is None:
        operations = {}

    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (for JPEG/WebP)
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')

            # Apply enhancements
            if operations.get('brightness', 1.0) != 1.0:
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(operations['brightness'])

            if operations.get('contrast', 1.0) != 1.0:
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(operations['contrast'])

            if operations.get('sharpen', False):
                img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

            # Resize if specified
            if 'resize' in operations:
                max_size = operations['resize']
                img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

            # Determine output path and format
            if output_path is None:
                base = Path(input_path)
                new_format = operations.get('format', base.suffix[1:].lower())
                output_path = base.parent / f"{base.stem}_enhanced.{new_format}"

            # Save with appropriate settings
            save_kwargs = {}
            if output_path.suffix.lower() in ['.jpg', '.jpeg']:
                save_kwargs['quality'] = operations.get('quality', 85)
                save_kwargs['optimize'] = True
            elif output_path.suffix.lower() == '.webp':
                save_kwargs['quality'] = operations.get('quality', 85)
                save_kwargs['method'] = 6

            img.save(output_path, **save_kwargs)
            print(f"Enhanced: {input_path.name} -> {output_path.name}")
            return True

    except Exception as e:
        print(f"Failed to enhance {input_path.name}: {e}")
        return False

def batch_enhance_images(image_dir, patterns=None, operations=None):
    """
    Batch enhance images in a directory
    """
    if patterns is None:
        patterns = ['*.jpg', '*.jpeg', '*.png']

    if operations is None:
        operations = {
            'sharpen': True,
            'brightness': 1.1,
            'contrast': 1.1,
            'format': 'webp',
            'quality': 85
        }

    image_dir = Path(image_dir)
    enhanced_count = 0

    for pattern in patterns:
        for img_path in image_dir.glob(pattern):
            if enhance_image(img_path, operations=operations):
                enhanced_count += 1

    print(f"Enhanced {enhanced_count} images")

if __name__ == "__main__":
    # Example usage
    base_dir = Path('images')

    # Enhance logos with specific settings
    logos = ['FINAL.png', 'TopLeft.png']
    for logo in logos:
        logo_path = base_dir / logo
        if logo_path.exists():
            enhance_image(logo_path, operations={
                'sharpen': True,
                'brightness': 1.05,
                'contrast': 1.1,
                'format': 'webp',
                'quality': 90
            })

    # Enhance a few sample project images
    sample_images = [
        '469327074_598960179374462_5671155366752172906_n (1).jpg',
        '469068295_598960359374444_1235283263084963995_n.jpg',
        '469792279_604267038843776_2918372920635893567_n.jpg'
    ]

    for img_name in sample_images:
        img_path = base_dir / img_name
        if img_path.exists():
            enhance_image(img_path, operations={
                'sharpen': True,
                'brightness': 1.05,
                'contrast': 1.05,
                'resize': 1200,  # Max width/height
                'format': 'webp',
                'quality': 85
            })

    print("Image enhancement complete!")