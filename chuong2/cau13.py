import requests

API_URL = "https://jsonplaceholder.typicode.com/comments?postId=1"

def fetch_comments():
    response = requests.get(API_URL)
    
    if response.status_code == 200: return response.json()  
    else:
        print("Không thể lấy dữ liệu từ API.")
        return []

def display_comments(comments):
    print(f"Tổng số bài post: {len(comments)}\n")
    print(f"{'postId':<8} {'id':<6} {'name':<30} {'email':<30} {'body':<50}")
    print("-" * 120)

    for comment in comments[:3]:
        post_id = comment.get("postId")
        comment_id = comment.get("id")
        name = comment.get("name")
        email = comment.get("email")
        body = comment.get("body")
        print(f"{post_id:<8} {comment_id:<6} {name:<30} {email:<30} {body[:50]}...")

def main():
    comments = fetch_comments()
    if comments: display_comments(comments)

if __name__ == "__main__": main()