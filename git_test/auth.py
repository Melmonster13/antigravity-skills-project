def login():
    pass

def login_with_google(token):
    """
    Verifies the Google ID token and returns user information.
    """
    if not token:
        return {"error": "Invalid token"}
        
    # Simulate token verification and user profile retrieval
    return {
        "status": "success",
        "user": {
            "email": "user@example.com",
            "name": "Google User",
            "id": "google-user-id-123"
        }
    }
