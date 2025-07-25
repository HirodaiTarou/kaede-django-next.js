from django.contrib import admin
from .models import Review, ReviewLog, Like, DeleteReviewRequest

admin.site.register(Review)
admin.site.register(ReviewLog)
admin.site.register(Like)
admin.site.register(DeleteReviewRequest)
