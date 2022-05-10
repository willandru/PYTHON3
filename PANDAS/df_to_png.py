import pandas as pd
import numpy as np
import dataframe_image as dfi
df = pd.DataFrame(np.random.randn(6, 6), columns=list(['a','2121', 'cas', 'dsasda', 'efre', 'fsad']))

#df_styled = df.style.background_gradient()
dfi.export(df,"mytable.png")