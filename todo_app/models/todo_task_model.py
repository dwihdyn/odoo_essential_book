from odoo import api, fields, models

class TodoTask(models.Model):
    _name = 'todo.task'              # name that will be used to refer to this class
    _description = 'To-do Task'      # user-friendly name
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.users',string = 'Responsible',default=lambda self: self.env.user)   # to let current user automatically be recorded 
    team_ids = fields.Many2many('res.partner', string='Team')
    
    date_deadline=fields.Datetime('Date Deadline')  # book forgot to add this
    


    @api.multi
    def do_clear_done(self):
        for task in self:
            task.active = False
        return True

    @api.multi
    def write(self,values):
        if 'active' not in values:
            values['active'] = True
        super().write(values)
