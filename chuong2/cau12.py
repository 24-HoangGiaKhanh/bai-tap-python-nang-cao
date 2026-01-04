import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(API_URL)
    
    if response.status_code == 200: return response.json()  
    else:
        print("Không thể lấy dữ liệu từ API.")
        return []

def display_posts(posts):
    print(f"Tổng số bài post: {len(posts)}\n")
    print(f"{'userID':<8} {'id':<6} {'title':<30} {'body':<50}")
    print("-" * 100)

    for post in posts:
        user_id = post.get("userId")
        post_id = post.get("id")
        title = post.get("title")
        body = post.get("body")
        print(f"{user_id:<8} {post_id:<6} {title:<30} {body[:50]}...")

def main():
    posts = fetch_posts()
    
    if posts: display_posts(posts)

if __name__ == "__main__": main()