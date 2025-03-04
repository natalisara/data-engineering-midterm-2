# გამოიყენება ოფიციალური Python 3.12 იმიჯი
FROM python:3.12

# სამუშაო დირექტორიის შექმნა
WORKDIR /app

# საჭირო ფაილების კოპირება კონტეინერში
COPY requirements.txt .
COPY problem7.py .
COPY customer_data.csv .

# დამოკიდებულებების ინსტალაცია
RUN pip install --no-cache-dir -r requirements.txt

# Docker კონტეინერის გაშვების ბრძანება
CMD ["python", "problem7.py", "customer_data.csv", "customer_data_new.csv"]
