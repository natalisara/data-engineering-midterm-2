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
    მონაცემთა კონვეიერი, რომელიც სხვადასხვა ტიპის მონაცემებს ამუშავებს
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
    # CSV ფაილიდან მონაცემების წაკითხვა
    input_file = "data.csv"
    output_files = {
        'finance': "processed_finance.csv",
        'marketing': "processed_marketing.csv",
        'scientific': "processed_scientific.csv"
    }

    try:
        data = pd.read_csv(input_file)
        print(" Input Data Loaded from CSV:\n", data)
    except FileNotFoundError:
        print(f" Error: {input_file} not found. Please make sure the file exists.")
        exit(1)

    # თითოეული მონაცემის დამუშავება და შენახვა CSV-ში
    for category in ['finance', 'marketing', 'scientific']:
        processed_data = process_pipeline(data, category)
        print(f"\n {category.capitalize()} Data Processed:\n", processed_data)

        # დამუშავებული მონაცემების შენახვა CSV ფაილში
        processed_data.to_csv(output_files[category], index=False)
        print(f" {category.capitalize()} Data Saved to {output_files[category]}")
