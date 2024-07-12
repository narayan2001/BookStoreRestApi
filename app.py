from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"},
    {"id":4,"title":"Book 4","author":"Author 4"},
]

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>',methods=['GET'])
def get_book(id):
    book = None
    for b in books:
        if b['id'] == id:
            book =b
            break

    if book:
        return jsonify(book),200
    return jsonify({'error':'Book Not Found'}),400

@app.route('/books',methods=["POST"])
def create_book():
    new_book = request.json
    if not new_book or 'title' not in new_book or 'author' not in new_book:
        return jsonify({'error':'Missing data'}),400
    
    #generate a new id

    new_book['id'] = max(book['id'] for book in books) +1
    books.append(new_book)
    return jsonify(new_book),201

@app.route('/books/<int:id>',methods=["DELETE"])
def delete_book(id):
    global books
    initial_length = len(books)
    books = [book for book in books if book['id']!=id]

    if len(books) < initial_length:
        return jsonify({'message':'Book Deleted'}),200
    
    else:
        return jsonify({'error':'Book not found'}),404
    


if __name__ == '__main__' :
    app.run(debug=True)