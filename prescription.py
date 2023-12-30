from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the form to input prescription details
    return render_template('index.html')

@app.route('/generate_prescription', methods=['POST'])
def generate_prescription():
    # Collect prescription details from the form
    patient_name = request.form.get('patient_name', 'Unknown')  # Default to 'Unknown' if not provided
    age = request.form.get('age', 'N/A')
    sex = request.form.get('sex', 'N/A')
    diagnosis = request.form.get('diagnosis', 'N/A')
    medication_details = request.form.get('medication_details', 'N/A')
    medication_quantity = request.form.get('medication_quantity', 'N/A')
    refills = request.form.get('refills', '0')  # Default to 0 refills if not provided

    # Get the current date in a readable format, e.g., "December 30, 2023"
    current_date = datetime.now().strftime("%B %d, %Y")

    # Static college ID for the prescription
    college_id = "52937"

    # Render the prescription page with the details
    return render_template('prescription.html',
                           patient_name=patient_name,
                           age=age,
                           sex=sex,
                           diagnosis=diagnosis,
                           medication_details=medication_details,
                           medication_quantity=medication_quantity,
                           refills=refills,
                           current_date=current_date,
                           college_id=college_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Specify the port if the default is in use
