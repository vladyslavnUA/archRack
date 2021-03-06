# archRack

##  Tech Stack (current)
```
> Django  (Backend)
> Python  (Backend)
> Bootstrap/CSS (UI/UX)
```

##  Tools (current)
```
> Django Crispy Forms  (General)
> CK-Editor  (Docs)
> Python  (Backend)
> Bootstrap/CSS (UI/UX)
```

## Roadmap

**Backend:**
- [x] User Authentication
- [x] Users can create Projects
- [ ] Users can edit/delete Projects
- [x] Users can create Docs
- [ ] Users can edit/delete Docs
- [ ] Users can create/edit Teams
- [ ] Users can create/edit Company

**Frontend:**
- [x] Templates setup
- [x] Forms rendered via crispy
- [ ] Improved UI/UX
- [ ] Drag & Drop

## Running Locally

Steps to run the Django-based project:
```
git clone https://github.com/vladyslavnUA/archRack archrack && cd archrack

# create a virtual environment
virtualenv env
source env/bin/activate

# install dependancies
pip install -r requirements.txt

# run migrations to create db
python manage.py migrate

# run the server
python manage.py runserver      

# head to http://localhost:8000/
```
