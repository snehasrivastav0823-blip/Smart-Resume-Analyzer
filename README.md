# 📄 Smart Resume Analyzer

## 🚀 Overview
The Smart Resume Analyzer is a Machine Learning-based web application that analyzes resumes by comparing them with job descriptions. It uses Natural Language Processing (NLP) techniques to calculate a match score, detect missing skills, and provide suggestions for improvement.

---

## 🎯 Features
- Upload resume in PDF format  
- Input job description  
- Calculate match score (%)  
- Identify missing skills  
- Provide improvement suggestions  
- Simple and interactive UI  

---

## 🧠 Technologies Used
- Python  
- scikit-learn  
- nltk  
- pdfminer.six  
- Streamlit  

---

## ⚙️ How It Works
1. Extract text from resume  
2. Clean and preprocess text  
3. Convert text into vectors using TF-IDF  
4. Calculate similarity using cosine similarity  
5. Identify missing skills  
6. Display results  

---

## 📁 Project Structure
resume-analyzer/
│── app.py
│── utils.py
│── skills.py
│── requirements.txt

---

## 🛠️ Installation & Setup
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
streamlit run app.py
## 🧪 Usage
- Upload your resume (PDF)  
- Paste the job description  
- View:
  - Match Score  
  - Missing Skills  
  - Suggestions  

---

## 📊 Output Interpretation
- 70–90% → Strong Match  
- 40–70% → Moderate Match  
- 20–40% → Weak Match  

---

## ⚠️ Limitations
- Uses keyword-based skill matching  
- Limited dataset  
- Accuracy depends on resume format  

---

## 🔮 Future Improvements
- Advanced NLP models (BERT)  
- Automatic skill extraction  
- Resume ranking system  
- Cloud deployment  

---

## 👨‍💻 Author
Sneha Srivastava  
