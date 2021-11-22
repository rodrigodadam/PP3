import os
from dgroup import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )













# # Made the request form should get the data and render the success page.
# # - Create a JS popup to give the feedback that the informations was received.
# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         client = request.form['client']
#         rating = request.form['rating']
#         comments = request.form['comments']
#         # print(client, rating, comments)
#         # Simple validation, if the client do not insert the name He'll 
#         # receive a message to imput the name and index.html will be render again
#         if client == '':
#             return render_template('index.html', message='Please insert all required informations')
#         return render_template('success.html')

