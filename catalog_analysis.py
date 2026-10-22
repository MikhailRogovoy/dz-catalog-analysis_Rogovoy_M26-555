import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies) -> float:
    ratings = []
    for movie in movies:
        ratings.append(movie["rating"])
    avg_rating = round(sum(ratings) / len(ratings), 1)
    return avg_rating


def catalog_age_stats(movies, current_year=2026) -> tuple[int, int, int]:
    ages = []
    for movie in movies:
        ages.append(current_year - movie["year"])
    min_age = min(ages)
    max_age = max(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (min_age, max_age, avg_age)


def duration_in_hours(minutes) -> str:
    return f"{minutes // 60}ч {minutes % 60}мин"


def rating_tier(rating: float) -> str:
    if rating >= 7:
        return 'Шедевр' if rating >= 9 else 'Хорошо'
    elif 5 <= rating < 7:
        return 'Средне'
    else:
        return 'Слабо'    


def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015 and year <= 2020:
            return "недавние"
        case _:
            return "старые"

print('Названия всех фильмов, которые НЕ относятся к жанру "comedy":')
for movie in movies:
    if movie['genres'].issuperset({'comedy'}):
        continue
    print(f'- {movie['title']}')

index = 0
while index < len(movies) - 1:    
    if movies[index]['rating'] > 9.0:
        print('Первый по порядку в списке фильм с рейтингом выше 9.0:', end = ' ')
        print(f'{movies[index]['title']}')
        break
    index += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1

    return count


def normalize_title(title):
    title = title.strip()
    if len(title) == 0:
        return ''
    words = title.split(' ')
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:])
    return ' '.join(new_words)


def make_slug(title):
    title = title.strip()
    if len(title) == 0:
        return ''
    words = title.split(' ')
    new_words = []
    for word in words:
        new_words.append(word[0].lower() + word[1:])
    return '-'.join(new_words)

def format_report_line(movie):
    m_title = movie['title']
    m_year = movie['year']
    m_rating = movie['rating']
    m_dur = duration_in_hours(movie['duration_min'])
    m_genres = ', '.join([genre for genre in sorted(movie['genres'])])
    return f'"{m_title}" ({m_year}) - {m_rating}/10, {m_dur}, жанры: {m_genres}'


def titles_sorted_by_rating(movies):
    new_movies = movies.copy()
    sorted_movies = sorted(new_movies, key=lambda movie: movie['rating'], reverse=True)
    result = []
    for m in sorted_movies:
        result.append((m['title'], m['rating']))
    return result

def top_n_by_rating(movies, n=3):
    return titles_sorted_by_rating(movies)[:n]


def count_by_genre(movies):
    genres_count = {}
    for movie in movies:
        movie_genres = list(movie['genres'])
        for genre in movie_genres:
            if genres_count.get(genre, 0) == 0:
                 genres_count[genre] = 1
            else:
                genres_count[genre] += 1

    return genres_count


def actor_filmography(movies):
    actor_movies = {}
    for movie in movies:
        actors = movie['actors']
        for actor in actors:
            if actor_movies.get(actor, 0) == 0:
                actor_movies[actor] = [movie['title']]
            else:
                actor_movies[actor].append(movie['title'])

    return actor_movies


def above_average_films(movies):
    avg_rat = average_rating(movies)
    result = {m["title"]: m['rating'] for m in movies if movie['rating'] > avg_rat}
    return result


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie['genres']

    return genres


def common_actors(movie1, movie2):
    return set(movie1['actors']) & set(movie2['actors'])


def genres_only_in_one(movies_a, movies_b):
    movies_a_genres = set()
    movies_b_genres = set()
    for movie_from_a in movies_a:
        movies_a_genres = movies_a_genres | movie_from_a['genres']
    for movie_from_b in movies_b:
        movies_b_genres = movies_b_genres | movie_from_b['genres']
    return movies_a_genres - movies_b_genres

print(genres_only_in_one(movies[5:6], movies[:3]))