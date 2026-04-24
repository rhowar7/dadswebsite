#!/usr/bin/env python3
"""
Gallery Image Enhancement Script
Run this locally to batch enhance all gallery images for web optimization.

Usage: python enhance_gallery.py

Requirements: pip install pillow

This script will:
1. Process all 76 gallery images
2. Apply sharpening, brightness, and contrast enhancements
3. Resize images to web-optimized dimensions (max 1200px)
4. Convert to WebP format with optimal compression
5. Maintain original images as backups
"""

from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance
import os
import sys

def enhance_image(input_path, output_path=None, operations=None):
    """Enhance a single image with specified operations"""
    if operations is None:
        operations = {}

    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
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

            # Determine output path
            if output_path is None:
                base = Path(input_path)
                new_format = operations.get('format', 'webp')
                output_path = base.parent / f"{base.stem}_enhanced.{new_format}"

            # Save with optimal settings
            save_kwargs = {}
            if output_path.suffix.lower() == '.webp':
                save_kwargs['quality'] = operations.get('quality', 85)
                save_kwargs['method'] = 6  # Best compression
            elif output_path.suffix.lower() in ['.jpg', '.jpeg']:
                save_kwargs['quality'] = operations.get('quality', 85)
                save_kwargs['optimize'] = True

            img.save(output_path, **save_kwargs)
            return True

    except Exception as e:
        print(f"FAILED to enhance {input_path.name}: {e}")
        return False

