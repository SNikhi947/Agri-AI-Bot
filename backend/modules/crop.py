def get_crop_recommendation():
    # Mock Logic - In production, this uses ML models based on N-P-K values
    return [
        {"crop": "Wheat", "season": "Rabi", "soil": "Loamy"},
        {"crop": "Rice", "season": "Kharif", "soil": "Clayey"},
        {"crop": "Maize", "season": "All", "soil": "Well-drained"}
    ]