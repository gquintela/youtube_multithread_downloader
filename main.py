import sys
from utils import download_list, get_video_list, distribute_urls, download_videos, run
import argparse
from argparse import RawTextHelpFormatter

# --- PARSE ---

parser = argparse.ArgumentParser(
    description="""Youtube multithread downloader:
    Download as many Youtube videos as you want in paralell!
    (change the variable "binary" if you want to use another executable, default=pytube)
    """,
    formatter_class=RawTextHelpFormatter,
)

parser.add_argument(
    "--input_list",
    type=str,
    help="url input list (DEFAULT='input_file.txt')",
    default="input_file.txt",
    dest="input_list",
)

parser.add_argument(
    "--threads_qty",
    type=int,
    help="Define how many threads will be used (DEFAULT=4)",
    default=4,
    dest="threads_qty",
)
args = parser.parse_args()


# ---- MAIN PROGRAM ----
binary = "pytube"
file = args.input_list
threads_qty = args.threads_qty

if run(binary, file, threads_qty):
    print("all files downloaded.")
else:
    print("error while downloading, please try again.")
