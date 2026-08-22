import json
import os

AREAS = {
    "sounds": (".mp3", ".ogg", ".wav"),
    "assets": (".png", ".jpg", ".jpeg", ".webp"),
    "images": (".png", ".jpg", ".jpeg"),
    "fonts": (".ttf", ".otf"),
}

manifest = {}

for area, extensions in AREAS.items():
    found = []

    if os.path.isdir(area):
        for root, _, filenames in os.walk(area):
            for name in filenames:
                if name.lower().endswith(extensions):
                    path = os.path.join(root, name)
                    found.append(os.path.relpath(path, area).replace(os.sep, "/"))

    manifest[area] = sorted(found)

with open("manifest.json", "w", encoding="utf-8", newline="\n") as handle:
    json.dump(manifest, handle, indent=2)
    handle.write("\n")
