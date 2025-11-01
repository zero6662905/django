from django.shortcuts import render


# Головна сторінка блогу
def home_view(request):
    context = {
        "blog_name": "TechBlog",
        "description": "Найкращі статті про технології та програмування"
    }
    return render(request, "blog/home.html", context)


# Перевірка досвіду користувача (через POST форму)
def check_experience(request):
    experience_years = None
    if request.method == 'POST':
        # Отримуємо число років досвіду з форми, якщо не передано — беремо 0
        experience_years = int(request.POST.get('years', 0))
    return render(request, "blog/experience.html", {"years": experience_years})


# Відображення списку популярних постів
def popular_posts(request):
    posts_data = [
        {"title": "Вивчаємо Python", "views": 1520},
        {"title": "Django для початківців", "views": 980},
        {"title": "JavaScript ES6", "views": 1340},
        {"title": "React Hooks", "views": 760},
        {"title": "Machine Learning", "views": 2100},
    ]

    context = {
        "blog_title": "Популярні статті TechBlog",
        "posts": posts_data,
    }
    return render(request, "blog/popular.html", context)

def about_view(request):
    context = {
        "title": "Про нас",
        "team_members": [
            {"name": "Олена", "role": "Редактор та контент-менеджер"},
            {"name": "Іван", "role": "Full-Stack розробник"},
            {"name": "Марія", "role": "Дизайнер UX/UI"},
        ]
    }
    return render(request, "blog/about.html", context)


def contact_view(request):
    context = {
        "title": "Контакти",
        "email": "info@techblog.com",
        "phone": "+380 67 123 45 67",
        "address": "м. Київ, вул. Технологічна, 42"
    }
    return render(request, "blog/contact.html", context)
