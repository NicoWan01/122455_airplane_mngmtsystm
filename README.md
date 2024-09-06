# 122455_airplane_mngmtsystm# Airline Booking System

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Models

### Flight
- `flight_number`: CharField, unique identifier for the flight.
- `departure`: DateTimeField, the date and time of departure.
- `arrival`: DateTimeField, the date and time of arrival.
- `origin`: CharField, the origin airport.
- `destination`: CharField, the destination airport.
- `capacity`: IntegerField, the total number of seats available on the flight.

### Passenger
- `first_name`: CharField, the first name of the passenger.
- `last_name`: CharField, the last name of the passenger.
- `email`: EmailField, unique email address of the passenger.
- `phone_number`: CharField, contact number of the passenger.
- `flight`: ForeignKey to Flight, relates the passenger to a specific flight.

## Serializers

### FlightSerializer
- Serializes all fields of the Flight model.

### PassengerSerializer
- Serializes all fields of the Passenger model, including the related flight details.

## Views/ViewSets

### FlightViewSet
- Provides CRUD operations for Flight model.
- Supports filtering by `origin` and `destination`.
- Supports searching by `flight_number`.
- Supports ordering by `departure` and `arrival`.

### PassengerViewSet
- Provides CRUD operations for Passenger model.
- Supports filtering by `flight`.
- Supports searching by `first_name`, `last_name`, and `email`.
- Supports ordering by `first_name` and `last_name`.

## Notable Design Decisions
- Used Django Rest Framework for building the API.
- Implemented filtering, searching, and ordering for better data retrieval.
- Added pagination to handle large datasets efficiently.
