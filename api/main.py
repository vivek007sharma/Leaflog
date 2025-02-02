# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.middleware.cors import CORSMiddleware

# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf

# app = FastAPI()

# MODEL = tf.keras.models.load_model("../LeafLog.keras")


# CLASS_NAMES = ['Ganigale', 'Pea', 'Sampige', 'Seethapala', 'Malabar_Spinach', 'Gasagase', 'Honge', 'Amla', 'Lemongrass', 'Castor', 'Palak(Spinach)', 'Raddish', 'Drumstick', 'Catharanthus', 'Rose', 'Malabar_Nut', 'Pepper', 'Coffee', 'Betel', 'Marigold', 'Arali', 'kepala', 'Lemon', 'Tecoma', 'Beans', 'Citron lime (herelikai)', 'Mango', 'Papaya', 'Nooni', 'Taro', 'Neem', 'Globe Amarnath', 'Tulsi', 'Ganike', 'Chakte', 'Lantana', 'Chilly', 'Tamarind', 'Doddpathre', 'Balloon_Vine', 'Astma_weed', 'Guava', 'Curry', 'Kasambruga', 'Kohlrabi', 'Onion', 'Badipala', 'Padri', 'kamakasturi', 'Aloevera', 'Nelavembu', 'Spinach1', 'Kambajala', 'Sapota', 'Hibiscus', 'Nerale', 'Ekka', 'Pomoegranate', 'Eucalyptus', 'Insulin', 'Bringaraja', 'Parijatha', 'Thumbe', 'Common rue(naagdalli)', 'camphor', 'Tomato', 'Ginger', 'Mint', 'Caricature', 'Henna', 'Turmeric', 'Jasmine', 'Bhrami', 'Amruthaballi', 'Bamboo', 'Coriender', 'Pumpkin', 'Seethaashoka', 'ashoka', 'Jackfruit']
# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"


# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image
# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...)
# ):
#     # bytes = await file.read()
#     image=read_file_as_image(await file.read())
#     img_batch = np.expand_dims(image, 0)
#     prediction = MODEL.predict(img_batch)
#     # CLASS_NAMES[np.argmax(prediction)]
#     predicted_class = CLASS_NAMES[np.argmax(prediction)]
#     confidence = np.max(prediction[0])
#     print(predicted_class, confidence)
#     return {
#         'class': predicted_class,
#         'confidence': float(confidence)
#     }

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8001)







from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("../LeafLog.keras")

CLASS_NAMES = ['Aloevera','Amla','Amruthaballi','Arali','Badipala','Astma_weed','Balloon_Vine','Bamboo','Beans','Betel','Bhrami','Bringaraja','Caricature','Castor','Catharanthus','Chakte','Chilly','Citron lime (herelikai)','Coffee','Common rue(naagdalli)','Coriender','Curry','Doddpathre','Drumstick','Ekka','Eucalyptus','Ganigale','Ganike','Gasagase','Ginger','Globe Amarnath','Guava','Henna','Hibiscus','Honge','Insulin','Jackfruit','Jasmine','Kambajala','Kasambruga','Kohlrabi','Lantana','Lemon','Lemongrass','Malabar_Nut','Malabar_Spinach','Mango','Marigold','Mint','Neem','Nelavembu','Nerale','Nooni','Onion','Padri','Palak(Spinach)','Papaya','Parijatha','Pea','Pepper','Pomoegranate','Pumpkin','Raddish','Rose','Sampige','Sapota','Seethaashoka','Seethapala','Spinach1','Tamarind','Taro','Tecoma','Thumbe','Tomato','Tulsi','Turmeric','ashoka','camphor','kamakasturi','kepala']
INPUT_SHAPE = MODEL.input_shape[1:3]  

@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}

# def read_file_as_image(data) -> np.ndarray:
#     """Load image, resize it to model's expected input shape, and return as a NumPy array"""
#     image = Image.open(BytesIO(data)).convert("RGB") 
#     image = image.resize(INPUT_SHAPE) 
#     image = np.array(image) / 255.0  
#     return image

def read_file_as_image(data) -> np.ndarray:
    """Load image, resize while maintaining aspect ratio, and return as a NumPy array"""
    image = Image.open(BytesIO(data)).convert("RGB")  # Ensure 3 channels

    # Get model's expected input size
    expected_height, expected_width = MODEL.input_shape[1:3]

    # Resize while keeping aspect ratio (avoids distortion)
    image = image.resize((expected_width, expected_height), Image.LANCZOS)

    # Normalize if needed (check if model was trained on [0,1] or [0,255])
    image_array = np.array(image, dtype=np.float32)  # Convert to float
    # if image_array.max() > 1:  # If pixel values are 0-255, normalize
        # image_array = image_array / 255.0  

    return image_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, axis=0)  

    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction[0])

    print(predicted_class, confidence)
    
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
# import matplotlib.pyplot as plt

# plt.axis("off")
# plt.show()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
