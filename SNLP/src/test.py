from datetime import datetime
import pandas as pd
import numpy as np
import json

utc_time = datetime.strptime("2015-01-01", "%Y-%m-%d")
epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
print (epoch_time)