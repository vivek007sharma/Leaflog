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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.keras.models.load_model("../LeafLog.keras")

CLASS_NAMES = ['Aloevera','Amla','Amruthaballi','Arali','Badipala','Astma_weed','Balloon_Vine','Bamboo','Beans','Betel','Bhrami','Bringaraja','Caricature','Castor','Catharanthus','Chakte','Chilly','Citron lime (herelikai)','Coffee','Common rue(naagdalli)','Coriender','Curry','Doddpathre','Drumstick','Ekka','Eucalyptus','Ganigale','Ganike','Gasagase','Ginger','Globe Amarnath','Guava','Henna','Hibiscus','Honge','Insulin','Jackfruit','Jasmine','Kambajala','Kasambruga','Kohlrabi','Lantana','Lemon','Lemongrass','Malabar_Nut','Malabar_Spinach','Mango','Marigold','Mint','Neem','Nelavembu','Nerale','Nooni','Onion','Padri','Palak(Spinach)','Papaya','Parijatha','Pea','Pepper','Pomoegranate','Pumpkin','Raddish','Rose','Sampige','Sapota','Seethaashoka','Seethapala','Spinach1','Tamarind','Taro','Tecoma','Thumbe','Tomato','Tulsi','Turmeric','ashoka','camphor','kamakasturi','kepala']

