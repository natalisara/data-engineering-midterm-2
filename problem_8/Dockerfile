# ოფიციალური Python 3.12 ბეის იმიჯი
FROM python:3.12

# სამუშაო დირექტორიის შექმნა
WORKDIR /app

# კოდის ასლი Docker კონტეინერში
COPY . /app

# საჭირო პაკეტების ინსტალაცია
RUN pip install fastapi uvicorn

# 8000 პორტის გახსნა
EXPOSE 8000

# FastAPI აპლიკაციის გაშვება
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
