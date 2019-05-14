from django.db import models
from django.conf import settings

# Create your models here.


class PersonalWebsite(models.Model):
    name                                  = models.CharField(max_length=100, null=True,  blank=True)
    location                              = models.CharField(max_length=200, null=True,  blank=True)
    category                              = models.CharField(max_length=200, null=True,  blank=True)
    title                                 = models.CharField(max_length=200, null=True,  blank=True)
    text                                  = models.TextField(max_length=2000, null=True,  blank=True)







    about_title                           = models.CharField(max_length=2000, null=True, blank=True)
    about_details                         = models.TextField(max_length=2000, null=True, blank=True)
    about_title_one                           = models.CharField(max_length=2000, null=True, blank=True)
    about_title_two                          = models.CharField(max_length=2000, null=True, blank=True)
    about_title_three                           = models.CharField(max_length=2000, null=True, blank=True)
    about_title_four                           = models.CharField(max_length=2000, null=True, blank=True)

    projects_done                           = models.CharField(max_length=2000, null=True, blank=True)
    projects_done_number                           = models.CharField(max_length=2000, null=True, blank=True)



    social_media_linkedin                = models.CharField(max_length=2000, null=True, blank=True)
    social_media_facebook                = models.CharField(max_length=2000, null=True, blank=True)
    social_media_github                  = models.CharField(max_length=2000, null=True, blank=True)
    social_media_stack_overflow          = models.CharField(max_length=2000, null=True, blank=True)
    social_media_twitter                 = models.CharField(max_length=2000, null=True, blank=True)
    social_media_instagram               = models.CharField(max_length=2000, null=True, blank=True)

    image = models.ImageField(default='', blank=True)




    contact_email = models.CharField(max_length=2000, null=True, blank=True)
    contact_address = models.CharField(max_length=2000, null=True, blank=True)
    contact_number = models.CharField(max_length=2000, null=True, blank=True)

    timestamp                            = models.DateTimeField(auto_now_add=True)
    updated                              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class Post(models.Model):

    blog_small_title = models.CharField(max_length=2000, null=True, blank=True)
    blog_title = models.CharField(max_length=2000, null=True, blank=True)
    blog_text = models.TextField(max_length=2000, null=True, blank=True)
    blog_images = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)



# class PostTwo(models.Model):
#
#     blog_small_title_two = models.CharField(max_length=2000, null=True, blank=True)
#     blog_title_two = models.CharField(max_length=2000, null=True, blank=True)
#     blog_text_two = models.TextField(max_length=2000, null=True, blank=True)
#     blog_images_two = models.ImageField(upload_to='')
#     created_date_two = models.DateTimeField(auto_now_add=True)
#     published_date_two = models.DateTimeField(blank=True, null=True)
#
#
# class PostThree(models.Model):
#
#     blog_small_title_three = models.CharField(max_length=2000, null=True, blank=True)
#     blog_title_three = models.CharField(max_length=2000, null=True, blank=True)
#     blog_text_three = models.TextField(max_length=2000, null=True, blank=True)
#     blog_images_three = models.ImageField(upload_to='')
#     created_date_three = models.DateTimeField(auto_now_add=True)
#     published_date_three = models.DateTimeField(blank=True, null=True)



class Email(models.Model):

    email_name  =models.CharField(max_length=100, null=True,  blank=True)
    from_email = models.EmailField( max_length=100, null=True,  blank=True )
    subject = models.CharField(max_length=100, null=True,  blank=True)
    message = models.CharField( max_length=100, null=True,  blank=True)



class Recentwork(models.Model):
    recent_work_one = models.CharField(max_length=2000, null=True, blank=True)
    # recent_work_two = models.CharField(max_length=2000, null=True, blank=True)
    # recent_work_three = models.CharField(max_length=2000, null=True, blank=True)
    # recent_work_four = models.CharField(max_length=2000, null=True, blank=True)

    work_image_one = models.ImageField(default='', blank=True)
    # work_image_two = models.ImageField(default='', blank=True)
    # work_image_three = models.ImageField(default='', blank=True)
    # work_image_four = models.ImageField(default='', blank=True)
    # work_image_five = models.ImageField(default='', blank=True)
    # work_image_six = models.ImageField(default='', blank=True)


class Gallery(models.Model):

    gallery_title = models.CharField(max_length=2000, null=True, blank=True)
    gallery_text = models.TextField(max_length=2000, null=True, blank=True)
    gallery_images = models.ImageField(upload_to='')
    gallery_date = models.DateTimeField(auto_now_add=True)
    gallery_published_date = models.DateTimeField(blank=True, null=True)

class Experience(models.Model):
    experience_title_one = models.CharField(max_length=2000, null=True, blank=True)
    experience_years_one = models.CharField(max_length=2000, null=True, blank=True)
    experience_details_one = models.TextField(max_length=2000, null=True, blank=True)

    # experience_title_two = models.CharField(max_length=2000, null=True, blank=True)
    # experience_years_two = models.CharField(max_length=2000, null=True, blank=True)
    # experience_details_two = models.TextField(max_length=2000, null=True, blank=True)
    #
    # experience_title_three = models.CharField(max_length=2000, null=True, blank=True)
    # experience_years_three = models.CharField(max_length=2000, null=True, blank=True)
    # experience_details_three = models.TextField(max_length=2000, null=True, blank=True)
    #
    # experience_title_four = models.CharField(max_length=2000, null=True, blank=True)
    # experience_years_four = models.CharField(max_length=2000, null=True, blank=True)
    # experience_details_four = models.TextField(max_length=2000, null=True, blank=True)
    #
    # experience_title_five = models.CharField(max_length=2000, null=True, blank=True)
    # experience_years_five = models.CharField(max_length=2000, null=True, blank=True)
    # experience_details_five = models.TextField(max_length=2000, null=True, blank=True)
    #
    # experience_title_six = models.CharField(max_length=2000, null=True, blank=True)
    # experience_years_six = models.CharField(max_length=2000, null=True, blank=True)
    # experience_details_six = models.TextField(max_length=2000, null=True, blank=True)



class Education(models.Model):

    education_masters = models.CharField(max_length=2000, null=True, blank=True)
    education_masters_details = models.TextField(max_length=2000, null=True, blank=True)
    education_masters_details_two = models.TextField(max_length=2000, null=True, blank=True)

class Skill(models.Model):
    skills_title = models.CharField(max_length=2000, null=True, blank=True)
    skills_details = models.CharField(max_length=10, null=True, blank=True)

class Services(models.Model):
    services_title_one                        = models.CharField(max_length=2000, null=True, blank=True)
    services_details_one                     = models.TextField(max_length=2000, null=True, blank=True)



class Client(models.Model):
    coffee = models.CharField(max_length=2000, null=True, blank=True)
    coffee_number = models.CharField(max_length=2000, null=True, blank=True)

    projects = models.CharField(max_length=2000, null=True, blank=True)
    projects_number = models.CharField(max_length=2000, null=True, blank=True)

    client = models.CharField(max_length=2000, null=True, blank=True)
    client_number = models.CharField(max_length=2000, null=True, blank=True)

    partners = models.CharField(max_length=2000, null=True, blank=True)
    partners_number = models.CharField(max_length=2000, null=True, blank=True)