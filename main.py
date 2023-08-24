import os

from utils import get_youtube_data, create_database, save_data_to_database

from config import config

def main():
    api_key = os.getenv('YT_API_KEY')
    channel_ids = [
        'UCTyru90KSxLC-YXP4P736cA',  # zerolife50
        'UCc0D86KVm97quyFmgXKLaYw',  # Daria IsrLife

    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()