import pandas as pd
import numpy as np
from functools import partial

def transform_data(data, column_mapping=None, date_format=None,
                   numeric_precision=2, missing_values='drop',
                   filters=None):
    """
    მთავარი ფუნქცია მონაცემთა ტრანსფორმაციისთვის
    """
    df = data.copy()

    # სვეტების სახელების გადარქმევა
    if column_mapping:
        df.rename(columns=column_mapping, inplace=True)

    # თარიღის ფორმატში გარდაქმნა
    if date_format:
        date_cols = df.select_dtypes(include=['object', 'datetime']).columns
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            if df[col].notna().any():
                df[col] = df[col].dt.strftime(date_format)

    # რიცხვების დამრგვალება
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].round(numeric_precision)

    # ცარიელი უჯრედების დამუშავება
    if missing_values == 'drop':
        df.dropna(inplace=True)
    elif missing_values == 'fill_zero':
        df.fillna(0, inplace=True)
    elif missing_values == 'fill_mean':
        mean_values = df[numeric_cols].mean()
        df.fillna(mean_values, inplace=True)

    # ფილტრაცია მითითებული პირობებით
    if filters:
        for col, value in filters.items():
            if col in df.columns:
                df = df[df[col] == value]

    return df

# სპეციალიზებული პროცესორების შექმნა `functools.partial()`-ის გამოყენებით
finance_processor = partial(transform_data,
                            column_mapping={'Revenue': 'Income', 'Expense': 'Cost'},
                            date_format='%Y-%m-%d',
                            numeric_precision=2,
                            missing_values='fill_zero')

marketing_processor = partial(transform_data,
                              column_mapping={'Clicks': 'UserClicks', 'Conversions': 'UserConversions'},
                              numeric_precision=0,
                              missing_values='drop',
                              filters={'AdType': 'Positive'})

scientific_processor = partial(transform_data,
                               numeric_precision=4,
                               missing_values='fill_mean',
                               date_format='%s')

def process_pipeline(data_source, source_type):
    """
    მონაცემთა კონვეიერი, რომელიც სხვადასხვა ტიპის მონაცემების დასამუშავებლად
    """
    processors = {
        'finance': finance_processor,
        'marketing': marketing_processor,
        'scientific': scientific_processor
    }

    if source_type in processors:
        return processors[source_type](data_source)
    else:
        raise ValueError("Invalid source type. Choose from: finance, marketing, scientific")


if __name__ == "__main__":
    data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
        'Revenue': [1000.567, 2000.789, np.nan],
        'Expense': [500.256, np.nan, 300.456],
        'Clicks': [120, 350, 500],
        'Conversions': [4, 10, 15],
        'AdType': ['Positive', 'Negative', 'Positive']
    })

    print("Input Data:\n", data)

    finance_result = process_pipeline(data, 'finance')
    print("\n Finance Data Processed:\n", finance_result)

    marketing_result = process_pipeline(data, 'marketing')
    print("\n Marketing Data Processed:\n", marketing_result)

    scientific_result = process_pipeline(data, 'scientific')
    print("\n Scientific Data Processed:\n", scientific_result)
