from django.shortcuts import render
from datetime import date

# Create your views here.
all_posts =[ {
            "slug": "python-django",
            "image": "django.jpg",
            "author": "Kasturi",
            "date": date(2021, 7, 21),
            "title": "Python Django",
            "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
          },
          {
            "slug": "programming-is-fun",
            "image": "coding.jpg",
            "author": "Sanket",
            "date": date(2022, 3, 10),
            "title": "Programming Is Great!",
            "content": """
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
              aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
              velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
          },
{
              "slug": "programming-is-fun",
              "image": "coding.jpg",
              "author": "Suchitra",
              "date": date(2022, 3, 10),
              "title": "Programming Is Great!",
              "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
              """
          },
{
              "slug": "programming-is-fun",
              "image": "coding.jpg",
              "author": "ketan",
              "date": date(2022, 3, 10),
              "title": "Programming Is Great!",
              "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
              """
          },
{
              "slug": "programming-is-fun",
              "image": "coding.jpg",
              "author": "santa",
              "date": date(2022, 3, 10),
              "title": "Programming Is Great!",
              "content": """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
              """
          }
]
def index(request):
    return render(request,'blog/startingpage.html',{
      'posts':all_posts
})

def Allpost(request):
    return render(request, 'blog/Allpost.html',{'posts':all_posts})

def Postinfo(request, slug):
    post = None
    for p in all_posts:
      if p['slug'] == slug:
          post = p
          break
    return render(request,"blog/postinfo.html",{'post':post})





