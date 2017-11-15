class ReadOnlyAdminMixin(object):
    """Disables all editing capabilities."""
    enabled_fields = []

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}

        if not getattr(self, 'show_save', False):
            extra_context['show_save'] = False
            extra_context['show_save_and_continue'] = False

        return super().change_view(
            request,
            object_id,
            form_url,
            extra_context=extra_context,
        )

    def get_form(self, *args, **kwargs):
        form = super(ReadOnlyAdminMixin, self).get_form(*args, **kwargs)

        for field_name in form.base_fields:
            if field_name not in self.enabled_fields:
                form.base_fields[field_name].disabled = True

        return form

    def has_add_permission(self, request):
        return False
