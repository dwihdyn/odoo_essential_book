from odoo import models,fields, api

class PhoneBook(models.Model):
    _name = 'phone.book'
    _description = "Phone Book"

    name = fields.Char(string="nAmE", required= True)
    related_partner = fields.Many2one(comodel_name='res.partner', string="rELatEd pARtnEr")
    
    date_of_joining = fields.Date(string="dAtE oF jOiNiNG")
    category_id = fields.Many2many(comodel_name= 'res.partner.category', string="tAGs")
    
    city = fields.Char(string="cItY", required=True)
    street = fields.Char(string="sTrEEt", required=True)
    country_id = fields.Many2one(comodel_name='res.country', string="cOUntRy")
    address = fields.Char(string="fUlL aDdreSs", compute='_calculate_address')
    address_for_printing = fields.Char(string="Printing Address", compute='return_full_address')

    def print_name(self):
        print("Name of record: %s" %self.name)
        return True

    api.depends('country_id','city','street')
    def _calculate_address(self):
        # if country_id is None:
        #     full_address = self.city + ' ,' + self.street
        # else:
        full_address = self.country_id.name + ' ,' + self.city + ' ,' + self.street
        self.address = full_address

    @api.model
    @api.onchange('name','address')       # if change 'name' or 'address', everything will change automatically
    def return_full_address(self):
        if self.name and self.address:
            self.address_for_printing = 'customer: ' + self.name + ' ,' + self.address


# see oreilly section6 last chapter on explanation @api.one , self.ensure_one() , @api.model

    # using create() function to upper() case the 'name' enterred when we create() new form
    @api.model
    def create(self,values):
        if 'name' in values:
            values['name'] = values['name'].upper()
            new_rec = super(PhoneBook, self).create(values)
            return new_rec

    # write(), same as create(), but applies for editing. create() meant for create new file ONLY
    @api.multi
    def write(self, values, context = None):
        if 'name' in values:
            values['name'] = values['name'].upper()
            old_rec = super(PhoneBook, self).write(values)
        else:
            old_rec = super(PhoneBook, self).write(values)
        return True

    # unlink(), ensuring that you can/cant delete something if the criteria are satisfied
    @api.multi
    def unlink(self):
        for rec in self:
            if rec.name == 'JOHN':
                raise NameError('Name that is exactly "JOHN" cant be deleted...because fuck you, thats why lmao')