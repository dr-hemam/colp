from colp import app, db
from project.models import Project
from flask import render_template, redirect, url_for, request, session
from users.models import User
from users.decorators import *
from lookaheads.models import LookAhead, LookAheadDetail
from lookaheads.form import LookAheadForm, LookAheadDetailForm
from calendars.models import ReportingDate

@app.route('/newlookahead', methods=['POST', 'GET'])
@login_required
@project_required
def new_lookahead():
    form = LookAheadForm()
    form.reportingdate.query = ReportingDate.query.filter_by(project_id= session.get('project_id'))
    if request.method == "POST" and form.validate() and session.get('project_id'):
        project = Project.query.filter_by(id=session.get('project_id')).first()
        lookahead = LookAhead (project= project, 
                                reportingdate= form.reportingdate.data )
        db.session.add(lookahead)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('new_lookahead_details', id= lookahead.id))
    return render_template('lookaheads/lookaheadform.html', form=form, action='new')
    

@app.route('/newlooaheaddetails/<id>', methods=['POST', 'GET'])
def new_lookahead_details(id):
    form = LookAheadDetailForm()
    lookaheadmain = LookAhead.query.filter_by(id= id).all()
    form.lookahead.query = lookaheadmain
    
    if request.method == "POST":
        codes = request.form.getlist('task_code')
        names = request.form.getlist('task_name')
        starts = request.form.getlist('start')
        finishs = request.form.getlist('finish')
        is_actives = request.form.getlist('is_active')
        for i in range(len(codes)):
            task = LookAheadDetail(lookahead = lookaheadmain[0],
                                    code= codes[i], 
                                    name= names[i], 
                                    start= starts[i], 
                                    finish= finishs[i], 
                                    is_active= is_actives[i])
            db.session.add(task)
            db.session.commit()
        
        return(str(names))
    return render_template('lookaheads/lookaheaddetailsform.html', form=form, action='new', lookahead = lookaheadmain[0])
        
@app.route('/viewlookaheads')
@login_required
@project_required
def view_lookaheads():
    lookaheads = LookAhead.query.filter_by(project_id=session['project_id']).all()
    print('lookaheads', lookaheads)
    return render_template('lookaheads/view.html', lookaheads=lookaheads)
    
@app.route('/viewlookahead/<id>')
@login_required
@project_required
def view_lookahead(id):
    lookahead = LookAhead.query.filter_by(id=id).first()
    details = LookAheadDetail.query.filter_by(lookahead_id=id).all()
    return render_template('lookaheads/viewlookahead.html', lookahead = lookahead, tasks = details)