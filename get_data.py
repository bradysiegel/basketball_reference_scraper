from basketball_reference_scraper.seasons import get_advanced_stats,get_per_game_stats
import os
import pathlib
import time

for i in range(1990, 2024):
    print('Downloading {}...'.format(i))

    pathlib.Path('./stats/{}'.format(i)).mkdir(parents=True, exist_ok=True)

    get_advanced_stats(i).to_csv('stats/{}/advanced.csv'.format(i))
    get_per_game_stats(i).to_csv('stats/{}/per_game.csv'.format(i))

    print('Done! Waiting 10 seconds...')

    time.sleep(10)
