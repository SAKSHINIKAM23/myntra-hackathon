import random

# Dummy data for weather conditions, personal styles, past choices, and upcoming events
weather_conditions = ['sunny', 'rainy', 'cloudy', 'snowy']
personal_styles = ['casual', 'formal', 'sporty', 'chic']
wardrobe = {
    'casual': ['t-shirt and jeans', 'sundress', 'shorts and tank top'],
    'formal': ['suit', 'dress', 'blazer and slacks'],
    'sporty': ['tracksuit', 'yoga pants and top', 'running shorts and t-shirt'],
    'chic': ['blouse and skirt', 'stylish dress', 'fashionable top and pants']
}
past_choices = ['t-shirt and jeans', 'suit', 'tracksuit', 'blouse and skirt']
upcoming_events = ['meeting', 'workout', 'date night', 'casual outing']

# Simulated functions to provide recommendations based on different factors
def get_weather_based_recommendation(weather):
    if weather == 'sunny':
        return random.choice(['sundress', 'shorts and tank top'])
    elif weather == 'rainy':
        return random.choice(['raincoat and boots', 'waterproof jacket and jeans'])
    elif weather == 'cloudy':
        return random.choice(['long sleeve shirt and jeans', 'light sweater and pants'])
    elif weather == 'snowy':
        return random.choice(['winter coat and boots', 'sweater and warm pants'])

def get_style_based_recommendation(style):
    return random.choice(wardrobe[style])

def get_event_based_recommendation(event):
    if event == 'meeting':
        return random.choice(['suit', 'blazer and slacks'])
    elif event == 'workout':
        return random.choice(['tracksuit', 'yoga pants and top'])
    elif event == 'date night':
        return random.choice(['stylish dress', 'fashionable top and pants'])
    elif event == 'casual outing':
        return random.choice(['t-shirt and jeans', 'sundress'])

def get_sustainable_recommendation(past_choices):
    return random.choice(past_choices)

# Main function to generate outfit recommendation
def generate_outfit_recommendation(weather, style, event):
    print("Smart Wardrobe Assistant Recommendations\n")
    print(f"Weather Condition: {weather}")
    print(f"Personal Style: {style}")
    print(f"Upcoming Event: {event}\n")
    
    weather_based = get_weather_based_recommendation(weather)
    style_based = get_style_based_recommendation(style)
    event_based = get_event_based_recommendation(event)
    sustainable_choice = get_sustainable_recommendation(past_choices)
    
    print(f"Recommendation based on Weather: {weather_based}")
    print(f"Recommendation based on Personal Style: {style_based}")
    print(f"Recommendation based on Upcoming Event: {event_based}")
    print(f"Sustainable Recommendation (based on past choices): {sustainable_choice}\n")

    # Final recommendation logic (simplified)
    final_recommendation = f"{style_based} (weather appropriate and event suitable)"
    print(f"Final Outfit Recommendation: {final_recommendation}")

# Simulated user inputs
random_weather = random.choice(weather_conditions)
random_style = random.choice(personal_styles)
random_event = random.choice(upcoming_events)

# Generate and display the outfit recommendation
generate_outfit_recommendation(random_weather, random_style, random_event)
