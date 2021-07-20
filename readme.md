# Multithread Youtube Downloader

Now you can download multiple videos from Youtube in paralell! Powered by <code>Pytube</code> (you can easily select another binary of your choice), you just have to save all your links into a .txt file and voila!, this script does the rest!

## Instalation

Use the package manager pip3 to install the dependencies.

    pip3 install -r requirements.txt

## Usage

```bash
# Example!

python3 main.py --input_list my_urls.txt --threads_qty 8
```
Both arguments are optional:

```bash
--input_list    (DEFAULT='input_file.txt')
--threads_qty   (DEFAULT=4)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)