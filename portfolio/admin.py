from django.contrib import admin
from .models import PortfolioInfo, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)


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

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Redirect to the change page of the existing object
        info = PortfolioInfo.objects.first()
        if not info:
            info = PortfolioInfo.objects.create()
        from django.urls import reverse
        from django.shortcuts import redirect

        return redirect(reverse("admin:portfolio_portfolioinfo_change", args=[info.id]))

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_continue"] = False
        return super(PortfolioInfoAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )


admin.site.register(PortfolioInfo, PortfolioInfoAdmin)
admin.site.register(Project, ProjectAdmin)
