  GNU nano 8.2                                                                                     problem_7/run.sh                                                                                     Modified
!/bin/bash

# Docker image-ის შექმნა
docker build -t csv_processor .

# კონტეინერის გაშვება
docker run --rm -v "$(pwd)":/app csv_processor
