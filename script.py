from django.contrib.auth.hashers import make_password
hashed = make_password('mypw')

from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    ...
# finish defining function

data = json.loads(request.body)

users = {}
users['alice'] = 'pass123'

# in /signup
users[username] = make_password(password)

# how to check username login password thingies
check_password(password, users[username])

request.session['user_id'] = user.user_id

if request.session.get('user_id'):
    return render(request, 'profile.html')
else:
    return redirect('/login')

# block access to private pages
if not request.session.get('user_id'):
    return redirect('/login')

# logging out
request.session.flush()

#cookies yaaaaaaaaaaaaaaaaaaaaaay
request.COOKIES.get('sessionid')