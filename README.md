# Liquorboxd

Letterboxd, but for spirits. Track, rate, and review whiskey, vodka, rum, tequila, gin, and more.

This is a personal learning project built to strengthen my full-stack development skills — from data modeling and backend logic to authentication, testing, and deployment.

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development) → PostgreSQL (planned)
- **Frontend:** Django templates (server-rendered)
- **Planned additions:** Django REST Framework, Docker, GitHub Actions CI/CD

## Features

### Implemented
- Spirit model with category (whiskey, vodka, rum, tequila, gin)
- Django admin integration for managing spirits

### Planned (MVP)
- User registration, login, logout
- Browse/search spirits
- Rate and review spirits (1–5 stars, optional written review)
- Personal log of spirits tried
- User profile page

### Future Ideas
- Follows/followers
- Activity feed
- Custom lists
- Personal stats and rating distributions
- REST API
- Deployment via Docker + PostgreSQL

## Why This Project

I'm building Liquorboxd as a hands-on way to learn backend development, database design, and full-stack Python — while working toward a portfolio project I can discuss in technical interviews. All code is written by me; I use AI tooling as a mentor for explanations and code review, not as a code generator.

## Development Status

🚧 Actively in development — MVP in progress.

## Setup (Local Development)

```bash
git clone https://github.com/marioesc425/Liquorboxd.git
cd Liquorboxd
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## License

MIT