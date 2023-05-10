{
    "name": "Smart Office",
    "version": "1.0",
    "depends": [
        "base_setup",
    ],
    "data": [
        "security/ir.model.access.csv",
        "report/reservation_templates.xml",
        "report/reservation_reports.xml",
        "views/office_space_views.xml",
        "views/office_space_menus.xml",
        "views/reservation_views.xml",
        "views/reservation_menus.xml",
        "views/smart_office_menu.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": True,
    "license": "LGPL-3",
}
