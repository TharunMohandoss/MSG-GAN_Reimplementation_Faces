from utils.config import process_config
from utils.dirs import create_dirs
from utils.utils import get_args
from configs.config import config
# from data_loader.DataGenerator import DataGenerator
# from models.simplemodel import Model
# from trainers.trainer import Trainer
import os

def main():
    try:
        args = get_args()
        mode = args.mode
    except:
        print("missing or invalid arguments")
        exit(0)


    print('Mode : ',mode)
    if mode == "TrainAndTest":
        print('Train and Test')


if __name__ == '__main__':
    main()