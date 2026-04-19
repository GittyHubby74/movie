from recommender import recommend

def main():
    print("🎬 Movie Recommendation System")
    print("Type 'exit' to quit\n")

    while True:
        movie = input("Enter a movie you like: ")

        if movie.lower() == 'exit':
            print("Goodbye 👋")
            break

        results = recommend(movie)

        print("\nRecommended movies:")
        for i, m in enumerate(results, start=1):
            print(f"{i}. {m}")

        print("\n" + "-"*30 + "\n")


if __name__ == "__main__":
    main()