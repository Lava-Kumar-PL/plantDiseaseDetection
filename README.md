# 🌿 Plant Disease Detection using Deep Learning

A web-based AI application to detect diseases in plant leaves using image classification. Upload a photo of a plant leaf and get real-time results about its disease and possible treatments. Powered by ResNet34 and trained on the PlantVillage dataset.

---

## 🚀 Demo

🔗 [Live Demo](https://your-app-link.com) *(Coming soon)*  
📸 Upload → 🧠 Predict → 💡 Cure Info

---

## 📂 Project Structure

```
plantDiseaseDetection/
│
├── static/                  # Static assets (CSS, JS)
├── templates/               # HTML templates
│   ├── landing.html
│   └── predict.html
├── Models/
│   └── plantDisease-resnet34.pth  # Trained PyTorch model
├── app.py                   # Flask app backend
├── model.py                 # Model loading & prediction logic
├── utils.py                 # Disease dictionary
├── requirements.txt         # Dependencies
└── README.md                # Project info
```

---

## 🧠 Model Details

- **Architecture**: ResNet34 (Pretrained on ImageNet)
- **Framework**: PyTorch
- **Classes**: 38 plant disease categories
- **Dataset**: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)

Each input image is resized to 128x128 and passed through a fine-tuned ResNet34 model.

---

## 📊 Dataset

- Total Images: ~54,000+
- Source: PlantVillage dataset on Kaggle
- Contains images for 14 crops including:
  - Apple 🍎
  - Grape 🍇
  - Corn 🌽
  - Tomato 🍅
  - Potato 🥔
  - Strawberry 🍓
  - Pepper 🌶️
  - ...and more

---

## 💻 Usage

### 🛠️ Setup

```bash
# Clone the repo
git clone https://github.com/Lava-Kumar-PL/plantDiseaseDetection.git
```
```bash
cd plantDiseaseDetection
```

```bash
# Install dependencies
pip install -r requirements.txt
```
```bash
# Run the application
python app.py
```

Open your browser and go to:

```bash
http://127.0.0.1:5000
```

---

## 🔍 How It Works

1. User uploads an image (drag & drop or file select)
2. Image is sent to backend (`Flask`) via POST
3. ResNet34 processes the image and returns predicted class
4. Mapped disease name and solution are displayed via `utils.py`

---

## 🖼️ Screenshots

> *(Add real screenshots here for better UX)*

- **Landing Page**
- **Image Upload & Prediction**
- **Result Display with Solution**

---

## 🛠️ Technologies Used

- **Frontend**: HTML5, Tailwind CSS
- **Backend**: Flask (Python)
- **Model**: PyTorch (ResNet34)
- **Tools**: PIL, torchvision, base64 encoding

---

## 📦 Features

- ✅ Real-time disease prediction
- 🧠 Deep learning-based backend
- 📱 Responsive UI
- 🌐 Drag & Drop + File Upload
- 🧾 Detailed prevention and cure tips
- 📤 Easy to extend to mobile or desktop apps

---

## 📌 Limitations

- Requires good image quality for accurate prediction
- Currently supports only 38 classes from PlantVillage
- Model runs on CPU (can be slow for larger apps)

---

## 🔮 Future Work

- Add multilingual disease tips
- Android/iOS App Integration
- Add feedback collection from users
- Model compression (e.g., quantization, pruning)
- Deploy to cloud (Render, Hugging Face Spaces, etc.)

---

## 🙌 Contributing

Pull requests and issues are welcome. Feel free to fork and improve!

```bash
git checkout -b feature/your-feature-name
git commit -m "Added new feature"
git push origin feature/your-feature-name
```

---


## 🙋‍♂️ Author

**Lava Kumar PL**  
🔗 [GitHub](https://github.com/Lava-Kumar-PL)
