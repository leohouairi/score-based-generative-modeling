import pandas as pd
import torch
from torch.utils.data import Dataset

class HeroicDataset(Dataset):
    def __init__(self, parquet_file):
        """
        Args:
            parquet_file (string): Path to the parquet file with annotations.
        """
        super(TinyDalleDataset, self).__init__()
        self.data = pd.read_parquet(parquet_file)


    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        image_name=self.data.iloc[idx,0]
        caption = self.data.iloc[idx, 1]
        
        
        return [image_name], [caption]