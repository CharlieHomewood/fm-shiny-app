import os
import pandas as pd
import janitor

def load_data(data_file: str) -> pd.DataFrame:
    """
    This is a summary
    
    Args:
        data_file (str): this is a description
    """
    
    if data_file.endswith(".html"):
        df = pd.read_html(data_file, encoding="utf-8").clean_names(strip_underscores=True, strip_whitespace=True)
        
    return df