#!/bin/python3
import os.path
import shutil

from src.logo_gen import GenerateLogoImg
from src.logo_gen_decoder import process_splashimg

menu_text = """
        [Xiaomi/Redmi Splash Image Maker]
  Author：ColdWindScholar
  Link: github.com/ColdWindScholar/splashmaker
  Thanks：Gokul NC @ XDA-Developers | affggh@github
  [1] Unpack splash.img
  [2] Generate splash.img
  [x] Exit
-->
"""


def unpack(filepath: str):
    if not os.path.exists(filepath):
        print(f"File {filepath} cannot access!")
    else:
        process_splashimg(filepath, "pic/splash.png")


def repack(nolimit=False):
    print("Using predefined DataSize to generate splash...")
    n = 1
    output_dir = 'output'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    print("Generate 1024 byte of empty file...")
    with open(f"{output_dir}/splash.img", "wb") as f:
        f.write(b'\x00' * 1024)
    for i in [100864, 613888, 101888, 204288, 204288, 0]:
        if nolimit:
            i = 0
        print(f"Compress ./pic/splash{n}.png padding into {output_dir}/splash.img...")
        data = GenerateLogoImg(f"./pic/splash{n}.png", i)
        a = len(data)
        b = a + 512
        print(f"Data size: {a}\nPredefined:{i}")
        if i != 0:
            if a > b:
                print(f"Error of picture [pic/splash{n}.png]... Image is too complex...")
                print("Please replace it with a more sample picture...")
                return
        with open(f"{output_dir}/splash.img", "ab") as f:
            f.write(data)
        n += 1
    print("Done...")


def main():
    choice = input(menu_text)
    if choice == '1':
        filepath = input('Please type your file here:')
        print("\033[32m Function : unpack...\n\033[0m")
        unpack(filepath)
    elif choice == '2':
        repack(input("No PayloadLimit?[1/0]") == '1')
    elif choice == 'x':
        exit(0)
    else:
        input('Invalid choice')


if __name__ == '__main__':
    while True:
        main()
