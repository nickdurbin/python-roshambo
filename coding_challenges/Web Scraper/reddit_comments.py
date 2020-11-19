# Build a command line tool that, given a subreddit,
# will print out the most common words in the comments of that subreddit
import csv
import random
import sys
from collections import Counter
​
import requests
​
HEADERS = {
  "user-agent": "glenna-script:cspt14-crawler:v0.0 (by /u/glennayu)"
}
​
​
def main():
  # User inputs subreddit as command line argument
  subreddit_name = sys.argv[1]
  print(subreddit_name)
​
  subreddit_url = f"https://www.reddit.com/r/{subreddit_name}/.json"
  print(subreddit_url)
​
  response = requests.get(subreddit_url, headers=HEADERS)
  js = response.json()
  children = js['data']['children']
​
  # choose a random post from that subreddit
  random_post = random.choice(children)
  post_url = random_post['data']['permalink']
  print(post_url)
​
  # get all comments for the post
  comments = get_comments_for_post(post_url)
​
  # parse the top 50
  comment_bodys = []
  for comment in comments[:50]:
    body = comment['data']['body']
    comment_bodys.append(body)
​
  # get list of common english stop words
  stop_words = set(load_stop_words())
​
  # Print out the most common words
  c = Counter()
​
  # we need to preprocess the comments to split out individual words
  for comment in comment_bodys:
    split_comment = comment.split()
    # remove words that appear in stop_words and convert to lower case
    filtered = [word.lower() for word in split_comment if word.lower() not in stop_words]
​
    # # ^ List comprehension is the same as doing the below:
    # filtered = []
    # for word in split_comment: O(n)
    #     if word not in stop_words: O(1)
    #         filtered.append(word) O(1)
​
    c.update(filtered)
​
  print(c.most_common(10))
  write_to_csv(c)
​
​
def get_comments_for_post(post_permalink):
  post_url = f"https://www.reddit.com{post_permalink}.json"
  response = requests.get(post_url, headers=HEADERS)
  js = response.json()
  comments = js[1]['data']['children']
  return comments
​
​
def load_stop_words():
  filename = "nltk_stopwords.txt"
  with open(filename, 'r') as f:
    stop_words = f.readlines()
  return [word.strip() for word in stop_words]
​
​
def write_to_csv(counter):
  columns = ["word", "count"]
  csv_filename = "word_counts.csv"
  with open(csv_filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, columns)
    writer.writeheader()
    for word, count in counter.most_common():
      writer.writerow({"word": word, "count": count})
​
​
if __name__ == "__main__":
  main()