{
    'name': "Resource Mailing",
    'summary': "Resource management",
    'version': '16.0.1.0.0',
    'website': "https://mcaf.nb.ca/en/",
    'author': "MCAF",
    'category': "Appointments",
    'license': 'OPL-1',
    "application": True,
    "installable": True,
    'depends': ['base',
                'mass_mailing'],
    'data': [
        'security/ir.model.access.csv',
        'views/resource_mail_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
