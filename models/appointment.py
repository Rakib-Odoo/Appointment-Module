from odoo import models, fields, api,_


class CorporateAppointment(models.Model):
    _name = 'corporate.appointment'
    _description = 'Corporate Appointment Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'title'

    # Fields definition
    title = fields.Char(string="Appointment Title", required=True, tracking=True)
    appointment_date = fields.Date(string='Appointment DateTime', tracking=True)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today, tracking=True)
    company_name = fields.Char(string='Company Name')
    employee_id = fields.Many2one('hr.employee', string="Appointment To", required=True)
    location = fields.Char(string="Email")
    contact = fields.Char(string='Mobile')

    sl_no = fields.Char(
        string="Sl No",
        required=True, copy=False, readonly=True,
        index='trigram',
        default=lambda self: _('New'))



    # client details
    client_name = fields.Many2one('res.partner', string="Appointment From")
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    company = fields.Char(string='Company Name')

    # Address Fields
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    zip = fields.Char(string='Zip Code')
    country_id = fields.Many2one('res.country', string='Country')



    # Appointment time range
    appointment_start = fields.Datetime(string='Start Time', tracking=True)
    appointment_end = fields.Datetime(string='End Time', tracking=True)

    # Duration (calculated field)
    duration = fields.Float(string='Duration (hours)', compute='_compute_duration', store=True)

    @api.depends('appointment_start', 'appointment_end')
    def _compute_duration(self):
        for rec in self:
            if rec.appointment_start and rec.appointment_end:
                duration = (rec.appointment_end - rec.appointment_start).total_seconds() / 3600.0
                rec.duration = duration
            else:
                rec.duration = 0.0


    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='scheduled')
    notes = fields.Text(string="Notes")

    def action_scheduled(self):
        self.state = 'scheduled'

    def action_completed(self):
        self.state = 'completed'

    def action_cancelled(self):
        self.state = 'cancelled'

    @api.model
    def create(self, vals):
        if not vals.get('notes'):
            vals['notes'] = 'New Appointment Created.'
        if vals.get('sl_no', _("New")) == _("New"):
            vals['sl_no'] = self.env['ir.sequence'].next_by_code(
                'appointment.appointment') or _("New")

