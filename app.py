from flask import Flask, render_template, request, redirect, session
import os
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# MySQL configurations
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='plagiarismchecker'
)

# Front end rendering 
@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        session['username'] = user[0]
        return redirect('/welcome')  # Redirect to dashboard or any other page after successful login
    else:
        error = 'Invalid credentials. Please try again.'
        return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    try:
        cursor.execute(query, (username, password))
        db.commit()
        message = "Successfully registered! Please login."
        return render_template('login.html', message=message)
    except mysql.connector.Error as err:
        error = "Error: {}".format(err)
        return render_template('signup.html', error=error)
    
@app.route('/welcome')
def welcome():
    plagiarism_results = check_plagiarism()
    return render_template('welcome.html', plagiarism_results=plagiarism_results)


# Backend plagiarism checking
def check_plagiarism():
    sample_files = [doc for doc in os.listdir() if doc.endswith('.c')]
    sample_contents = [open(file).read() for file in sample_files]

    # Use TfidfVectorizer to convert the words to an array of numbers
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sample_contents)

    results = set()
    
    for i, text_vector_a in enumerate(vectors):
        for j, text_vector_b in enumerate(vectors):
            if i != j:
                similarity_score = cosine_similarity(text_vector_a, text_vector_b)[0][0]
                sample_pair = sorted((sample_files[i], sample_files[j]))
                # Similarity score * 100 is the percentage of plagiarism
                score = sample_pair[0], sample_pair[1], similarity_score * 100
                # Append to the results list that is to be returned
                results.add(score)

    return results

if __name__ == '__main__':
    app.run(debug=True)
