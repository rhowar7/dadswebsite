#!/usr/bin/env python3
"""
Script to identify missing images referenced in gallery.html
"""

import os
import re
from pathlib import Path

def find_missing_images():
    """Find images referenced in gallery.html that don't exist in images/ folder"""

    # Read gallery.html
    gallery_path = Path("gallery.html")
    if not gallery_path.exists():
        print("gallery.html not found")
        return

    with open(gallery_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all image src attributes
    img_pattern = r'srcset="images/([^"]*\.webp)"|src="images/([^"]*\.(?:jpg|jpeg|png|gif|webp))"'
    matches = re.findall(img_pattern, content)

    # Flatten the matches (some are from srcset, some from src)
    referenced_images = set()
    for match in matches:
        img = match[0] or match[1]  # Take the non-empty group
        if img:
            referenced_images.add(img)

    # Get actual files in images directory
    images_dir = Path("images")
    if not images_dir.exists():
        print("images/ directory not found")
        return

    actual_files = set()
    for file_path in images_dir.rglob("*"):
        if file_path.is_file():
            actual_files.add(file_path.name)

    # Find missing images
    missing_images = []
    for img in referenced_images:
        if img not in actual_files:
            missing_images.append(img)

    print(f"Total images referenced in gallery.html: {len(referenced_images)}")
    print(f"Total files in images/ directory: {len(actual_files)}")
    print(f"Missing images: {len(missing_images)}")

    if missing_images:
        print("\nMissing images:")
        for img in sorted(missing_images):
            print(f"  - {img}")
    else:
        print("\nAll referenced images exist!")

    return missing_images

if __name__ == "__main__":
    find_missing_images()