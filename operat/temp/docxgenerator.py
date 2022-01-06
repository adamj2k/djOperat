import datetime
from docxtpl import DocxTemplate
from docx.shared import Cm, Inches, Mm, Emu


#import docx template
template = DocxTemplate('c:\\_PRACA\\ZZZ_Dane referencyjne\\!skrypty_python\\docx_generator\\operat_inwet_temp.docx')

#variable in context to pass to docx template
contex= {
    'idpracy' : 'Gk.6640.232.2021',
    #'Robota.wojew' : 'zachodniopomorskie',
    #'Robota.powiat' : 'm. Szczecin',
    #'Robota.jew' : 'm. Szczecin'
}

#render docx file
template.render(contex)
template.save('operat.docx')
