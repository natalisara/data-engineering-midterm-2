# CSV დამუშავების Docker აპლიკაცია

ეს პროექტი წარმოადგენს Python აპლიკაციას, რომელიც ფილტრავს მონაცემებს `customer_data.csv`-დან და ინახავს ახალ ფაილში `customer_data_new.csv`.

## ინსტრუქცია Docker-ის გამოყენებისთვის

### 1. Docker Image-ის შექმნა
Docker image-ის შესაქმნელად გაუშვით:
```bash
docker build -t csv_processor .
