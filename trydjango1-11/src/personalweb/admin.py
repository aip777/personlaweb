from django.contrib import admin

# Register your models here.


from .models import PersonalWebsite

admin.site.register(PersonalWebsite)



from .models import Post

admin.site.register(Post)


# from .models import PostTwo
#
# admin.site.register(PostTwo)
#
#
#
# from .models import PostThree
#
# admin.site.register(PostThree)




from .models import Email

admin.site.register(Email)


from .models import Recentwork

admin.site.register(Recentwork)


from .models import Gallery

admin.site.register(Gallery)



from .models import Experience

admin.site.register(Experience)


from .models import Education

admin.site.register(Education)

from .models import Skill

admin.site.register(Skill)




from .models import Services

admin.site.register(Services)


from .models import Client

admin.site.register(Client)