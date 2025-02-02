from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("../LeafLog.keras")


CLASS_NAMES = ['Ganigale', 'Pea', 'Sampige', 'Seethapala', 'Malabar_Spinach', 'Gasagase', 'Honge', 'Amla', 'Lemongrass', 'Castor', 'Palak(Spinach)', 'Raddish', 'Drumstick', 'Catharanthus', 'Rose', 'Malabar_Nut', 'Pepper', 'Coffee', 'Betel', 'Marigold', 'Arali', 'kepala', 'Lemon', 'Tecoma', 'Beans', 'Citron lime (herelikai)', 'Mango', 'Papaya', 'Nooni', 'Taro', 'Neem', 'Globe Amarnath', 'Tulsi', 'Ganike', 'Chakte', 'Lantana', 'Chilly', 'Tamarind', 'Doddpathre', 'Balloon_Vine', 'Astma_weed', 'Guava', 'Curry', 'Kasambruga', 'Kohlrabi', 'Onion', 'Badipala', 'Padri', 'kamakasturi', 'Aloevera', 'Nelavembu', 'Spinach1', 'Kambajala', 'Sapota', 'Hibiscus', 'Nerale', 'Ekka', 'Pomoegranate', 'Eucalyptus', 'Insulin', 'Bringaraja', 'Parijatha', 'Thumbe', 'Common rue(naagdalli)', 'camphor', 'Tomato', 'Ginger', 'Mint', 'Caricature', 'Henna', 'Turmeric', 'Jasmine', 'Bhrami', 'Amruthaballi', 'Bamboo', 'Coriender', 'Pumpkin', 'Seethaashoka', 'ashoka', 'Jackfruit']
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    pass
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
