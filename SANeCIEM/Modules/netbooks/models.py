from django.db import models

# Create your models here.
"""
    * people(personas): Conjunto de personas que intervienen en el sistema de netbooks
    Esta tabla tiene todos los datos de las personas.
"""
class people:
    id_person = models.PositiveIntergerField( primary_key = True )
    name = models.CharField( max_lenght = 150 )
    lastname = models.CharField( max_lenght = 150 )
    dni = models.CharField( max_lenght = 9 )
    address = models.CharField( max_lenght = 200 )
    tel1 = models.PhoneNumbreField( null = False, blank = False, unique = True )
    tel2 = models.PhoneNumbreField( null = False, blank = False, unique = True )
    email = models.EmailField( max_lenght = 150 )
    anniversary = model.DateField()

"""
    * peopleDetails: Detalle de las personas que estan en la tabla
        * record: numero de legajos, los docentes/no docentes y alumnos solo poseen este campo
        * type: las personas pueden ser Docentes, No Docentes o Alumnos estos son valores tabulados en el frotend
        * status: ( valor tabulado en fronted )
            * for Docentes/No Docentes -> Regular - Jubilado
            * for Alumnos -> Regular - Egresado - Pase - ET (Egresado Tardio)
        * course: ( valor tabulado en fronted )
            Solo para los alumnos, detalla el grado que cursa el alumno
"""
class peopleDetails:
    id_person = model.ForeignKey( people, null = False, blank = False )
    record = model.PositiveSmallIntergerField( primary_key = True )
    type = model.CharField( max_lenght = 50 )
    status = model.CharField( max_lenght = 50 )
    date_entry = model.DateField()
    course = model.CharField( max_lenght = 2 )
    enable = model.BooleanField( null = True )
    datachange = model.DateTimeField( auto_now_add = True )

"""
    * Tutor: es un tipo de persona que tiene acardo uno o mas estudiantes, el no tiene:
        - Legajos
        - Estado
        - Curso
"""
class tutor:
    id_person = model.ForeignKey( people, null = False, blank = False )
    record = model.ForeignKey( peopleDetails, null = False, blank = False )
    comment = model.CharField( max_lenght = 250 )
    enable = model.BooleanField( default = True )

"""
    * ModelsNetbook: contiene los diferentes modelos de las netbook 
        - model valor tabulado en el frontend
        - gen valor tabulado en el frontend
        - ageModel valor tabulado en el frotend
"""
class modelsNetbook:
    id_model = model.PositiveIntergerField( primary_key = True )
    model = model.CharField( max_lenght = 30 )
    gen = model.CharField( max_lenght = 4 )
    ageModel = model.CharField( 4 )

# netbook: contiene los datos de la netbook
class netbook:
    id_model = model.ForeignKey( modelsNetbook, null = False, blank = False )
    id_netbook = model.CharField( max_lenght = 25, primary_key = True )
    status = model.CharField( max_lenght = 1, choices = [ 
                                                         ( 'B':'Buena' ), 
                                                         ( 'E':'Excelente' ),
                                                         ( 'M':'Mal Estado' ),
                                                         ( 'N':'Nuevo' ),
                                                         ( 'R':'Roto' ),
                                                         ( 'Q':'Quemado' ),
                                                         ( 'P':'Pesimas Condiciones' )
                                                        ], default = 'B' )
    comment = model.CharField( max_lenght = 250 )

#   * chargers: contiene los datos de los cargadores asignadas a la netbook
class charger:
    id_charger = model.PositiveIntergerField( primary_key = True )
    id_netbook = model.ForeignKey( netbook, null = False, blank = False )
    comment = model.CharField( max_lenght = 250 )

#   * digitalMobile: contiene las netbook perteneciente algun carro mobil
class digitalMobile:
    id_digMob = model.PositiveIntergerField( primary_key = True )
    letter = model.CharField( max_lenght = 1, choices [ 'A', 'B', 'C', 'D', 'E', 'F'], default = 'A' )
    number = model.CharField( max_lenght = 2 )
    id_netbook = model.ForeignKey( netbook, null = False, blank = False )
    comment = model.DateField( max_lenght = 250 )
    enable = model.BooleanField( null = True )

#    * netbook4People: contiene el registro de las netbook que pasaron por diferentes usuarios Alumnos
class netbook4People:
    id_n4p = model.PositiveIntergerField( primary_key = True )
    id_netbook = model.ForeignKey( netbook, null = False, blank = False )
    record = model.ForeignKey( peopleDetails, null = False, blank = False )
    comment = model.DateField( max_lenght = 250 )
    date_n4p = model.DateTimeField( auto_now_add = True )
    enable = model.BooleanField( null = True )

"""
    * proceedings: contiene el registro de actas de una netbook
        - type: tipo de acta ( valor tabulado desde frontend )
        - act: contendido de la acta ( default dependiendo del tipo de acta tambien desde frontend )
"""
class proceedings:
    id_act = model.PositiveIntergerField( primary_key = True )
    id_netbook = model.ForeignKey( netbook, null = False, blank = False )
    act = model.CharField( max_lenght = 500 )
    type_act = model.CharField( max_lenght = 50 )
    date_act = model.DateTimeField( auto_now_add = True )  

#   * detailAct: contiene las netbook aparte del principal que se usaron en el acta.
class detailAct:
    id_detailAct = model.PositiveIntergerField( primary_key = True )
    id_act = model.ForeignKey( proceedings, null = False, blank = False )
    id_netbook_involved = model.CharField( max_lenght = 25 )
    date_act = model.DateTimeField( auto_now_add = True  )

#    * technicalReport: contiene el registro del reporte tecnico de la computadora
class technicalReport:
    nro_treport = model.PositiveIntergerField( primary_key = True )
    id_netbook = model.ForeignKey( netbook, null = False, blank = False )
    name_technical = model.CharField( max_lenght = 150 )
    report = model.CharField( max_lenght = 500 )
    date_report = model.DateTimeField( auto_now_add = True )

#   * detailsTR: contiene las netbook intervinientes en el reporte tecnico
class detailsTR:
    id_detailTR = model.PositiveIntergerField( primary_key = True )
    nro_treport = model.ForeignKey( technicalReport, null = False, blank = False )
    id_netbook_involved = model.CharField( max_lenght = 25 )
    date_dtr = model.DateField()
