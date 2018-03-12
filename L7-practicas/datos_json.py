import json

data = {}
data["people"] = []
data['people'].append({
    'Nombre de la asignatura': 'Programacion en entornos de red',
    'Curso': '1o',
    'Nombre de la titulacion': 'Ingenieria biomedica',
    'Temas de la asignatura': [
        [{'Numero de tema':'1'},
        {'Titulo': 'Aprende a programar'},
        {'Numero de horas': 10}
        ],
        [{'Numero de tema':'2'},
        {'Titulo': 'Seguimos programando'},
        {'Numero de horas': 15}
        ]
    ]

})

with open('datos2.json', 'w') as outfile:
    json.dump(data, outfile)
