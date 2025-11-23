# MVP Rule-based Logic
def analyze_pest_image(filename: str):
    filename = filename.lower()
    
    if "rust" in filename:
        return {
            "disease": "Wheat Rust",
            "confidence": "98%",
            "treatment": "Apply fungicides like Tebuconazole. Rotate crops.",
            "urgent": True
        }
    elif "blight" in filename:
        return {
            "disease": "Early Blight",
            "confidence": "92%",
            "treatment": "Remove infected leaves. Use copper-based sprays.",
            "urgent": True
        }
    elif "aphid" in filename:
        return {
            "disease": "Aphid Infestation",
            "confidence": "89%",
            "treatment": "Spray Neem oil or introduce ladybugs.",
            "urgent": False
        }
    else:
        return {
            "disease": "Unknown / Healthy",
            "confidence": "Low",
            "treatment": "Ensure proper watering and check soil nutrients.",
            "urgent": False
        }