import os
from dgroup import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )





# class Feedback(base):
#     __tablename__ = 'feedback'
#     id = Column(Integer, primary_key=True)
#     client = Column(String(150))
#     rating = Column(Integer)
#     comments = Column(String(500))

#     def __init__(self, client, rating, comments):
#         self.client = client
#         self.rating = rating
#         self.comments = comments







# # Made the request form should get the data and render the success page.
# # TODO - Create a JS popup to give the feedback that the informations was received.
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


# if __name__ == '__main__':
#     app.run()