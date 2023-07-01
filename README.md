# Django Blog Project

This is a basic Django blog project that includes a blog app and an accounts app for user authentication. The project is designed to showcase the functionality of a simple blogging platform.

## Features

- User registration and authentication
- User login and logout
- Create, update, and delete blog posts
- View blog posts
- Comment on blog posts
- User profile page
- User dashboard with post management

## Requirements

- Python 3.7 or higher
- Django 3.2 or higher

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/blog-app.git
   ```

2. Navigate to the project directory:

   ```shell
   cd blog-app
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows:**

     ```shell
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```shell
     source venv/bin/activate
     ```

5. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

7. Create a superuser (admin account):

   ```shell
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```shell
   python manage.py runserver
   ```

9. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

- To create a new blog post, you need to log in or register for an account.
- After logging in, you will be redirected to the dashboard where you can manage your posts.
- On the dashboard, you can create new posts, edit existing posts, or delete posts.
- The home page displays all the published blog posts, along with their titles, authors, and publication dates.
- You can click on a blog post to view its details and comments.
- To comment on a blog post, you need to be logged in.
- You can also view and edit your profile by clicking on the "Profile" link in the navigation bar.

## Folder Structure

The project has the following folder structure:

```
├── blog
│   ├── migrations
│   ├── static
│   ├── templates
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── accounts
│   ├── migrations
│   ├── templates
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   └── css
│       └── styles.css
├── templates
│   ├── base.html
│   ├── home.html
│   ├── post_detail.html
│   ├── post_form.html
│   ├── profile.html
│   ├── registration
│   │   ├── login.html
│   │   └── register.html
│   
├── manage.py
└── README.md
```

- The `blog` app contains the models, views, forms, and templates related to the blog functionality.
- The `accounts` app handles user authentication

, including registration, login, logout, and profile management.
- The `config` folder contains the project settings and URL configurations.
- The `static` folder includes static files such as CSS stylesheets.
- The `templates` folder contains HTML templates used by the project.

## Contributing

Contributions to the project are welcome. If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE)
