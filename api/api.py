import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     
     'author': 'Vernor Vinge',
     
     'year_published': '1992'},
    {'id': 1,
     
     'author': 'Ursula K. Le Guin',
     
     'published': '1973'},
    {'id': 2,
   
     'author': 'Samuel R. Delany',
    
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id_get():
     
    
    # If no published or author is provided, display an error in the browser.
    if ('published' and 'author') in request.args:
        query_parameters = request.args
        published = query_parameters.get('published')
        author = query_parameters.get('author')
    else:
        return "Please specify a published or author"

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested entry.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['author'] == author or book['published'] == published :
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    if(len(results)==0):
        return "entry not found"

    return jsonify(results)

@app.route('/api/v1/resources/books', methods=['DELETE'])
def api_id_delete():
   # If no published or author is provided, display an error in the browser.
    if ('published' and 'author') in request.args:
        query_parameters = request.args
        published = query_parameters.get('published')
        author = query_parameters.get('author')
    else:
        return "Please specify a published or author"


    

    # Loop through the data and match results that fit the requested entry.
    # IDs are unique, but other fields might return many results
    ok =0
    for book in books:
        if book['author'] == author or book['published'] == published :
            books.remove(book)
            ok=1
    # if given id is not found      
    if ok==0:
        return "does not contain book with given author or published"

@app.route('/api/v1/resources/books', methods=['POST'])
def api_id_post():
    
    # If no published or author is provided, display an error in the browser.
    if ('published' and 'author') in request.args:
        query_parameters = request.args
        published = query_parameters.get('published')
        author = query_parameters.get('author')
    else:
        return "Please specify a published and author"

    

   
    # IDs are unique, but other fields might return many results
    id=len(books)
    book ={'id':id,
    'published':published,
    'author':author
    }   
    books.append(book)    
    return jsonify(books)  

@app.route('/api/v1/resources/books', methods=['PUT'])
def api_id_put():
    
   
    # Check if an ID was provided as part of the URL.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        query_parameters = request.args
        id=int(query_parameters.get('id'))
        published = query_parameters.get('published')
        author = query_parameters.get('author')
    else:
        return "Please specify a id"

    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # Update entry
    for book in books:
        if book['id'] == id:
            if published!=None:
                book['published']=published
                return ("updated published")
            if book['author']!=None:
                book['author']=author
                return ("updated published")
            

            
    
            
if __name__ == "__main__":
    app.run()