# Tools for pickle operation

import pickle
from datetime import datetime

now = datetime.now().strftime('%Y%m%d_%H%M%S')

def save_pickle(obj, filepath: str = f'../models/pickle_{now}.pkl'):
    """
    指定したオブジェクトobjをfilepathでpickleとして保存する
    """
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)

def load_pickle(filepath):
    """
    指定したfilepathからpickleデータをロードして返す
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)
