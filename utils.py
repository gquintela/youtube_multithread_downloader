import subprocess
import threading
import os
from pathlib import Path


def download_list(binary, url_list):
    for url in url_list:
        try:
            subprocess.run([binary, url])
        except:
            print(f"{binary} error")
            exit(1)


def get_video_list(file):
    file_path = Path(file)
    if not file_path.is_file():
        print(f"{file} does not exist, please choose a valid input list file.")
        exit(0)
    try:
        with open(file) as file:
            videos_url_list = file.readlines()
            return videos_url_list
    except:
        print(f"ERROR while trying to read {file}. Exiting...")
        exit(1)


def distribute_urls(videos_url_list, threads_qty):
    # creates (#threads) lists (min between threads and total videos)
    effective_threads_qty = min(threads_qty, len(videos_url_list))
    url_list_of_lists = [[] for x in range(effective_threads_qty)]
    index_list = 0
    for url in videos_url_list:
        url_list_of_lists[index_list].append(url)
        index_list += 1
        if index_list >= effective_threads_qty:
            index_list = 0
    return url_list_of_lists


def download_videos(binary, url_list_of_lists):
    for url_list in url_list_of_lists:
        if len(url_list) != 0:
            try:
                x = threading.Thread(
                    target=download_list,
                    args=(
                        binary,
                        url_list,
                    ),
                )
                x.start()
            except:
                print("Thread error")
                exit(1)


def run(binary, file, threads_qty):
    try:
        videos_url_list = get_video_list(file)
        url_list_of_lists = distribute_urls(videos_url_list, threads_qty)
        download_videos(binary, url_list_of_lists)
        return True
    except:
        return False
