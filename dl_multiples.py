import subprocess

if __name__ == "__main__":
    titles = ["Distinctive image features from scale-invariant keypoints"]
    for title in titles:
        subprocess.call(['python', 'sopaper.py', title])
