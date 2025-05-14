from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    business_type = request.args.get('type', 'Retail')
    location = request.args.get('location', 'Urban')
    doc_type = request.args.get('doc_type', 'ID Proof')
    zone = request.args.get('zone', 'Commercial')

    # Permit Recommendation
    if business_type.lower() == 'restaurant':
        permits = ['Food Safety License', 'Health Permit', 'Fire Safety']
    elif business_type.lower() == 'retail':
        permits = ['Trade License', 'Fire Safety']
    else:
        permits = ['General Business License']

    # Document Verification
    if doc_type.lower() == 'id proof':
        doc_status = 'Valid'
    else:
        doc_status = 'Needs manual check'

    # Zoning Rules
    rules = {
        'Commercial': 'Allows retail, restaurant, and office spaces.',
        'Residential': 'Allows housing but not businesses.',
        'Mixed-Use': 'Allows both residential and commercial use.'
    }

    zoning_rule = rules.get(zone, 'No data available')

    return f"""
    <h1>Urban Planning and Design Portal</h1>
    <h2>Permit Recommendations</h2>
    <p>Business Type: {business_type}</p>
    <p>Location: {location}</p>
    <p>Recommended Permits: {', '.join(permits)}</p>

    <h2>Document Verification</h2>
    <p>Document Type: {doc_type}</p>
    <p>Status: {doc_status}</p>

    <h2>Zoning Rules</h2>
    <p>Zone: {zone}</p>
    <p>Regulations: {zoning_rule}</p>

    <h2>Admin Section</h2>
    <p>This is a placeholder for the admin dashboard.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
