from odoo import models, api

class UpdateShippingWave(models.Model):
    _name = 'run.action.schedule'

    @api.model
    def run_function(self):
        # Call stored procedure
        self.env.cr.execute("SELECT lp_function_postgresql()")
