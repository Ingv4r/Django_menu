FROM python:3.12-slim
WORKDIR /menu_app
COPY . .
RUN chmod +x start.sh
CMD ["./start.sh", "gunicorn tree_menu.wsgi:application --bind 0.0.0.0:8080"]