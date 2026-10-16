"""
Data collection for INFO 2950 project: Lyrics vs. Audio Sentiment in Pop Music.

Downloads the two raw source files into data/raw/. Run once from the repo root:
    python collect_data.py

Sources
-------
1. Billboard Year-End Hot 100 lyrics, 1965-2015 (Kaylin Pavlik)
   https://github.com/walkerkq/musiclyrics
2. Spotify audio features for Billboard Hot 100 songs (Sean Miller via data.world,
   republished by TidyTuesday 2021-09-14)
   https://github.com/rfordatascience/tidytuesday/tree/master/data/2021/2021-09-14

Note: our Phase 1 plan was to call Spotify's /audio-features endpoint directly.
Spotify restricted that endpoint for new developer apps in November 2024 (requests
return 403), so we use the archived pull above, which was collected before the change.
"""

from pathlib import Path
from urllib.request import urlretrieve

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "billboard_lyrics_1964-2015.csv":
        "https://raw.githubusercontent.com/walkerkq/musiclyrics/master/billboard_lyrics_1964-2015.csv",
    "audio_features.csv":
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-09-14/audio_features.csv",
}

for fname, url in SOURCES.items():
    dest = RAW / fname
    if dest.exists():
        print(f"already have {dest}")
        continue
    print(f"downloading {url}")
    urlretrieve(url, dest)
    print(f"saved {dest}")
