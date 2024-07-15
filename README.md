# Smart Wardrobe Assistant

Welcome to the Smart Wardrobe Assistant! This project is an AI-powered outfit recommendation system designed to help users make daily fashion decisions based on various factors such as weather, personal style, past choices, and upcoming events.

## Features

- **Weather-based Recommendations**: Suggests outfits suitable for different weather conditions.
- **Style-based Recommendations**: Provides outfit options based on the user's personal style.
- **Event-based Recommendations**: Recommends outfits appropriate for upcoming events.
- **Sustainable Recommendations**: Encourages sustainable fashion choices by considering past outfit selections.

## How It Works

The Smart Wardrobe Assistant uses a combination of predefined wardrobe options and simulated functions to generate outfit recommendations. The main factors influencing the recommendations are:

- **Weather Conditions**: sunny, rainy, cloudy, snowy
- **Personal Styles**: casual, formal, sporty, chic
- **Upcoming Events**: meeting, workout, date night, casual outing
- **Past Choices**: previous outfits worn by the user

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. The code uses the `random` module, which is included in the Python Standard Library.

### Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/smart-wardrobe-assistant.git
    cd smart-wardrobe-assistant
    ```

2. **Run the script**:
    ```sh
    python smart_wardrobe_assistant.py
    ```

### Example

The script will simulate user inputs for weather, style, and event, and generate outfit recommendations accordingly. Here's an example of the output:

```plaintext
Smart Wardrobe Assistant Recommendations

Weather Condition: sunny
Personal Style: casual
Upcoming Event: casual outing

Recommendation based on Weather: shorts and tank top
Recommendation based on Personal Style: t-shirt and jeans
Recommendation based on Upcoming Event: sundress
Sustainable Recommendation (based on past choices): t-shirt and jeans

Final Outfit Recommendation: t-shirt and jeans (weather appropriate and event suitable)
```

## Code Explanation

The code consists of dummy data for weather conditions, personal styles, past choices, and upcoming events. It includes several functions to provide recommendations based on these factors:

- `get_weather_based_recommendation(weather)`: Returns an outfit suggestion based on the weather condition.
- `get_style_based_recommendation(style)`: Returns an outfit suggestion based on personal style.
- `get_event_based_recommendation(event)`: Returns an outfit suggestion based on the upcoming event.
- `get_sustainable_recommendation(past_choices)`: Returns a sustainable outfit choice based on past outfits.

The `generate_outfit_recommendation(weather, style, event)` function combines these recommendations and prints the final outfit suggestion.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.