BLOGS={

    "Betel": "Betel leaf (Piper betle) is a heart-shaped leaf widely used in traditional medicine, especially in Ayurveda. It is packed with antioxidants and possesses antibacterial, antifungal, and anti-inflammatory properties. Chewing betel leaves is known to aid digestion, freshen breath, and boost oral health. The leaves are also used to treat cough, cold, and respiratory issues due to their decongestant properties. Additionally, betel leaf juice is applied to wounds and skin infections for faster healing. Rich in essential oils, betel leaves help regulate blood sugar levels and improve metabolism. They are also believed to have mild aphrodisiac properties.",
    "Aloevera": "Aloe Vera (Aloe barbadensis miller) is a succulent plant known for its healing properties. Its gel is rich in vitamins, enzymes, and amino acids, making it a powerful remedy for burns, wounds, and skin conditions like acne. Aloe Vera is also used in digestive health, helping to soothe stomach ulcers and constipation. It has antimicrobial and anti-inflammatory properties that support immunity and skin hydration. Regular consumption of Aloe Vera juice can improve digestion and regulate blood sugar levels. The plant is widely used in cosmetics and herbal medicine for its hydrating, soothing, and anti-aging effects.",
    "Catharanthus": "Catharanthus (Catharanthus roseus), also known as Madagascar Periwinkle, is a medicinal plant valued for its alkaloids, which are used in cancer treatment. It contains vincristine and vinblastine, essential in chemotherapy for leukemia and lymphoma. In traditional medicine, it is used to treat diabetes, wounds, and infections. The plant also has antibacterial and antifungal properties. Catharanthus extracts are used to lower blood sugar levels and improve blood circulation. Despite its medicinal benefits, high doses can be toxic. This evergreen shrub, with its beautiful pink or white flowers, is often grown as an ornamental plant in gardens worldwide.",
    "Arali": "Arali (Nerium oleander), commonly known as Oleander, is an evergreen shrub with vibrant pink, white, or red flowers. Despite its beauty, it is highly toxic due to cardiac glycosides, which affect heart function. Traditionally, it has been used in Ayurveda for skin diseases, ulcers, and inflammation, but only under medical supervision. Some cultures use Arali extracts to treat asthma, indigestion, and infections. However, ingestion can cause severe poisoning, affecting the nervous system and heart. Due to its ornamental appeal, Arali is widely planted in gardens and public spaces. Extreme caution is advised while handling any part of this plant.",
    "Caricature": "Caricature plant (Graptophyllum pictum) is an ornamental shrub known for its unique variegated leaves. Traditionally used in folk medicine, it is believed to have anti-inflammatory and wound-healing properties. Its leaves are used to treat skin conditions, bruises, and infections. In some cultures, Caricature plant extracts are used to aid digestion and relieve gastrointestinal disorders. The plant contains antioxidants that help reduce oxidative stress. While not as well known as other medicinal plants, Caricature is valued for both its decorative appeal and potential health benefits. It is commonly grown in tropical gardens for its striking foliage and easy maintenance.",
    "Castor": "Castor (Ricinus communis) is a fast-growing plant widely cultivated for its seeds, which produce castor oil. This oil is rich in ricinoleic acid and is used for treating constipation, skin ailments, and inflammation. Castor oil is also a natural remedy for hair growth and joint pain relief. However, raw castor seeds contain ricin, a highly toxic substance. The plant has antimicrobial and antifungal properties, making it useful in traditional medicine for wound healing. Castor oil is commonly used in cosmetics, lubricants, and biofuels. Despite its toxicity, controlled processing makes castor one of the most versatile medicinal plants.",
    "Chakte": "Chakte is a lesser-known medicinal plant used in traditional remedies for inflammation and skin infections. It is known for its antibacterial and antifungal properties, helping to treat wounds and ulcers. Some cultures use Chakte extracts to improve digestion and respiratory health. The plant's leaves and roots contain bioactive compounds that help in pain relief and reduce swelling. Though not widely studied, Chakte is valued in folk medicine for its ability to boost immunity and promote overall well-being. It is also used in herbal teas for its calming effects and as a natural remedy for digestive issues.",
    "Chilly": "Chilly (Capsicum annuum or Capsicum frutescens) is one of the most widely used spices globally, valued for its heat and medicinal benefits. It contains capsaicin, which has anti-inflammatory and pain-relieving properties. Chilly is known to boost metabolism, promote weight loss, and improve blood circulation. It is also beneficial for digestion, helping to prevent gastric ulcers and indigestion. The spice has antibacterial properties, making it useful for preventing infections. In some traditional remedies, chilly is applied topically to relieve muscle and joint pain. Rich in vitamins A and C, chilly also strengthens the immune system and improves heart health.",
    "Citron lime (herelikai)": "Citron (Citrus medica) is an ancient citrus fruit known for its medicinal and culinary uses. It is rich in vitamin C, antioxidants, and essential oils that boost immunity and fight infections. Citron juice is traditionally used to treat indigestion, nausea, and respiratory issues. The fruit’s peel contains bioactive compounds that promote heart health and reduce inflammation. In Ayurveda, Citron is used for its detoxifying and digestive properties. It is also applied to the skin for its brightening and anti-aging effects. Despite being less common than lemons, Citron remains a valuable fruit in herbal medicine and natural remedies.",
    "Common rue(naagdalli)": "Common Rue (Ruta graveolens) is an aromatic herb known for its medicinal and insect-repellent properties. It has been used in traditional medicine to treat digestive issues, menstrual disorders, and joint pain. The herb has anti-inflammatory and antibacterial effects, making it useful for skin infections and wounds. Common Rue is also believed to reduce anxiety and improve blood circulation. However, high doses can be toxic, causing nausea and irritation. It is sometimes used as a natural insect repellent. Due to its strong aroma and medicinal properties, Common Rue is cultivated for both therapeutic and agricultural purposes.",
    "Ganigale": "Ganigale is a lesser-known medicinal plant used in Ayurveda for its anti-inflammatory and healing properties. It is believed to help treat digestive disorders, skin conditions, and respiratory ailments. The plant contains bioactive compounds that support immune function and promote overall health. In traditional remedies, Ganigale leaves are often used in herbal teas to relieve stress and improve digestion. Some cultures apply its extracts to wounds for faster healing. Though not widely studied in modern medicine, Ganigale remains an important plant in folk medicine, valued for its holistic health benefits and natural healing properties.",
    "Gasagase": "Gasagase (Papaver somniferum), commonly known as poppy seeds, is a plant valued for its sedative and medicinal properties. The seeds are rich in calcium, magnesium, and dietary fiber, promoting bone health and digestion. Gasagase is used in traditional medicine to treat insomnia, anxiety, and stress due to its calming effects. The plant’s extracts have pain-relieving and anti-inflammatory properties, making them useful for joint and muscle pain. In Indian cuisine, poppy seeds are commonly used in dishes for their nutty flavor and health benefits. Despite its medicinal use, excessive consumption should be avoided due to its mild narcotic properties.",

}

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

    blog_content=BLOGS.get(predicted_class,"No blog available for this leaf.")
    print(predicted_class, confidence, blog_content)
    
    return {
        'class': predicted_class,
        'confidence': float(confidence),
        'blog':blog_content
    }
# import matplotlib.pyplot as plt

# plt.axis("off")
# plt.show()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
