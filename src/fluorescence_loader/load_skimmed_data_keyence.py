import nd2
import numpy as np

file_path = "/Users/tanmay/LenevoINFN/Work/BratatiImageJ/InFile/nd005.nd2"

with nd2.ND2File(file_path) as f:
    print("Sizes:", f.sizes)   # IMPORTANT
    data = f.asarray()
    #print("sizes: ", f.sizes)
    print("Has timestamps:", hasattr(f, "timestamps"))
    print("Events type:", type(f.events))
    print("Dir:", [x for x in dir(f) if "time" in x.lower()])
print("Shape:", data.shape)
