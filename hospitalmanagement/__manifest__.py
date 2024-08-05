{
    'name': "hospital management",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'view/hospitalmanagement_property_views.xml',
        'view/doctor_property_views.xml',
        'view/hospital_op_views.xml',
        'view/hospital_op_menu.xml',
    ],
}
