#!/usr/bin/env python3
"""
Update gallery.html to use <picture> elements with WebP and JPEG fallbacks.
This allows the gallery to automatically use enhanced WebP images when available,
with JPEG fallbacks for older browsers.
"""

from pathlib import Path
import re

def update_gallery_images():
    """Convert gallery images to use <picture> elements"""
    gallery_path = Path('gallery.html')
    content = gallery_path.read_text(encoding='utf-8')

    # Pattern to match entire gallery items with img tags
    # Looking for: <img src="images/[filename].jpg" alt="[alt]" loading="lazy" />
    pattern = r'<img src="(images/[^"]+\.jpg)" alt="([^"]*)" loading="lazy" />'

    def replace_with_picture(match):
        full_path = match.group(1)
        alt_text = match.group(2)
        filename = Path(full_path).name
        base_name = Path(filename).stem

        return f'<picture><source srcset="images/{base_name}_enhanced.webp" type="image/webp"><img src="{full_path}" alt="{alt_text}" loading="lazy" /></picture>'

    new_content = re.sub(pattern, replace_with_picture, content)

    if new_content != content:
        gallery_path.write_text(new_content, encoding='utf-8')
        print("Gallery.html updated successfully!")
        print("Images now use <picture> elements with WebP support")
        print("Run enhance_gallery.py to generate the enhanced WebP images")
    else:
        print("No changes made - images may already be using <picture> elements")

if __name__ == "__main__":
    update_gallery_images()
