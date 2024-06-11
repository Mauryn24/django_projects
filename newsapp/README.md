# News API App

## Overview

This Django application, `newsapp`, leverages the NewsAPI to display top headlines from various countries and categories. Users can search for news by country or category through the web interface.

## Project Structure

The project has the following structure:

```
newsapp/
    manage.py
    newsapp/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    news_api/
        __init__.py
        views.py
        templates/
            news_api/
                home.html
```

## Requirements

- Python 3.x
- Django 3.x or higher
- Requests library

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/newsapp.git
   cd newsapp
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install django requests
   ```

4. **Set Up the Database**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**

   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Configuration

The application uses an API key from NewsAPI to fetch news articles. Update the API key in `news_api/views.py`.

```python
API_KEY = 'your_newsapi_key_here'
```

## Application Details

### Views

- **Home View (`news_api/views.py`):**

  This view handles requests for displaying news articles. It checks for `country` and `category` parameters in the request, constructs the appropriate URL, fetches data from NewsAPI, and renders the `home.html` template with the retrieved articles.

  ```python
  from django.shortcuts import render
  import requests

  API_KEY = 'your_newsapi_key_here'

  def home(request):
      country = request.GET.get('country')
      category = request.GET.get('category')

      if country:
          url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
      else:
          url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'

      response = requests.get(url)
      data = response.json()
      articles = data.get('articles', [])

      context = {
          'articles': articles
      }

      return render(request, 'news_api/home.html', context)
  ```

### Templates

- **Home Template (`news_api/templates/news_api/home.html`):**

  This template displays a form for searching news by country or category, and a list of news articles. Each article includes an image, title, author, source, description, publication date, and a link to the full article.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet">
      <title>News APP</title>
  </head>
  <body>
      <h1 class="text-center">News App</h1>

      <h2>Search Country</h2>
      <form action="" method="get">
          <input type="text" name="country">
          <button type="submit">Search</button>
      </form>
      <br>

      <h2>Search Category</h2>
      <form action="" method="get">
          <input type="text" name="category">
          <button type="submit">Search</button>
      </form>

      <div class="container">
          <div class="row">
              <div class="col-md-8">
                  {% for i in articles %}
                      <div class="card rounded shadow-lg m-2" style="width: 25rem;">
                          <img src="{{ i.urlToImage }}" class="card-img-top" alt="...">
                          <div class="card-body">
                              <p class="card-text">{{ i.author }}</p>
                              <h5 class="card-title">{{ i.title }}</h5>
                              <p class="card-title">{{ i.source.name }}</p>
                              <p class="card-text">{{ i.description }}</p>
                              <hr>
                              <small>date: {{ i.publishedAt }}</small>
                              <a href="{{ i.url }}" target="_blank" class="btn btn-success m-1">See News</a>
                          </div>
                      </div>
                  {% endfor %}
              </div>
              <div class="col-md-4">
                  <h3><b>Category</b></h3>
                  <hr>
                  <br>
                  <ul class="list-group">
                      <li class="list-group-item"><a class="btn btn-secondary" href="?category=technology">Technology</a></li>
                      <li class="list-group-item"><a class="btn btn-success" href="?category=health">Health</a></li>
                      <li class="list-group-item"><a class="btn btn-danger" href="?category=Entertainment">Entertainment</a></li>
                      <li class="list-group-item"><a class="btn btn-secondary" href="?category=Sports">Sports</a></li>
                      <li class="list-group-item"><a class="btn btn-primary" href="?category=Science">Science</a></li>
                      <li class="list-group-item"><a class="btn btn-info" href="?category=Business">Business</a></li>
                  </ul>
              </div>
          </div>
      </div>
  </body>
  </html>
  ```

## API Documentation

This application uses the NewsAPI to fetch news articles. The main endpoint used is `/v2/top-headlines`, which requires an API key.

### Request Parameters

- `apiKey` (string, required): Your API key.
- `country` (string, optional): The country you want to get headlines for. Use ISO 3166-1 alpha-2 country codes (e.g., 'us' for the United States, 'gb' for the United Kingdom, 'in' for India).
- `category`  (string, optional): The category you want to get headlines for. Possible categories include 'business', 'entertainment', 'general', 'health', 'science', 'sports', and 'technology'.

### Example Request

```sh
GET https://newsapi.org/v2/top-headlines?country=us&apiKey=your_newsapi_key_here
```

### Response

The response contains a list of articles with details like title, description, author, source, and publication date.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or questions, feel free to reach out to [maurynnyakio19@gmail.com](mailto:maurynnyakio19@gmail.com).