# Django Real Estate Web App
Implementation of a real estate website using the Django framework from the [Python Django Dev To Deployment](https://www.udemy.com/course/python-django-dev-to-deployment) Udemy course.

Deployed to Digital Ocean using Gunicorn and Nginx. Viewable online at [real-estate.davidwin.ch](real-estate.davidwin.ch).

Features a personalised admin area for creating/modifying listings, realtors, and accounts and authentication.

Users can enquire about a property and choose to create an account to keep track of messages within the site.

Backend database uses Postgres.

## Features

- Mobile friendly
- Responsive Bootstrap frontend
- Postgres database
- Display listings (using pagination)
- Listing details including up to 5 images with zoom/lightbox functionality
- Search listings using keywords, details, and location
- User roles
- Registration/Log in for customers
- Customers can enquire about a property from the listing page.
  This sends an email to the respective realtor and adds the enquiry to the admin area.
- Allow 'Seller of the Month' badge for a realtor

**PAGES**
- Home
- All Listings (paginated)
- View Single Listing
- Search
- Login/Register
- Dashboard
- About