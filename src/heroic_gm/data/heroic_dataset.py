import pandas as pd
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from PIL import Image
from io import BytesIO

class HeroicDataset(Dataset):
    def __init__(self, parquet_file):
        """
        Args:
            parquet_file (string): Path to the parquet file with annotations.
        """
        super(HeroicDataset, self).__init__()
        self.data = pd.read_parquet(parquet_file)
        self.transform = transforms.Compose([
            transforms.PILToTensor()
        ])
        self.data['image_tensor']=self.data['image'].apply(lambda x : self.transform(Image.open(BytesIO(x['bytes']))))
        self.data=self.data[['text','image_tensor']]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        image=self.data.iloc[idx,1]
        caption = self.data.iloc[idx, 0]
        return [caption], [image]