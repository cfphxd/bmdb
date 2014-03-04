from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.db import connections


# report view
import json
import datetime
import csv
#import mm
import xlwt
import hashlib

from datetime import date
from helpers import JsonResponse
from queries import QuerySupplier

def make_file_name(report, ext):
    today = date.today()
    return report + '_' + hashlib.md5(str(today)).hexdigest() + ext



def get_xls(report, data, header):
    from xlwt import Workbook

    wb = Workbook()
    ws = wb.add_sheet(report)

    col = 0
    for h in header:
        ws.write(0,col,h)
        col+=1

    row = 1
    for l in data:
        col = 0
        for v in l:
           ws.write(row, col, v) 
           col+=1
        row+=1

    fname = make_file_name(report,'.xls')
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % fname

    wb.save(response)

    return response



def get_csv(report, data, head):
    # Create the HttpResponse object with the appropriate CSV header.
    fname = make_file_name(report,'.csv')
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % fname

    writer = csv.writer(response)
    writer.writerow(head)
    for row in data:
        writer.writerow(row)

    return response


def get_html(report, data, head):
    s = '<table>'

    s += '<tr>'
    for h in head:
        s += '<th>' + str(h) + '</th>'
    s += '</th>'

    for l in data:
        s += '<tr>'
        for v in l:
            s += '<td>' + str(v) + '</td>'
        s += '</tr>'

    s += '</table>'

    return HttpResponse(s)

def report_view(request, report, param, fmt):

    data, head = report_data(request, report, param)

    if fmt == 'HTML':
        return get_html(report, data, head) 
    elif fmt== 'JSON':
        data.insert(0,head)
        return JsonResponse(data)
    elif fmt=='CSV':
        return get_csv(report, data, head)
    elif fmt=="XLS":
        return get_xls(report, data, head)
    elif fmt=="RAW":
        return HttpResponse(data)

    return HttpResponse('Form unknown')

def report_data(request, report, param):
    qry_supp = QuerySupplier(report)

    cursor = connections['default'].cursor()

    cursor.execute(qry_supp.query(param))

    desc = cursor.description

    data = []
    head = []
    for h in desc:
        head.append(h.name)

    for row in cursor.fetchall():
        data.append(row)

    return data, head


def add_config(request, name, descr):
    conf = BdbConfig.objects.get_or_create(name=name)
    conf.descr = descr
    conf.save()
    return HttpResponsestr(str(conf.id))

def add_biomarker(request, name, descr):
    biom = BdbBiomarker.objects.get_or_create(name=name);
    biom.descr = descr
    biom.save()
    return HttpResponsestr(str(biom.id))

def add_disease(request, biom_id, name, descr):
    dise = BdbDisease.objects.get_or_create(name=name)
    dise.descr = descr
    dise.save()
    biom = BdbBiomarker.objects.get(id=biom_id)
    biom.add(dise)

    return HttpResponsestr(str(biom.id))
    
