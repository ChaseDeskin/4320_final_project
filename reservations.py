from flask import Flask, render_template, request

app = Flask(__name__)

# Constants
MAX_ROWS = 12
MAX_COLS = 4
reservations = []

@app.route('/')
def reserve_seat():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        row = int(request.form['row'])
        column = int(request.form['column'])

        if is_seat_available(row, column):
            e_ticket = generate_code(first_name)
            reservations.append({
                'first_name': first_name,
                'last_name': last_name,
                'row': row,
                'column': column,
                'e_ticket': e_ticket
            })
            save_reservation_to_file(first_name, last_name, row, column, e_ticket)
            return f"Seat reserved! Your e-ticket number is: {e_ticket}"
        else:
            return "Sorry, the seat is already taken."

    return render_template('reserve_seat.html', rows=MAX_ROWS, cols=MAX_COLS)

def is_seat_available(row, column):
    # Check if the seat is available for reservation
    # Implement logic here to check against existing reservations
    return True  # Placeholder logic

def save_reservation_to_file(first_name, last_name, row, column, e_ticket):
    # Save reservation information to a file
    with open('reservation.txt', 'a') as file:
        file.write(f"{first_name},{last_name},{row},{column},{e_ticket}\n")

def generate_code(first_name):
    # Generate a code for e-ticket number
    return f"{first_name[:3]}-XXXX"  # Placeholder code generation

if __name__ == '__main__':
    app.run(debug=True)
