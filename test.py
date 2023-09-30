from utils.fire_baseee_db import db
#from utils.chain import qa

# question = "summerize the procedure for Summoning and Dissolution of National Assembly"
# result = qa({'question': question})

# print(result['answer'])

users_ref = db.collection('user').document('nnamaka7@gmail.com').collection('chats').document('4fP6PaZI8iCo5zPOaQZs').collection('messages')

# /user/nnamaka7@gmail.com/chats/4fP6PaZI8iCo5zPOaQZs/messages/1MKEWvxgDZqKC16q6hEU
# or /users/
docs = users_ref.stream()
for doc in docs:
    print(u'Data: {}'.format(doc.to_dict()))