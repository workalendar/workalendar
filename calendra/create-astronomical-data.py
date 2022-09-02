from tqdm import tqdm

from .precomputed_astronomy import create_astronomical_data

if __name__ == '__main__':
    create_astronomical_data(tqdm)