def batch_enhance_gallery():
    """Batch enhance all gallery images"""
    script_dir = Path(__file__).parent
    images_dir = script_dir / 'images'

    if not images_dir.exists():
        print("ERROR: Images directory not found. Please run this script from the website root directory.")
        return

    # All gallery images from the HTML
    gallery_images = [
        '468917837_598960172707796_4392995363642965109_n.jpg',
        '469054715_598960186041128_8977828184486520472_n.jpg',
        '469060113_598959989374481_8005011486067409336_n.jpg',
        '469068295_598960359374444_1235283163084963995_n.jpg',
        '469069036_598960026041144_3615970573676701971_n.jpg',
        '469280556_598960316041115_6942750839963618547_n.jpg',
        '469312755_598960166041130_4458184962779155438_n.jpg',
        '469327074_598960179374462_5671155366752172906_n (1).jpg',
        '469327074_598960179374462_5671155366752172906_n (2).jpg',
        '469327074_598960179374462_5671155366752172906_n (3).jpg',
        '469340448_598960516041095_1353663974947487406_n.jpg',
        '469356996_598960512707762_5288148795746564193_n.jpg',
        '469384157_598960356041111_2681682371082480057_n.jpg',
        '469792279_604267038843776_2918372920635893567_n.jpg',
        '469792790_604266825510464_5518029663481596237_n.jpg',
        '469794219_604266972177116_162021975549140524_n.jpg',
        '469797041_604266875510459_5437632338137401609_n.jpg',
        '469798453_604267812177032_7077985023241179798_n.jpg',
        '469798453_604267812177032_7077985023241179798_n (1).jpg',
        '469800303_604266662177147_3682357505085647304_n.jpg',
        '469901775_604266822177131_8682149838933231815_n.jpg',
        '469920376_604266695510477_4769213215063635563_n.jpg',
        '469928540_604267012177112_5290904890683240457_n.jpg',
        '469930539_604266798843800_1288957857041031147_n.jpg',
        '469930951_604266745510472_7309024063734482301_n.jpg',
        '469931567_604267885510358_8858479463770053695_n.jpg',
        '469931567_604267885510358_8858479463770053695_n (1).jpg',
        '469969278_604266698843810_4173337286265709613_n.jpg',
        '469969925_604267045510442_4449944546144782488_n.jpg',
        '469981913_604266735510473_7958627480631772228_n.jpg',
        '469982106_604266995510447_5233274699003462931_n.jpg',
        '470043545_604266838843796_7308691180477622952_n.jpg',
        '470060864_604266882177125_337319679168049871_n.jpg',
        '470076784_604267042177109_6806057666459142188_n.jpg',
        '470086205_604266612177152_5307626397710960313_n.jpg',
        '470086412_604266615510485_2631837733401361939_n.jpg',
        '470087458_604266868843793_3533790342271227478_n.jpg',
        '470130901_604266682177145_8866535896523768724_n.jpg',
        '470170580_605479325389214_8818592383256207584_n.jpg',
        '470170580_605479325389214_8818592383256207584_n (1).jpg',
        '470172306_604267058843774_4585589275804146652_n.jpg',
        '470173310_604266622177151_8381389229356469565_n.jpg',
        '470173610_604266828843797_7102076533589677417_n.jpg',
        '470173864_604266872177126_7199608696422742242_n.jpg',
        '470173884_604266958843784_4983926025867088_n.jpg',
        '470174564_604266625510484_6220679843727327736_n.jpg',
        '470175479_605479185389228_2337300550703062153_n.jpg',
        '470175479_605479185389228_2337300550703062153_n (1).jpg',
        '470176197_604266962177117_3698534254084899071_n.jpg',
        '470178248_604266772177136_5035603731384110708_n.jpg',
        '470178475_604266982177115_6016257473353095909_n.jpg',
        '470182750_604266652177148_5765796464376076267_n.jpg',
        '470185974_604266688843811_6028303521662865661_n.jpg',
        '470186439_605479425389204_9029043948128750672_n.jpg',
        '470186439_605479425389204_9029043948128750672_n (1).jpg',
        '470187616_604267008843779_7501600216774408090_n.jpg',
        '470188609_604266618843818_2243950410113845959_n.jpg',
        '470188988_604266932177120_2973055033104807271_n.jpg',
        '470189017_604266912177122_8983506294378210819_n.jpg',
        '470189163_604266768843803_3985188361236407637_n.jpg',
        '470196517_604266865510460_7316629597089257670_n.jpg',
        '470196846_604267015510445_7834194499158768662_n.jpg',
        '470197334_604266692177144_509694744473799404_n.jpg',
        '470201725_604266732177140_6083694743268106448_n.jpg',
        '470205969_604266792177134_1906951095019877631_n.jpg',
        '470206138_604267055510441_4028444999450946628_n.jpg',
        '470208147_604266702177143_2880483880002985097_n.jpg',
        '470208770_604266718843808_1900626128399653328_n.jpg',
        '470210271_604266832177130_2133401833830188241_n.jpg',
        '470211150_604267025510444_1493998338960857410_n.jpg',
        '470223783_604266898843790_3703887429629729522_n.jpg',
        '470296676_604267028843777_8306077024170358696_n.jpg',
        '470305476_604266685510478_3357339723131912740_n.jpg',
        '470320043_604267035510443_7095239707593958810_n.jpg',
        '473724762_626919813245165_9148578232732617382_n.jpg',
        '473724762_626919813245165_9148578232732617382_n (1).jpg'
    ]

    # Enhancement settings
    enhancement_ops = {
        'sharpen': True,
        'brightness': 1.05,  # +5% brightness
        'contrast': 1.08,    # +8% contrast
        'resize': 1200,      # Max dimension
        'format': 'webp',
        'quality': 85
    }

    print("Starting batch enhancement of gallery images...")
    print(f"Processing {len(gallery_images)} gallery images")
    print("Enhancement settings:")
    print("   - Sharpening: Enabled")
    print("   - Brightness: +5%")
    print("   - Contrast: +8%")
    print("   - Max size: 1200px")
    print("   - Format: WebP (85% quality)")
    print()

    enhanced_count = 0
    failed_count = 0
    total_original_size = 0
    total_enhanced_size = 0

    for img_name in gallery_images:
        img_path = images_dir / img_name
        if img_path.exists():
            # Get original file size
            original_size = img_path.stat().st_size
            total_original_size += original_size

            if enhance_image(img_path, operations=enhancement_ops):
                enhanced_count += 1
                # Get enhanced file size
                enhanced_path = images_dir / f"{Path(img_name).stem}_enhanced.webp"
                if enhanced_path.exists():
                    enhanced_size = enhanced_path.stat().st_size
                    total_enhanced_size += enhanced_size
            else:
                failed_count += 1
        else:
            print(f"Missing: {img_name}")
            failed_count += 1

    print()
    print("Batch enhancement complete!")
    print(f"Results: {enhanced_count} enhanced, {failed_count} failed")

    if total_enhanced_size > 0 and total_original_size > 0:
        savings_percent = (1 - total_enhanced_size / total_original_size) * 100
        print(f"File size reduction: {savings_percent:.1f}%")
    print("The HTML has been updated to use WebP images with JPEG fallbacks")
    print("Browsers will automatically use the best format available")

def main():
    """Main function"""
    print("Gallery Image Enhancement Script")
    print("=" * 40)

    # Check if PIL/Pillow is available
    try:
        import PIL
        print(f"OK: PIL/Pillow version: {PIL.__version__}")
    except ImportError:
        print("ERROR: PIL/Pillow not found. Install with: pip install pillow")
        sys.exit(1)

    # Check if we're in the right directory
    if not Path('images').exists():
        print("ERROR: 'images' directory not found. Please run from website root.")
        sys.exit(1)

    batch_enhance_gallery()

if __name__ == "__main__":
    main()