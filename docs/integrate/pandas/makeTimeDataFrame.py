def makeTimeDataFrame(rows=5_000, freq = "B"):
    import numpy as np
    import pandas as pd
    return pd.DataFrame(
        np.random.default_rng(2).standard_normal((rows, 4)),
        columns=pd.Index(list("ABCD"), dtype=object),
        index=pd.date_range("2000-01-01", periods=rows, freq=freq),
    )
