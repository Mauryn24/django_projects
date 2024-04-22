
# Smart Travel Companion

Smart Travel Companion is a web application built with Django that assists travelers in planning their trips efficiently by providing personalized recommendations and real-time information, including weather forecasts, location recommendations, and trip planning features.

## Features

- **Personalized Trip Planning:** Plan your trips based on your preferences, budget, and time constraints.
- **Real-Time Weather Integration:** Get up-to-date weather forecasts for your destination cities to help you pack appropriately and plan activities.
- **Local Recommendations:** Discover nearby attractions, restaurants, events, and accommodations with personalized recommendations.
- **Interactive Map:** Visualize your trip itinerary, explore points of interest, and navigate your destinations seamlessly.
- **Budget Tracker:** Manage expenses throughout your trip by setting budgets for different categories and receiving alerts when nearing or exceeding limits.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart-travel-companion.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the project root directory.
   - Add your API keys and other sensitive information to the `.env` file:

     ```plaintext
     OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
     ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Sign up for an account or log in if you already have one.
- Plan your trip by providing details such as destination, dates, and preferences.
- Explore personalized recommendations for activities, restaurants, and accommodations.
- Track your budget and receive alerts when nearing or exceeding limits.
- Check the weather forecast for your destination cities.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview)
- [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)

