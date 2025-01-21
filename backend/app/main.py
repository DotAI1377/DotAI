from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Run the application on the specified host and port
    app.run(host="0.0.0.0", port=5000, debug=True)
