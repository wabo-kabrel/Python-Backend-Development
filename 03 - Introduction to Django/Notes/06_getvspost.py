# Handling GET vs POST Requests in Django

#1. What are GET and POST?
# - GET: Sends data in the URL. For retrieving data (search, filters).
# - POST: Sends data in the body. For submitting or changing data (login, register, forms).

#2. Example of a GET Request
# - URL:
#       http://127.0.0.1:8000/search/?q=django
# - Here, ?q=django is a GET parameter.
# - In Django, you can access it using the python code:
#   query = request.GET.get('q')

#3. Example of a POST Request
# - POST data is usually submitted from a form.
# - In Django, you can access it using the code:
#   text = request.POST.get('text')

#4. Creating a New View to Handle Both GET and POST
# - Let’s create a “Text Processor” view to show both methods in action.
'''
def text_processor_view(request):
    context = {}

    if request.method == 'POST':
        submitted_text = request.POST.get('text')
        word_count = len(submitted_text.split()) if submitted_text else 0
        char_count = len(submitted_text) if submitted_text else 0

        context = {
            'submitted_text': submitted_text,
            'word_count': word_count,
            'char_count': char_count
        }

    elif request.method == 'GET':
        name = request.GET.get('name', 'Guest')
        context = {
            'greeting': f'Welcome, {name}!'
        }

    return render(request, 'home/text_processor.html', context)
'''

#5. Creating the Template text_processor.html
'''
<!DOCTYPE html>
<html>
<head>
    <title>Text Processor</title>
</head>
<body>
    {% if greeting %}
        <h2>{{ greeting }}</h2>
    {% endif %}

    <form method="post">
        {% csrf_token %}
        <textarea name="text" rows="6" cols="50" placeholder="Enter some text..."></textarea><br><br>
        <input type="submit" value="Analyze Text">
    </form>

    {% if submitted_text %}
        <h3>Original Text:</h3>
        <p>{{ submitted_text }}</p>

        <h3>Stats</h3>
        <ul>
            <li>Word Count: {{ word_count }}</li>
            <li>Character Count: {{ char_count }}</li>
        </ul>
    {% endif %}
</body>
</html>
'''

#6. Register the URL
# - In home/urls.py:
'''
path('text-processor/', views.text_processor_view, name='text_processor'),
'''

#7. Test it in Browser
# - Visit:
        # - http://127.0.0.1:8000/text-processor/?name=Kabrel
        # - You should see: “Welcome, Kabrel!”
# - Type text into the textarea and submit
        # - It shows word and character count using POST

#8. Summary of request.method
'''
if request.method == 'POST':
    # Use request.POST.get()
elif request.method == 'GET':
    # Use request.GET.get()
'''

#9. When to Use GET vs POST
#   ----------------------------------------------------------------------- 
#   | Operation            | Method | Why                                 |
#   |----------------------|--------|-------------------------------------|
# - | Search               | GET    | So it can appear in the URL         |
# - | Contact form         | POST   | Because you're sending data         |
# - | Login / Register     | POST   | Secure, avoids exposing info        |
# - | Pagination / Sorting | GET    | Allows link sharing and bookmarking |
#   -----------------------------------------------------------------------
