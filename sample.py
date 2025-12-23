# Creating sample_reviews.json from yelp_academic_dataset_review.json
# import json
# import random

# INPUT_PATH = r"C:\Users\dev\OneDrive\Documents\Desktop\Fake Review Detection\yelp_academic_dataset_review.json"
# OUTPUT_PATH = "sample_reviews.json"
# SAMPLE_SIZE = 50000   # perfect for laptop

# with open(INPUT_PATH, "r", encoding="utf-8") as fin, \
#      open(OUTPUT_PATH, "w", encoding="utf-8") as fout:

#     for i, line in enumerate(fin):
#         if i >= SAMPLE_SIZE:
#             break
#         fout.write(line)

# print("Sample dataset created:", SAMPLE_SIZE)


#Creating reviews_clean.csv from sample_reviews.json
import json
import csv

# INPUT_PATH = r"C:\Users\dev\OneDrive\Documents\Desktop\Fake Review Detection\yelp_academic_dataset_review.json"
# OUTPUT_PATH = "reviews_clean.csv"
# MAX_REVIEWS = 50000   # laptop-friendly

# with open(INPUT_PATH, "r", encoding="utf-8") as fin, \
#      open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as fout:

#     writer = csv.writer(fout)
#     writer.writerow(["review_id", "stars", "text"])

#     for i, line in enumerate(fin):
#         if i >= MAX_REVIEWS:
#             break
#         review = json.loads(line)
#         writer.writerow([
#             review["review_id"],
#             review["stars"],
#             review["text"].replace("\n", " ")
#         ])

# print("CSV created successfully!")
