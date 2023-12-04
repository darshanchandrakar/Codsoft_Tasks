class MovieRecommendationSystem:
    def __init__(self):
        self.movies = {
            'Inception': {'genre': 'Action', 'rating': 4.5},
            'The Dark Knight': {'genre': 'Action', 'rating': 4.0},
            'Interstellar': {'genre': 'Sci-Fi', 'rating': 4.8},
            'Pulp Fiction': {'genre': 'Crime', 'rating': 4.7},
            'Forrest Gump': {'genre': 'Drama', 'rating': 4.2}
        }
        self.user_preferences = {}

    def add_user_preference(self, user_id, movie_title, rating):
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}
        if movie_title not in self.movies:
            return f"{movie_title} is not in the database."
        self.user_preferences[user_id][movie_title] = rating

    def recommend_movies(self, user_id, top_n=2):
        user_preference = self.user_preferences.get(user_id, {})
        if not user_preference:
            return "No user preferences found. Please rate some movies."

        recommendations = {}
        for movie_title, movie_info in self.movies.items():
            if movie_title not in user_preference:
                genre = movie_info['genre']
                rating = movie_info['rating']
                if genre not in recommendations:
                    recommendations[genre] = []
                recommendations[genre].append((movie_title, rating))

        sorted_recommendations = {
            genre: sorted(movies, key=lambda x: x[1], reverse=True)[:top_n]
            for genre, movies in recommendations.items()
        }
        return sorted_recommendations

# Example usage:
recommendation_system = MovieRecommendationSystem()
# User preferences
recommendation_system.add_user_preference(user_id=1, movie_title='The Dark Knight', rating=4.0)
recommendation_system.add_user_preference(user_id=1, movie_title='Interstellar', rating=5.0)
# Recommend movies for the user
user_id = 1
recommendations = recommendation_system.recommend_movies(user_id=user_id, top_n=2)
print(f"Recommended movies for User {user_id}:")
for genre, movies in recommendations.items():
    for movie_title, rating in movies:
        print(f"Movie Title: {movie_title}, Genre: {genre}, User Rating: {rating}")



    
                
    