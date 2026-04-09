#!/usr/bin/env python3
"""
Script to identify and remove missing images from gallery.html
"""

import os
import re
from pathlib import Path

def check_image_exists(image_path):
    """Check if an image file exists in the images directory"""
    full_path = Path("images") / image_path
    return full_path.exists()

def find_and_remove_missing_images():
    """Find missing images and remove their gallery items from gallery.html"""

    # Read gallery.html
    gallery_path = Path("gallery.html")
    if not gallery_path.exists():
        print("gallery.html not found")
        return

    with open(gallery_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all gallery items
    gallery_item_pattern = r'(\s*<div class="gallery-item"[^>]*>.*?</div>\s*)'
    gallery_items = re.findall(gallery_item_pattern, content, re.DOTALL)

    missing_items = []
    valid_items = []

    for item in gallery_items:
        # Extract image sources from this item
        img_sources = []

        # Check srcset (WebP)
        srcset_match = re.search(r'srcset="images/([^"]*)"', item)
        if srcset_match:
            img_sources.append(srcset_match.group(1))

        # Check src (fallback)
        src_match = re.search(r'src="images/([^"]*)"', item)
        if src_match:
            img_sources.append(src_match.group(1))

        # Check if any of the images exist
        item_has_valid_image = False
        for img_src in img_sources:
            if check_image_exists(img_src):
                item_has_valid_image = True
                break

        if item_has_valid_image:
            valid_items.append(item)
        else:
            missing_items.append(item)
            # Extract image names for reporting
            img_names = [src for src in img_sources if not check_image_exists(src)]
            print(f"Missing images: {img_names}")

    print(f"\nTotal gallery items: {len(gallery_items)}")
    print(f"Valid items: {len(valid_items)}")
    print(f"Items to remove: {len(missing_items)}")

    if missing_items:
        # Remove missing items from content
        for missing_item in missing_items:
            content = content.replace(missing_item, '', 1)

        # Write back the cleaned content
        with open(gallery_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\nRemoved {len(missing_items)} gallery items with missing images.")
    else:
        print("\nNo missing images found!")

if __name__ == "__main__":
    find_and_remove_missing_images()