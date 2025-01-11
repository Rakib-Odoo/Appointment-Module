{
    'name': 'Appointments',
    'summary': 'Manage appointments in a corporate.',
    'description': """
        This module helps manage appointments in a corporate.
        Features include creating, updating, and scheduling appointments.
    """,
    'author': 'Nelsis Limited.',
    'website': 'https://yourwebsite.com',
    'category': 'Healthcare',
    'version': '16.0.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'hr', ],  # Add other modules like 'mail' if needed
    'data': [
        # security file
        'security/ir.model.access.csv',
        'security/security_groups.xml',
        'security/record_rules.xml',

        # data files
        'data/appointment_sequence.xml',

        # views all file
        'views/appointment_view.xml',

        ## report
        'reports/report_action.xml',
        'reports/report_appointment_template.xml',

        # views menu file
        'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
