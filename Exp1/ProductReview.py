from collections import defaultdict
import os

directory = os.path.dirname(__file__)

files = [f for f in os.listdir(directory) if f.endswith('.txt')]

reviews = []
for file in files:
    with open(file, 'r') as f:
        content = f.read().split('\n\n') 
        for block in content:
            review_data = {}
            for line in block.split('\n'):
                if ': ' in line:
                    key, value = line.split(': ')
                    review_data[key] = value
            reviews.append(review_data)

valid_reviews = []
invalid_reviews = []

for review in reviews:
    if {'CustomerID', 'ProductID', 'ReviewDate', 'ReviewRating', 'ReviewText'}.issubset(review.keys()):
        review_rating = review['ReviewRating']
        if review_rating.isdigit() and 1 <= int(review_rating) <= 5:
            valid_reviews.append(review)
        else:
            invalid_reviews.append(review)
    else:
        invalid_reviews.append(review)

product_ratings = defaultdict(list)

for review in valid_reviews:
    product_id = review['ProductID']
    review_rating = int(review['ReviewRating'])
    product_ratings[product_id].append(review_rating)

average_ratings = {product_id: sum(ratings) / len(ratings) for product_id, ratings in product_ratings.items()}

top_products = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)[:3]

total_reviews = len(reviews)
valid_review_count = len(valid_reviews)
invalid_review_count = len(invalid_reviews)

summary_path = os.path.join(directory, 'summary.txt')
with open(summary_path, 'w') as f:
    f.write(f'Total reviews processed: {total_reviews}\n')
    f.write(f'Total valid reviews: {valid_review_count}\n')
    f.write(f'Total invalid reviews: {invalid_review_count}\n')
    f.write('Top 3 products with highest average ratings:\n')
    for product_id, avg_rating in top_products:
        f.write(f'{product_id}: {avg_rating:.2f}\n')
