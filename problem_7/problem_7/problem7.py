import pandas as pd

def process_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        filtered_df = df[df['age'] > 30]
        filtered_df.to_csv(output_file, index=False)
        print(f"მონაცემები გაიფილტრა (age > 30) და შეინახა: {output_file}")
    except Exception as e:
        print(f"შეცდომა: {e}")

if __name__ == "__main__":
    input_file = "customer_data.csv"
    output_file = "customer_data_new.csv"

    process_data(input_file, output_file)
