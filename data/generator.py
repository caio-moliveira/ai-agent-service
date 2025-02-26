import csv
import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)


def generate_fake_netflix_data(num_records=10000):
    types = ["Movie", "TV Show"]
    ratings = [
        "G",
        "PG",
        "PG-13",
        "R",
        "NC-17",
        "TV-Y",
        "TV-Y7",
        "TV-G",
        "TV-PG",
        "TV-14",
        "TV-MA",
    ]
    genres = [
        "Drama",
        "Comedy",
        "Action",
        "Horror",
        "Romance",
        "Thriller",
        "Sci-Fi",
        "Documentary",
        "Fantasy",
    ]

    with open("netflix_fake_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "show_id",
                "type",
                "title",
                "director",
                "movie_cast",
                "country",
                "date_added",
                "release_year",
                "rating",
                "duration",
                "listed_in",
                "description",
            ]
        )

        for _ in range(num_records):
            show_id = fake.uuid4()
            type_ = random.choice(types)
            title = fake.sentence(nb_words=3).replace(".", "")
            director = (
                fake.name() if random.random() > 0.2 else ""
            )  # Some missing directors
            movie_cast = ", ".join(fake.name() for _ in range(random.randint(2, 5)))
            country = (
                fake.country() if random.random() > 0.1 else ""
            )  # Some missing country
            date_added = (
                fake.date_between(start_date="-5y", end_date="today")
                if random.random() > 0.2
                else ""
            )  # Some missing dates
            release_year = fake.year()
            rating = random.choice(ratings)
            duration = (
                f"{random.randint(1, 180)} min"
                if type_ == "Movie"
                else f"{random.randint(1, 10)} Season"
            )
            listed_in = ", ".join(random.sample(genres, k=random.randint(1, 3)))
            description = fake.text(max_nb_chars=200)

            writer.writerow(
                [
                    show_id,
                    type_,
                    title,
                    director,
                    movie_cast,
                    country,
                    date_added,
                    release_year,
                    rating,
                    duration,
                    listed_in,
                    description,
                ]
            )

    print("Fake Netflix dataset generated successfully: netflix_fake_data.csv")


if __name__ == "__main__":
    generate_fake_netflix_data()
