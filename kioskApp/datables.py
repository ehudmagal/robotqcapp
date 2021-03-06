from kioskApp.models import *
from datable.web.table import Table
from  datable.web import storage
from datable.web.columns import StringColumn, DateTimeColumn, DateColumn
from datable.web.widgets import *
from web.columns import *
from kioskApp.models import *

def getScriptsTable(_user):
    q = RobotScript.objects.filter(user = _user).order_by('script_date','script_time')
    return Table(
        name='scriptstable',
        storage=storage.Storage( #There's a clash between TamuzApp's "Storage" and datable's "Storage" so we use storage.Storage (see import...)
            querySet =q,
            columns=[
                StringColumn('script_description','script description'),
                StringColumn('type','type'),
                DateColumn('script_date','script date'),
                StringColumn('script_time','script time'),
                ButtonColumn('Edit Script details',
                    serializer=ButtonSerializer('/robot_scripts_page/','Edit Script Details','RobotScript_id'),width=250),
                ],
            widgets=[
                StringWidget('type', placeholder='type'),
                StringWidget('script_description', placeholder='description'),
                DateWidget('script_date', placeholder='date '),
                ],
        ),
    )

def getExperimentsTable(_user):
    q = Experiment.objects.filter(user = _user).order_by('date','time')

    return Table(
        name='experimentstable',
        storage=storage.Storage( #There's a clash between TamuzApp's "Storage" and datable's "Storage" so we use storage.Storage (see import...)
            querySet =q,
            columns=[
                StringColumn('name','Name'),
                StringColumn('type','Type'),
                StringColumn('grade','Grade'),
                 StringColumn('distance','Distance'),
                StringColumn('volume','Volume'),
                StringColumn('description','Description'),
                StringColumn('pipetingMode','Pipeting Mode'),
                StringColumn('liquidClass','Liquid Class'),
                StringColumn('tipType','Tip Type'),
                StringColumn('sourcePlastic','Source Plastic'),
                StringColumn('destPlastic','Dest Plastic'),
                #StringColumn('plateReader','plate reader'),
                DateColumn('date','date',type='date'),
                StringColumn('time','time',type='time'),
                ButtonColumn('Edit Experiment details',
                    serializer=ButtonSerializer('/experiments/','Edit Experiment Details','Experiment_id'),width=250),
                ],
            widgets=[
                StringWidget('name', placeholder=' name'),
                StringWidget('description', placeholder='description'),
                StringWidget('volume', placeholder='volume'),
                DateWidget('date', placeholder='date '),
                ],
        ),
    )
def getErrorsTable(script):
    q = RobotScriptError.objects.filter(robotscript=script).order_by('date','time')
    return Table(
        name='errorstable',
        storage=storage.Storage( #There's a clash between TamuzApp's "Storage" and datable's "Storage" so we use storage.Storage (see import...)
            querySet =q,
            columns=[
                StringColumn('description','Description'),
                DateColumn('date','date'),
                StringColumn('time','time'),
                ButtonColumn('Edit error  details',
                    serializer=ButtonSerializer('/robot_scripts_page/robotscript/','Edit Error  Details','RobotScriptError_id'),width=250),
                ],
            widgets=[
                StringWidget('description', placeholder='description'),
                DateWidget('date', placeholder='date '),
                ],
        ),
    )