#!/usr/bin/env python3
# This code...
# 1. Takes in a list of artists
# 2. Searches them on Google or a search engine or wikipedia
# 3. If search is successful, grabs their list of genres
# 4. Spit out genre stats

import sys

def main():
    # sys arg stuff here
    if len(sys.argv) < 1:
        print("No artist list given as argument")
    else:
        print(sys.argv)

if __name__== "__main__":
    main()

