#Hack NASA by DDOS
import requests
import json
import sys
import os
import time
import random
import string
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Hack NASA")
    parser.add_argument("-t", "--target", help="Target URL", required=True)
    parser.add_argument("-s", "--sleep", help="Sleep time", required=False)
    parser.add_argument("-c", "--count", help="Count", required=False)
    parser.add_argument("-f", "--file", help="File", required=False)
    args = parser.parse_args()
    return args



