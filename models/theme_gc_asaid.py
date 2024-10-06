from odoo import models


class ThemeGC(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_gc_asaid_post_copy(self, mod):
        self.enable_view('website.template_footer_descriptive')
