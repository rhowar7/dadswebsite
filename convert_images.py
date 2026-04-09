from pathlib import Path
from PIL import Image

base = Path('images')
# rename Final Logo.jpg -> final-logo.jpg
src = base / 'Final Logo.jpg'
tgt = base / 'final-logo.jpg'
if src.exists() and not tgt.exists():
    src.rename(tgt)
    print('renamed', src, '->', tgt)
elif not src.exists():
    print('source missing', src)
else:
    print('target exists', tgt)

files = [
    'final-logo.jpg',
    '469327074_598960179374462_5671155366752172906_n (1).jpg',
    '469068295_598960359374444_1235283263084963995_n.jpg',
    '469792279_604267038843776_2918372920635893567_n.jpg'
]
for name in files:
    jpg = base / name
    webp = base / (Path(name).stem + '.webp')
    if jpg.exists():
        try:
            with Image.open(jpg) as im:
                im.convert('RGB').save(webp, 'WEBP', quality=85, method=6)
            print('converted', jpg.name, '->', webp.name)
        except Exception as e:
            print('failed', jpg.name, e)
    else:
        print('missing', jpg)
