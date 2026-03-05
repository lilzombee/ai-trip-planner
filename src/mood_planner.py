def mood_based_travel_planner(mood):
    travel_destinations = {
        'happy': ['Bali', 'Hawaii', 'Maldives'],
        'sad': ['London', 'Iceland', 'Tokyo'],
        'adventurous': ['Bungee Jumping in New Zealand', 'Safari in Africa', 'Rock Climbing in Colorado'],
        'relaxed': ['Spa in Bali', 'Yoga retreat in India', 'Beach in Fiji'],
        'romantic': ['Paris', 'Venice', 'Santorini']
    }

    return travel_destinations.get(mood.lower(), 'No suggestions available for this mood.')

# Example usage:
if __name__ == '__main__':
    user_mood = input('Enter your mood: ')
    destinations = mood_based_travel_planner(user_mood)
    print(f'Travel suggestions for {user_mood} mood: {destinations}')