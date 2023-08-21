class NewsFeed:
    def __init__(self):
        self.articles = []

    def add_article(self, title, content):
        self.articles.append({"title": title, "content": content})

    def display_feed(self):
        for idx, article in enumerate(self.articles, start=1):
            print(f"Article {idx}: {article['title']}")
            print(article['content'])
            print("=" * 40)


def main():
    news_feed = NewsFeed()

    while True:
        print("1. Add Article")
        print("2. Display News Feed")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            news_feed.add_article(title, content)
            print("Article added successfully!")

        elif choice == '2':
            news_feed.display_feed()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
