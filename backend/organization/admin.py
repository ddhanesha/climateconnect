from django.contrib import admin

from organization.models import (
    Organization, OrganizationTags, OrganizationTagging,
    Project, ProjectTags, ProjectTagging, Post, Comment,
    PostComment, ProjectComment, ProjectMember, OrganizationMember,
    ProjectParents, ProjectStatus, ProjectCollaborators, ProjectFollower,
    OrganizationFieldTagging
)

pass_through_models = (
    OrganizationTags, OrganizationTagging, ProjectTags,
    ProjectTagging, Post, Comment, PostComment, ProjectComment, 
    ProjectStatus, ProjectCollaborators, ProjectFollower,
    OrganizationFieldTagging
)

for model in pass_through_models:
    admin.site.register(model, admin.ModelAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'country', 'state', 'city', 'url-slug')


admin.site.register(Organization, OrganizationAdmin)


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_filter = ('status',)


admin.site.register(Project, ProjectAdmin)


class ProjectMemberAdmin(admin.ModelAdmin):
    search_fields = ('user__name', 'user__id', 'project__name',)
    list_filter = ('role__name',)


admin.site.register(ProjectMember, ProjectMemberAdmin)


class OrganizationMemberAdmin(admin.ModelAdmin):
    search_fields = ('user__name', 'user__id', 'organization__name',)
    list_filter = ('role__name',)


admin.site.register(OrganizationMember, OrganizationMemberAdmin)


class ProjectParentsAdmin(admin.ModelAdmin):
    search_fields = ('project__name', 'organization__name')


admin.site.register(ProjectParents, ProjectParentsAdmin)
