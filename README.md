# django-cart App

## Overview
This Django application provides a simple shopping cart functionality where users can view products, add them to their cart, and remove items from the cart. It utilizes Django's ORM for data modeling and provides basic views for managing the cart.

## Features
- List all products available for purchase.
- Add products to the shopping cart.
- Remove products from the shopping cart.
- Calculate and display the total price of items in the cart.

## Installation
1. Clone the repository:
    - `git clone https://github.com/alex-njuguna/django-cart.git`

2. Create a virtual environment and activate it:
    - `python -m venv env`
    - `source env/bin/activate # On Windows use env\Scripts\activate`

3. Install dependencies:
    - `pip install -r requirements.txt`

4. Apply migrations to set up the database:
    - `python manage.py makemigratons`
    - `python manage.py migrate`

5. Create a superuser to access the Django admin interface:
    - `python manage.py createsuperuser`

6. Start the development server:
    - `python manage.py runserver`


## Usage
1. Access the application by navigating to `http://localhost:8000/`.
2. Browse through the list of products available.
3. Click on a product to view details and add it to your cart.
4. Navigate to the cart page (`/cart/`) to view all items currently in your cart and the total price.
5. Remove items from the cart by clicking the 'Remove' button next to each item.
6. Continue shopping.

## Technologies Used
- Django: Web framework for rapid development and clean design.
- SQLite: Default database engine used by Django for local development.
- CSS: styling 
- HTML

## Project Structure
- `django-cart -> ecommerce/`: Main Django application directory.
- `cart -> models.py`: Defines `Product` and `CartItem` models.
- `cart -> views.py`: Contains view functions for rendering templates and handling user requests.
- `urls.py`: URL configuration for mapping views to URLs.
- `templates/`: HTML templates for rendering pages.
- `static/`: Contains static files like CSS, JavaScript, and images.

## Credits
This project was created by Alex Njuguna Kinuthia as a demonstration of Django development skills.

## License
This project is licensed under the MIT License - see the LICENSE file for details.





