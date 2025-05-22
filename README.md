# 📝 Blog Personnel - Django

Bienvenue sur le dépôt de mon **blog personnel développé avec Django**.  
Ce projet me permet d’explorer le développement web avec Python et Django, en construisant une plateforme de publication simple, propre et évolutive.

---

## 🚀 Fonctionnalités

- 🖊️ Création, modification et suppression d’articles
- 🧾 Interface d’administration (via Django admin)
- 🔍 Navigation par catégories ou tags
- 📱 Design responsive (compatible mobile)

---

## 🛠️ Technologies utilisées

- Django (backend)
- HTML, CSS, HTMX (frontend de base)
- SQLite
- Django templating engine
- Tailwind CSS

---

## 📦 Installation locale

1. **Cloner le dépôt**  
``` bash
git clone https://github.com/ton-utilisateur/nom-du-repo.git
cd nom-du-repo
```

2. **Create a virtual env**  
``` bash
python -m venv env
source env/bin/activate
```
3. **Install dependencies**  
``` bash
pip install -r requirements.txt
```
4. **Apply migrations**  
``` bash
python manage.py migrate
```
5. **Create a superuser**  
``` bash
python manage.py createsuperuser
```
6. **Run the server** 
``` bash
python manage.py runserver
```

run locally on localhost:8000 by default

## Poject structure

blog/
├── blog/             # Configuration du projet Django
├── posts/            # App principale du blog
├── templates/        # Templates HTML
├── static/           # Fichiers CSS/JS/images
├── media/            # Uploads (images, etc.)
├── manage.py
└── requirements.txt
