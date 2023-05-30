from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,IntegerField,SubmitField


from wtforms.validators import DataRequired



FAI=Flask(__name__)




class GaniForms(Form):
    name=StringField(validators=[DataRequired()])
    age=IntegerField(validators=[DataRequired()])
    submit=SubmitField()


@FAI.route('/webform/',methods=['GET','POST'])
def WebForm():
    GFO=GaniForms()
    if request.method=='POST':
        GFD=GaniForms(request.form)
        if GFD.validate():
            return GFD.data

    return render_template('webform.html',GFO=GFO)


if __name__=='__main__':
    FAI.run(debug=True)
