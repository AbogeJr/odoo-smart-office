
{
    'name': 'office',
    'version': '1.0',
    'depends': [
        'base_setup',
    ],
    'data': [
		'security/ir.model.access.csv',
        'views/office_views.xml',
	],
	'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
