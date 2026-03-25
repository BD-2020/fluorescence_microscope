import nd2
import numpy as np

file_path = "your_file.nd2"

with nd2.ND2File(file_path) as f:
    print("Sizes:", f.sizes)   # IMPORTANT
    data = f.asarray()

print("Shape:", data.shape)
