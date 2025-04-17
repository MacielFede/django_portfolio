from django.contrib import admin
from .models import PortfolioInfo, Project


class PortfolioInfoAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "job_position",
        "degree_name",
        "avatar",
        "about_me",
        "phone_number",
        "email",
        "github",
        "linkedin",
        "price",
    ]

    def has_add_permission(self, request):
        # Prevent addition if instance already exists
        return not PortfolioInfo.objects.exists()

    def changelist_view(self, request, extra_context=None):
        # Redirect to the change page of the existing object
        info = PortfolioInfo.objects.first()
        if not info:
            info = PortfolioInfo.objects.create()
        from django.urls import reverse
        from django.shortcuts import redirect

        return redirect(reverse("admin:portfolio_portfolioinfo_change", args=[info.id]))


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)


admin.site.register(PortfolioInfo, PortfolioInfoAdmin)
admin.site.register(Project, ProjectAdmin)
