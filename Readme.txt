relevant URLS/API endpoints

Static contents URL:
- to view static HTML content: send a HTTP GET request to http://127.0.0.1:8000/restaurant/home

Menu API endpoints (user must be authenticated to access these endpoints):
- to view menu: send a HTTP GET request to http://127.0.0.1:8000/restaurant/menu
- to add new menu item: send a HTTP POST request to http://127.0.0.1:8000/restaurant/menu
- to view a specific menu item: send a HTTP GET request to http://127.0.0.1:8000/restaurant/menu/1 (change 1 to any other menu item ID to view other menu items)
- to edit a specific menu item: send a HTTP PUT or PATCH request to http://127.0.0.1:8000/restaurant/menu/1 (change 1 to any other menu item ID to edit other menu items)
- to delete a specific menu item: send a HTTP DELETE request to http://127.0.0.1:8000/restaurant/menu/1 (change 1 to any other menu item ID to delete other menu items)

Booking API endpoints (user must be authenticated to access these endpoints):
- to view all bookings: send a HTTP GET request to http://127.0.0.1:8000/restaurant/bookings
- to create a new booking: send a HTTP POST request to http://127.0.0.1:8000/restaurant/bookings/
- to view a specific booking: send a HTTP GET request to http://127.0.0.1:8000/restaurant/bookings/1 (change 1 to any other booking ID to view other bookings)
- to edit a specific booking: send a HTTP PUT or PATCH request to http://127.0.0.1:8000/restaurant/bookings/1 (change 1 to any other booking ID to edit other bookings)
- to delete a specific booking: send a HTTP DELETE request to http://127.0.0.1:8000/restaurant/bookings/1 (change 1 to any other booking ID to delete other bookings)

User registration / authentication:
- to view all users: send a HTTP GET request to http://127.0.0.1:8000/auth/users
- to register a new user: send a HTTP POST request to http://127.0.0.1:8000/auth/users/
- to generate token (i.e., login): send a HTTP POST request to http://127.0.0.1:8000/auth/token/login or http://127.0.0.1:8000/api-token-auth
- to delete token (i.e., logout): send a HTTP POST request to http://127.0.0.1:8000/auth/token/logout