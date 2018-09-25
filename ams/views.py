from account.models import TenantProfile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PFormRM101A, PFormRM102A, PFormRM103A, PFormRM104A, PFormRM105A, PFormRM106A
from .forms import PFormRM201A, PFormRM202A, PFormRM203A, PFormRM204A, PFormRM205A, PFormRM206A
from .forms import PFormRM301A, PFormRM302A, PFormRM303A, PFormRM304A, PFormRM305A, PFormRM306A
from .forms import PFormRM201B, PFormRM202B, PFormRM203B, PFormRM204B, PFormRM205B
from .forms import PFormRM301B, PFormRM302B, PFormRM303B, PFormRM304B, PFormRM305B
from .forms import PFormRM401B, PFormRM402B, PFormRM403B, PFormRM404B, PFormRM405B
from .forms import PaymentForm
from .forms import Elec_cpu_change, Water_cpu_change, PhoneNoMessage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from ams.models import Billing, Extra, Room_type
import datetime
from django.utils.dateparse import parse_datetime, parse_date
from django.utils.timezone import is_aware, is_naive, make_aware, make_naive
# -----SMS FROM LOCALHOST & WEB------------------------------------------
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
# -----------------------------------------------------------------------
import GV


@login_required
def tenant_comment(request):
    return render(request, 'ams/tenant_comment.html', {'section': 'comment'})


@login_required
def tenant_record(request):
    return render(request, 'ams/tenant_record.html', {'section': 'record'})


# @login_required (cannot be used here !!!)
def update_pf_and_bill(roomno, cd):
    pf = get_object_or_404(TenantProfile, room_no__room_no=roomno)
    bill = get_object_or_404(Billing, room_no=roomno, status='open')

    cf = bill.bill_total - cd['payment_amount']
    bill.cf_amount = cf
    pf.cum_ovd = cf
    bill.payment_date = cd['payment_date']
    bill.payment_amount = cd['payment_amount']
    bill.status = 'close'

    bill.save()
    pf.save()

@login_required
def pay_rent(request, bref):
    tenant_bill = get_object_or_404(Billing, bill_ref=bref, status='open')
    rmn = tenant_bill.room_no

    if request.method == 'POST':
        pay_form = PaymentForm(data=request.POST)

        if pay_form.is_valid():
            cd = pay_form.cleaned_data

            # -------------------
            update_pf_and_bill(rmn, cd)
            # ------------------

        else:
            messages.error(request, 'Error updating Room {} Payment'.format(tenant_bill.room_no))

    else:
        pay_form = PaymentForm()

    if request.method == 'POST':
        # messages.info(request, 'Payments have been completed.')
        messages.success(request, 'Room {}: Payment has been completed !!!'.format(rmn))
        return HttpResponseRedirect(reverse_lazy('payment_individual'))
    else:
        return render(request, 'ams/pay_rent.html', {'tenant_bill': tenant_bill, 'pay_form': pay_form})


@login_required
def payment_individual(request):
    bills = Billing.objects.filter(status='open').order_by('id')

    return render(request, 'ams/payment_individual.html', {'bills': bills, 'section': 'payment_individual'})


@login_required
def payment(request):
    # bills were created in order from first room to last room
    bills = Billing.objects.filter(status='open').order_by('id')

    rm101a_form = None
    rm102a_form = None
    rm103a_form = None
    rm104a_form = None
    rm105a_form = None
    rm106a_form = None

    rm201a_form = None
    rm202a_form = None
    rm203a_form = None
    rm204a_form = None
    rm205a_form = None
    rm206a_form = None

    rm301a_form = None
    rm302a_form = None
    rm303a_form = None
    rm304a_form = None
    rm305a_form = None
    rm306a_form = None

    rm201b_form = None
    rm202b_form = None
    rm203b_form = None
    rm204b_form = None
    rm205b_form = None

    rm301b_form = None
    rm302b_form = None
    rm303b_form = None
    rm304b_form = None
    rm305b_form = None

    rm401b_form = None
    rm402b_form = None
    rm403b_form = None
    rm404b_form = None
    rm405b_form = None

    for bill in bills:
        rmn = bill.room_no

        if request.method == 'POST':

            if rmn == '101A':
                rm101a_form = PFormRM101A(data=request.POST, prefix='rm101a')
                if rm101a_form.is_valid():
                    cd = rm101a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 101A Payment')
            if rmn == '102A':
                rm102a_form = PFormRM102A(data=request.POST, prefix='rm102a')
                if rm102a_form.is_valid():
                    cd = rm102a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 102A Payment')

            if rmn == '103A':
                rm103a_form = PFormRM103A(data=request.POST, prefix='rm103a')
                if rm103a_form.is_valid():
                    cd = rm103a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------

                else:
                    messages.error(request, 'Error updating Room 103A Payment')

            if rmn == '104A':
                rm104a_form = PFormRM104A(data=request.POST, prefix='rm104a')
                if rm104a_form.is_valid():
                    cd = rm104a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 104A Payment')

            if rmn == '105A':
                rm105a_form = PFormRM105A(data=request.POST, prefix='rm105a')
                if rm105a_form.is_valid():
                    cd = rm105a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 105A Payment')

            if rmn == '106A':
                rm106a_form = PFormRM106A(data=request.POST, prefix='rm106a')
                if rm106a_form.is_valid():
                    cd = rm106a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 106A Payment')

            if rmn == '201A':
                rm201a_form = PFormRM201A(data=request.POST, prefix='rm201a')
                if rm201a_form.is_valid():
                    cd = rm201a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 201A Payment')

            if rmn == '202A':
                rm202a_form = PFormRM202A(data=request.POST, prefix='rm202a')
                if rm202a_form.is_valid():
                    cd = rm202a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 202A Payment')

            if rmn == '203A':
                rm203a_form = PFormRM203A(data=request.POST, prefix='rm203a')
                if rm203a_form.is_valid():
                    cd = rm203a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 203A Payment')

            if rmn == '204A':
                rm204a_form = PFormRM204A(data=request.POST, prefix='rm204a')
                if rm204a_form.is_valid():
                    cd = rm204a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 204A Payment')

            if rmn == '205A':
                rm205a_form = PFormRM205A(data=request.POST, prefix='rm205a')
                if rm205a_form.is_valid():
                    cd = rm205a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 205A Payment')

            if rmn == '206A':
                rm206a_form = PFormRM206A(data=request.POST, prefix='rm206a')
                if rm206a_form.is_valid():
                    cd = rm206a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 206A Payment')

            if rmn == '301A':
                rm301a_form = PFormRM301A(data=request.POST, prefix='rm301a')
                if rm301a_form.is_valid():
                    cd = rm301a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 301A Payment')

            if rmn == '302A':
                rm302a_form = PFormRM302A(data=request.POST, prefix='rm302a')
                if rm302a_form.is_valid():
                    cd = rm302a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 302A Payment')

            if rmn == '303A':
                rm303a_form = PFormRM303A(data=request.POST, prefix='rm303a')
                if rm303a_form.is_valid():
                    cd = rm303a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 303A Payment')

            if rmn == '304A':
                rm304a_form = PFormRM304A(data=request.POST, prefix='rm304a')
                if rm304a_form.is_valid():
                    cd = rm304a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 304A Payment')

            if rmn == '305A':
                rm305a_form = PFormRM305A(data=request.POST, prefix='rm305a')
                if rm305a_form.is_valid():
                    cd = rm305a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 305A Payment')

            if rmn == '306A':
                rm306a_form = PFormRM306A(data=request.POST, prefix='rm306a')
                if rm306a_form.is_valid():
                    cd = rm306a_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 306A Payment')

            if rmn == '201B':
                rm201b_form = PFormRM201B(data=request.POST, prefix='rm201b')
                if rm201b_form.is_valid():
                    cd = rm201b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 201B Payment')

            if rmn == '202B':
                rm202b_form = PFormRM202B(data=request.POST, prefix='rm202b')
                if rm202b_form.is_valid():
                    cd = rm202b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 202B Payment')

            if rmn == '203B':
                rm203b_form = PFormRM203B(data=request.POST, prefix='rm203b')
                if rm203b_form.is_valid():
                    cd = rm203b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 203B Payment')

            if rmn == '204B':
                rm204b_form = PFormRM204B(data=request.POST, prefix='rm204b')
                if rm204b_form.is_valid():
                    cd = rm204b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 204B Payment')

            if rmn == '205B':
                rm205b_form = PFormRM205B(data=request.POST, prefix='rm205b')
                if rm205b_form.is_valid():
                    cd = rm205b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 205B Payment')

            if rmn == '301B':
                rm301b_form = PFormRM301B(data=request.POST, prefix='rm301b')
                if rm301b_form.is_valid():
                    cd = rm301b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 301B Payment')

            if rmn == '302B':
                rm302b_form = PFormRM302B(data=request.POST, prefix='rm302b')
                if rm302b_form.is_valid():
                    cd = rm302b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 302B Payment')

            if rmn == '303B':
                rm303b_form = PFormRM303B(data=request.POST, prefix='rm303b')
                if rm303b_form.is_valid():
                    cd = rm303b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 303B Payment')

            if rmn == '304B':
                rm304b_form = PFormRM304B(data=request.POST, prefix='rm304b')
                if rm304b_form.is_valid():
                    cd = rm304b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 304B Payment')

            if rmn == '305B':
                rm305b_form = PFormRM305B(data=request.POST, prefix='rm305b')
                if rm305b_form.is_valid():
                    cd = rm305b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 305B Payment')

            if rmn == '401B':
                rm401b_form = PFormRM401B(data=request.POST, prefix='rm401b')
                if rm401b_form.is_valid():
                    cd = rm401b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 401B Payment')

            if rmn == '402B':
                rm402b_form = PFormRM402B(data=request.POST, prefix='rm402b')
                if rm402b_form.is_valid():
                    cd = rm402b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 402B Payment')

            if rmn == '403B':
                rm403b_form = PFormRM403B(data=request.POST, prefix='rm403b')
                if rm403b_form.is_valid():
                    cd = rm403b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 403B Payment')

            if rmn == '404B':
                rm404b_form = PFormRM404B(data=request.POST, prefix='rm404b')
                if rm404b_form.is_valid():
                    cd = rm404b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 404B Payment')

            if rmn == '405B':
                rm405b_form = PFormRM405B(data=request.POST, prefix='rm405b')
                if rm405b_form.is_valid():
                    cd = rm405b_form.cleaned_data

                    # -------------------
                    update_pf_and_bill(rmn, cd)
                    # ------------------
                else:
                    messages.error(request, 'Error updating Room 405B Payment')


        else:
            if rmn == '101A':
                rm101a_form = PFormRM101A(prefix='rm101a')

            if rmn == '102A':
                rm102a_form = PFormRM102A(prefix='rm102a')

            if rmn == '103A':
                rm103a_form = PFormRM103A(prefix='rm103a')

            if rmn == '104A':
                rm104a_form = PFormRM104A(prefix='rm104a')

            if rmn == '105A':
                rm105a_form = PFormRM105A(prefix='rm105a')

            if rmn == '106A':
                rm106a_form = PFormRM106A(prefix='rm106a')

            if rmn == '201A':
                rm201a_form = PFormRM201A(prefix='rm201a')

            if rmn == '202A':
                rm202a_form = PFormRM202A(prefix='rm202a')

            if rmn == '203A':
                rm203a_form = PFormRM203A(prefix='rm203a')

            if rmn == '204A':
                rm204a_form = PFormRM204A(prefix='rm204a')

            if rmn == '205A':
                rm205a_form = PFormRM205A(prefix='rm205a')

            if rmn == '206A':
                rm206a_form = PFormRM206A(prefix='rm206a')

            if rmn == '301A':
                rm301a_form = PFormRM301A(prefix='rm301a')

            if rmn == '302A':
                rm302a_form = PFormRM302A(prefix='rm302a')

            if rmn == '303A':
                rm303a_form = PFormRM303A(prefix='rm303a')

            if rmn == '304A':
                rm304a_form = PFormRM304A(prefix='rm304a')

            if rmn == '305A':
                rm305a_form = PFormRM305A(prefix='rm305a')

            if rmn == '306A':
                rm306a_form = PFormRM306A(prefix='rm306a')

            if rmn == '201B':
                rm201b_form = PFormRM201B(prefix='rm201b')

            if rmn == '202B':
                rm202b_form = PFormRM202B(prefix='rm202b')

            if rmn == '203B':
                rm203b_form = PFormRM203B(prefix='rm203b')

            if rmn == '204B':
                rm204b_form = PFormRM204B(prefix='rm204b')

            if rmn == '205B':
                rm205b_form = PFormRM205B(prefix='rm205b')

            if rmn == '301B':
                rm301b_form = PFormRM301B(prefix='rm301b')

            if rmn == '302B':
                rm302b_form = PFormRM302B(prefix='rm302b')

            if rmn == '303B':
                rm303b_form = PFormRM303B(prefix='rm303b')

            if rmn == '304B':
                rm304b_form = PFormRM304B(prefix='rm304b')

            if rmn == '305B':
                rm305b_form = PFormRM305B(prefix='rm305b')

            if rmn == '401B':
                rm401b_form = PFormRM401B(prefix='rm401b')

            if rmn == '402B':
                rm402b_form = PFormRM402B(prefix='rm402b')

            if rmn == '403B':
                rm403b_form = PFormRM403B(prefix='rm403b')

            if rmn == '404B':
                rm404b_form = PFormRM404B(prefix='rm404b')

            if rmn == '405B':
                rm405b_form = PFormRM405B(prefix='rm405b')

    if request.method == 'POST':
        # messages.info(request, 'Payments have been completed !!!')
        messages.success(request, 'All payments have been completed !!!')

        return HttpResponseRedirect(reverse_lazy('admin_page'))
    else:
        return render(request, 'ams/payment.html', {'bills': bills, 'section': 'payment',
                                                    'rm101a_form': rm101a_form,
                                                    'rm102a_form': rm102a_form,
                                                    'rm103a_form': rm103a_form,
                                                    'rm104a_form': rm104a_form,
                                                    'rm105a_form': rm105a_form,
                                                    'rm106a_form': rm106a_form,

                                                    'rm201a_form': rm201a_form,
                                                    'rm202a_form': rm202a_form,
                                                    'rm203a_form': rm203a_form,
                                                    'rm204a_form': rm204a_form,
                                                    'rm205a_form': rm205a_form,
                                                    'rm206a_form': rm206a_form,

                                                    'rm301a_form': rm301a_form,
                                                    'rm302a_form': rm302a_form,
                                                    'rm303a_form': rm303a_form,
                                                    'rm304a_form': rm304a_form,
                                                    'rm305a_form': rm305a_form,
                                                    'rm306a_form': rm306a_form,

                                                    'rm201b_form': rm201b_form,
                                                    'rm202b_form': rm202b_form,
                                                    'rm203b_form': rm203b_form,
                                                    'rm204b_form': rm204b_form,
                                                    'rm205b_form': rm205b_form,

                                                    'rm301b_form': rm301b_form,
                                                    'rm302b_form': rm302b_form,
                                                    'rm303b_form': rm303b_form,
                                                    'rm304b_form': rm304b_form,
                                                    'rm305b_form': rm305b_form,

                                                    'rm401b_form': rm401b_form,
                                                    'rm402b_form': rm402b_form,
                                                    'rm403b_form': rm403b_form,
                                                    'rm404b_form': rm404b_form,
                                                    'rm405b_form': rm405b_form,

                                                    })


# def payment_individual(request):
#     return render(request, 'ams/report_type.html', {'section': 'report'})


# @login_required
# def report(request):
#     return render(request, 'ams/report_type.html', {'section': 'report'})


@login_required
def report_type(request):
    return render(request, 'ams/report_type.html', {'section': 'report'})


@login_required
def report_parameters(request):
    return render(request, 'ams/report_parameters.html', {'section': 'report'})


def get_eng_month_name(m: int):
    md = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September',
          10: 'October', 11: 'November', 12: 'December'}
    im = int(m)
    return md[im]


def get_thai_month_name(bill_date: str):
    md = {1: 'มกราคม', 2: 'กุมภาพันธ์', 3: 'มีนาคม', 4: 'เมษายน', 5: 'พฤษภาคม', 6: 'มิถุนายน', 7: 'กรกฏาคม',
          8: 'สิงหาคม', 9: 'กันยายน',
          10: 'ตุลาคม', 11: 'พฤศจิกายน', 12: 'ธันวาคม'}

    y, m, d = bill_date.split('-')

    im = int(m)
    return md[im]


def get_thai_year(bill_date: str):
    y, m, d = bill_date.split('-')

    christ_y = int(y)
    buddist_y = christ_y + 543

    return str(buddist_y)


def get_aware_datetime(date_str):
    ret = parse_datetime(date_str)
    if not is_aware(ret):
        ret = make_aware(ret)
    return ret


@login_required
def monthly_report(request):
    bld = request.POST['bld']
    if bld == 'AB':
        bld = 'A&B'

    mnth = int(request.POST['month'])
    mnth_name = get_eng_month_name(mnth)
    yr = int(request.POST['year'])

    # start_date = datetime.date(yr, mnth, 1)
    # end_date = datetime.date(yr, mnth, 30) # USE 30 TO AVOID OUT-OF-IDX RANGE

    # --------------------------------------------------------------------------
    start_date = datetime.datetime(yr, mnth, 1)
    end_date = datetime.datetime(yr, mnth, 30)  # USE 30 TO AVOID OUT OF INDX RANGE

    start_date = start_date.date()
    end_date = end_date.date()
    # --------------------------------------------------------------------------

    opl_a = None
    opl_b = None
    if bld == 'A':
        opl_a = Billing.objects.filter(status='close', room_no__endswith='A',
                                       bill_date__range=(start_date, end_date)).order_by('room_no')

    if bld == 'B':
        opl_b = Billing.objects.filter(status='close', room_no__endswith='B',
                                       bill_date__range=(start_date, end_date)).order_by('room_no')

    if bld == 'A&B':
        opl_a = Billing.objects.filter(status='close', room_no__endswith='A',
                                       bill_date__range=(start_date, end_date)).order_by('room_no')

        opl_b = Billing.objects.filter(status='close', room_no__endswith='B',

                                       bill_date__range=(start_date, end_date)).order_by('room_no')

    cum_list_a = []
    cum_list_b = []
    cum_list_ab = []

    trc_a = 0
    trac_a = 0
    tec_a = 0
    twc_a = 0
    tcsc_a = 0
    tosc_a = 0
    tovd_a = 0

    tadj_a = 0

    tbt_a = 0
    tpa_a = 0
    tbf_a = 0

    trc_b = 0
    trac_b = 0
    tec_b = 0
    twc_b = 0
    tcsc_b = 0
    tosc_b = 0
    tovd_b = 0

    tadj_b = 0

    tbt_b = 0
    tpa_b = 0
    tbf_b = 0

    trc_ab = 0
    trac_ab = 0
    tec_ab = 0
    twc_ab = 0
    tcsc_ab = 0
    tosc_ab = 0
    tovd_ab = 0

    tadj_ab = 0

    tbt_ab = 0
    tpa_ab = 0
    tbf_ab = 0

    if opl_a:
        for bill in opl_a:
            trc_a += bill.room_cost
            trac_a += bill.room_acc_cost
            tec_a += bill.electricity_cost
            twc_a += bill.water_cost
            tcsc_a += bill.common_ser_cost
            tosc_a += bill.other_ser_cost
            tovd_a += bill.overdue_amount

            tadj_a += bill.adjust

            tbt_a += bill.bill_total
            tpa_a += bill.payment_amount
            tbf_a += bill.cf_amount
        cum_list_a.append(trc_a)
        cum_list_a.append(trac_a)
        cum_list_a.append(tec_a)
        cum_list_a.append(twc_a)
        cum_list_a.append(tcsc_a)
        cum_list_a.append(tosc_a)
        cum_list_a.append(tovd_a)

        cum_list_a.append(tadj_a)

        cum_list_a.append(tbt_a)
        cum_list_a.append(tpa_a)
        cum_list_a.append(tbf_a)

    if opl_b:
        for bill in opl_b:
            trc_b += bill.room_cost
            trac_b += bill.room_acc_cost
            tec_b += bill.electricity_cost
            twc_b += bill.water_cost
            tcsc_b += bill.common_ser_cost
            tosc_b += bill.other_ser_cost
            tovd_b += bill.overdue_amount

            tadj_b += bill.adjust

            tbt_b += bill.bill_total
            tpa_b += bill.payment_amount
            tbf_b += bill.cf_amount
        cum_list_b.append(trc_b)
        cum_list_b.append(trac_b)
        cum_list_b.append(tec_b)
        cum_list_b.append(twc_b)
        cum_list_b.append(tcsc_b)
        cum_list_b.append(tosc_b)
        cum_list_b.append(tovd_b)

        cum_list_b.append(tadj_b)

        cum_list_b.append(tbt_b)
        cum_list_b.append(tpa_b)
        cum_list_b.append(tbf_b)

    if opl_a and opl_b:
        trc_ab = trc_a + trc_b
        trac_ab = trac_a + trac_b

        tec_ab = tec_a + tec_b
        twc_ab = twc_a + twc_b
        tcsc_ab = tcsc_a + tcsc_b
        tosc_ab = tosc_a + tosc_b
        tovd_ab = tovd_a + tovd_b

        tadj_ab = tadj_a + tadj_b

        tbt_ab = tbt_a + tbt_b
        tpa_ab = tpa_a + tpa_b
        tbf_ab = tbf_a + tbf_b

    return render(request, 'ams/monthly_report.html', {'opl_a': opl_a,
                                                       'opl_b': opl_b,
                                                       'bld': bld,
                                                       'mnth_name': mnth_name,
                                                       'yr': yr,

                                                       'cum_list_a': cum_list_a,
                                                       'cum_list_b': cum_list_b,
                                                       'cum_list_ab': cum_list_ab,
                                                       'trc_a': trc_a,
                                                       'trac_a': trac_a,
                                                       'tec_a': tec_a,
                                                       'twc_a': twc_a,
                                                       'tcsc_a': tcsc_a,
                                                       'tosc_a': tosc_a,
                                                       'tovd_a': tovd_a,

                                                       'tadj_a': tadj_a,

                                                       'tbt_a': tbt_a,
                                                       'tpa_a': tpa_a,
                                                       'tbf_a': tbf_a,

                                                       'trc_b': trc_b,
                                                       'trac_b': trac_b,
                                                       'tec_b': tec_b,
                                                       'twc_b': twc_b,
                                                       'tcsc_b': tcsc_b,
                                                       'tosc_b': tosc_b,
                                                       'tovd_b': tovd_b,

                                                       'tadj_b': tadj_b,

                                                       'tbt_b': tbt_b,
                                                       'tpa_b': tpa_b,
                                                       'tbf_b': tbf_b,

                                                       'trc_ab': trc_ab,
                                                       'trac_ab': trac_ab,
                                                       'tec_ab': tec_ab,
                                                       'twc_ab': twc_ab,
                                                       'tcsc_ab': tcsc_ab,
                                                       'tosc_ab': tosc_ab,
                                                       'tovd_ab': tovd_ab,

                                                       'tadj_ab': tadj_ab,

                                                       'tbt_ab': tbt_ab,
                                                       'tpa_ab': tpa_ab,
                                                       'tbf_ab': tbf_ab,

                                                       })


@login_required
def extra_service(request):
    extra = Extra.objects.all().order_by('id')

    current_dt = datetime.datetime.now()

    return render(request, 'ams/extra_service.html', {'extra': extra, 'current_dt': current_dt})


@login_required
def elec_cpu_change(request):
    if request.method == 'POST':
        elec_cpu_form = Elec_cpu_change(request.POST)
        if elec_cpu_form.is_valid():
            cd = elec_cpu_form.cleaned_data

            ex_item = get_object_or_404(Extra, desc='Electricity CPU')
            ex_item.cpu = cd['elec_cpu']
            ex_item.save()

            messages.info(request, 'Electricity CPU has been chnaged !!')

            return HttpResponseRedirect(reverse_lazy('admin_page'))
        else:
            messages.ERROR(request, 'Error ... !!')
    else:
        elec_cpu_form = Elec_cpu_change()
    return render(request, 'ams/elec_cpu_change.html', {'elec_cpu_form': elec_cpu_form})


@login_required
def water_cpu_change(request):
    if request.method == 'POST':
        water_cpu_form = Water_cpu_change(request.POST)
        if water_cpu_form.is_valid():
            cd = water_cpu_form.cleaned_data

            ex_item = get_object_or_404(Extra, desc='Water CPU')
            ex_item.cpu = cd['water_cpu']
            ex_item.save()

            messages.success(request, 'Water CPU has been chnaged !!')
            return HttpResponseRedirect(reverse_lazy('admin_page'))
        else:
            messages.ERROR(request, 'Error ... !!')
    else:
        water_cpu_form = Water_cpu_change()
    return render(request, 'ams/water_cpu_change.html', {'water_cpu_form': water_cpu_form})


@login_required
def room_type_rate(request):
    rm_type_rate = Room_type.objects.all()

    current_dt = datetime.datetime.now()

    return render(request, 'ams/room_type_rate.html', {'rm_type_rate': rm_type_rate, 'current_dt': current_dt})


@login_required
def current_tenant(request):
    cur_tenant = TenantProfile.objects.all().order_by('start_date')

    total_tn = cur_tenant.count()

    current_dt = datetime.datetime.now()

    return render(request, 'ams/current_tenant.html',
                  {'cur_tenant': cur_tenant, 'current_dt': current_dt, 'total_tn': total_tn})


@login_required
def vacant_rooms(request):
    oc_rooms = []
    vc_rooms = []

    all_rooms_dict = [{'rn': '101A', 'rmc': 2400}, {'rn': '102A', 'rmc': 2400}, {'rn': '103A', 'rmc': 2400},
                      {'rn': '104A', 'rmc': 2400}, {'rn': '105A', 'rmc': 2400}, {'rn': '106A', 'rmc': 2400},

                      {'rn': '201A', 'rmc': 2400}, {'rn': '202A', 'rmc': 2400}, {'rn': '203A', 'rmc': 2400},
                      {'rn': '204A', 'rmc': 2400}, {'rn': '205A', 'rmc': 2400}, {'rn': '206A', 'rmc': 2400},

                      {'rn': '301A', 'rmc': 2400}, {'rn': '302A', 'rmc': 2400}, {'rn': '303A', 'rmc': 2400},
                      {'rn': '304A', 'rmc': 2400}, {'rn': '305A', 'rmc': 2400}, {'rn': '306A', 'rmc': 2400},

                      {'rn': '201B', 'rmc': 2500}, {'rn': '202B', 'rmc': 2500}, {'rn': '203B', 'rmc': 2500},
                      {'rn': '204B', 'rmc': 2500}, {'rn': '205B', 'rmc': 3100},

                      {'rn': '301B', 'rmc': 2500}, {'rn': '302B', 'rmc': 2500}, {'rn': '303B', 'rmc': 2500},
                      {'rn': '304B', 'rmc': 2500}, {'rn': '305B', 'rmc': 3100},

                      {'rn': '401B', 'rmc': 2500}, {'rn': '402B', 'rmc': 2500}, {'rn': '403B', 'rmc': 2500},
                      {'rn': '404B', 'rmc': 2500}, {'rn': '405B', 'rmc': 3100}, ]

    cur_tenant = TenantProfile.objects.all().order_by('start_date')

    for ct in cur_tenant:
        rn_rc_dict = {}
        rn_rc_dict.setdefault('rn', '')
        rn_rc_dict.setdefault('rmc', 0.0)

        rn_rc_dict.update({'rn': str(ct.room_no), 'rmc': ct.room_no.room_type.rate})

        oc_rooms.append(rn_rc_dict)

    for armd in all_rooms_dict:
        if armd not in oc_rooms:
            vc_rooms.append(armd)

    current_dt = datetime.datetime.now()

    return render(request, 'ams/vacant_rooms.html',
                  {'cur_tenant': cur_tenant, 'vc_rooms': vc_rooms, 'current_dt': current_dt})


# SENDING MESSAGE FROM LOCALHOST AND FROM WEB !!!! **********************************************************
def send_message(to_phone_no, msg):
    account_sid = GV.Account_SID
    auth_token = GV.Auth_Token
    client = Client(account_sid, auth_token)
    sending_phone_no = GV.Sending_Phone_No

    tenant_phone_no = '+66' + to_phone_no
    sending_message = msg

    # SENDING MESSAGE *********************************************************************************
    message = client.messages.create(to=tenant_phone_no, from_=sending_phone_no, body=sending_message)

    # *************************************************************************************************


# # SENDING MESSAGE FROM WEB ??? ****************************************************************************
# def send_message(to_phone_no, msg):

#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https':os.environ['https_proxy']}

#     account_sid = GV.Account_SID
#     auth_token = GV.Auth_Token

#     client = Client(account_sid, auth_token, http_client=proxy_client)

#     sending_phone_no = GV.Sending_Phone_No
#     tenant_phone_no = '+66' + to_phone_no
#     sending_message = msg

#     # SENDING MESSAGE ********************************************************************************
#     message = client.messages.create(to=tenant_phone_no, from_=sending_phone_no, body=sending_message)
#     # ************************************************************************************************


@login_required
def send_bill_sms_to_all_tenants(request):
    bills = Billing.objects.filter(status='open').order_by('id')

    if bills:

        total_open_bills = len(bills)
        no_of_bills_sent = 0
        for rmn_bill in bills:
            rmn = rmn_bill.room_no

            rmn_pf = get_object_or_404(TenantProfile, room_no__room_no=rmn)

            # --------------------------------------------------
            # rmn_hp = rmn_pf.phone # TEMP. OFF
            rmn_hp = '0840860087'  # TESTING ONLY'
            # -------------------------------------------------

            bill_dt = rmn_bill.bill_date.date()
            cur_mth = bill_dt.month
            cur_yr = bill_dt.year
            cur_th_mth = get_thai_month_name(str(bill_dt))
            cur_th_yr = get_thai_year(str(bill_dt))
            next_dt_mth = datetime.date(cur_yr, cur_mth + 1, 15)
            next_th_m = get_thai_month_name(str(next_dt_mth))

            rn = rmn
            bank_info = GV.bank_info

            rc_and_rac = rmn_bill.room_cost + rmn_bill.room_acc_cost + rmn_bill.adjust
            wc = rmn_bill.water_cost
            ec = rmn_bill.electricity_cost
            csc = rmn_bill.common_ser_cost
            osc = rmn_bill.other_ser_cost
            ovd = rmn_bill.overdue_amount

            # TEMPORARY UNTIL OVD OF RM204A HAS BEEN COVERED =========
            if rmn == '204A':
                bt = rmn_bill.bill_total - ovd + 1000
            else:
                bt = rmn_bill.bill_total
            # ========================================================

            bill_msg = "<ห้อง {0}> กรุณาชำระค่าเช่า ประจำเดือน {1} จำนวน {2:,.0f} บาท ภายในวันที่ 5 {3} {4} {5} <รายละเอียดค่าเช่า> ห้องพร้อมอุปกรณ์: {6:,.0f} บาท นำ้: {7:,.0f} บาท ไฟ: {8:,.0f} บาท ส่วนกลาง: {9:,.0f} บาท อื่นๆ: {10:,.0f} บาท ค้างจ่าย: {11:,.0f} บาท"
            bill_msg = bill_msg.format(rn, cur_th_mth, bt, next_th_m, cur_th_yr, bank_info, rc_and_rac, wc, ec, csc,
                                       osc,
                                       ovd)

            # print(rmn_hp, ': ', bill_msg)

            # -------------------------------
            send_message(rmn_hp, bill_msg)  # TURNED OFF-FOR TESTING
            # -------------------------------
            no_of_bills_sent += 1

        messages.success(request,
                         'Billing SMS has been sent to: {} of {} rooms !!'.format(no_of_bills_sent, total_open_bills))

    else:
        messages.info(request, 'No open bills available !!!')

    return HttpResponseRedirect(reverse_lazy('misc_contents'))


@login_required
def send_sms_to_individual_room(request):
    bills = Billing.objects.filter(status='open').order_by('id')

    if bills:
        if request.method == 'POST':
            rn = request.POST['rmn']
            rmn_bill = get_object_or_404(Billing, room_no=rn, status='open')

            bill_dt = rmn_bill.bill_date.date()
            cur_mth = bill_dt.month
            cur_yr = bill_dt.year
            cur_th_mth = get_thai_month_name(str(bill_dt))
            cur_th_yr = get_thai_year(str(bill_dt))
            next_dt_mth = datetime.date(cur_yr, cur_mth + 1, 15)
            next_th_m = get_thai_month_name(str(next_dt_mth))
            bank_info = GV.bank_info

            rc_and_rac = rmn_bill.room_cost + rmn_bill.room_acc_cost + rmn_bill.adjust
            wc = rmn_bill.water_cost
            ec = rmn_bill.electricity_cost
            csc = rmn_bill.common_ser_cost
            osc = rmn_bill.other_ser_cost
            ovd = rmn_bill.overdue_amount

            # TEMPORARY UNTIL OVD OF RM204A HAS BEEN COVERED
            if rn == '204A':
                bt = rmn_bill.bill_total - ovd + 1000
            else:
                bt = rmn_bill.bill_total
            # ===============================================

            rmn_pf = get_object_or_404(TenantProfile, room_no__room_no=rn)

            # to_phone_no = rmn_pf.phone # To be permanent
            to_phone_no = '0840860087'  # TESTING ONLY

            bill_msg = "<ห้อง {0}> กรุณาชำระค่าเช่า ประจำเดือน {1} จำนวน {2:,.0f} บาท ภายในวันที่ 5 {3} {4} {5} <รายละเอียดค่าเช่า> ห้องพร้อมอุปกรณ์: {6:,.0f} บาท นำ้: {7:,.0f} บาท ไฟ: {8:,.0f} บาท ส่วนกลาง: {9:,.0f} บาท อื่นๆ: {10:,.0f} บาท ค้างจ่าย: {11:,.0f} บาท"
            bill_msg = bill_msg.format(rn, cur_th_mth, bt, next_th_m, cur_th_yr, bank_info, rc_and_rac, wc, ec, csc,
                                       osc,
                                       ovd)

            # --------------------------------------
            send_message(to_phone_no, bill_msg)
            # --------------------------------------

            messages.success(request, 'Billing SMS has been sent to: {}-{} !!'.format(rn, to_phone_no))
            return HttpResponseRedirect(reverse_lazy('misc_contents'))
        else:
            return render(request, 'ams/send_sms_to_individual_room.html', {'bills': bills})
    else:
        messages.info(request, 'No open bills available !!!')
    return HttpResponseRedirect(reverse_lazy('misc_contents'))


@login_required
def send_general_sms(request):
    if request.method == 'POST':
        phone_msg_form = PhoneNoMessage(request.POST)
        if phone_msg_form.is_valid():
            cd = phone_msg_form.cleaned_data

            phn = cd['phone_no']
            msg = cd['sms_msg']

            try:
                send_message(phn, msg)
            except Exception as err:
                messages.error(request, 'ERROR: {}'.format(str(err)))
                return HttpResponseRedirect(reverse_lazy('misc_contents'))
            else:
                messages.success(request, 'SMS has been sent to: {} !!'.format(phn))
                return HttpResponseRedirect(reverse_lazy('misc_contents'))
    else:
        phone_msg_form = PhoneNoMessage()
        return render(request, 'ams/send_general_sms.html', {'phone_msg_form': phone_msg_form})


@login_required
def misc_contents(request):
    return render(request, 'ams/misc_contents.html', {'section': 'misc'})


@login_required
def tenant_page(request):
    usr = str(request.user)
    fn, ln = usr.split(" ")
    # tenant_pf = get_object_or_404(TenantProfile, tenant__first_name=fn, tenant__last_name=ln)
    try:
        tenant_pf = TenantProfile.objects.get(tenant__first_name=fn, tenant__last_name=ln)
    except Exception as err:
        messages.error(request, 'ERROR: {} '.format(str(err)))
        return HttpResponseRedirect(reverse_lazy('login'))
    else:
        exd = {}
        exd.setdefault('Electricity CPU', 0)
        exd.setdefault('Water CPU', 0)
        exd.setdefault('Garbage', 0)
        exd.setdefault('Parking', 0)
        exd.setdefault('Wifi', 0)
        exd.setdefault('Cable TV', 0)
        exd.setdefault('Bed', 0)
        exd.setdefault('Bed accessories', 0)
        exd.setdefault('Dressing Table', 0)
        exd.setdefault('Clothing Cupboard', 0)
        exd.setdefault('TV Table', 0)
        exd.setdefault('Fridge', 0)
        exd.setdefault('Air-Conditioner', 0)

        for e in tenant_pf.extra.all():
            exd.update({e.desc: e.cpu})

        room_acc_cost = exd['Bed'] + exd['Bed accessories'] + exd['Dressing Table'] \
                        + exd['Clothing Cupboard'] + exd['TV Table'] + exd['Fridge'] \
                        + exd['Air-Conditioner']

        oth_ser_cost = exd['Garbage'] + exd['Parking'] + exd['Wifi'] + exd['Cable TV']

        cur_dt = datetime.datetime.now()

        return render(request, 'ams/tenant_page.html',
                      {'section': 'tenant_profile', 'tenant_pf': tenant_pf, 'room_acc_cost': room_acc_cost,
                       'oth_ser_cost': oth_ser_cost, 'cur_dt': cur_dt})


@login_required
def tenant_bill(request):
    tenant = str(request.user)
    bills = Billing.objects.filter(tenant_name=tenant)
    if bills:
        try:
            tn_bill = get_object_or_404(Billing, tenant_name=tenant, status='open')

        except Exception as err:
            # messages.error(request, 'ERROR: {} '.format(str(err)))
            now_month = str(datetime.datetime.now().month - 1)

            tn_bill = get_object_or_404(Billing, tenant_name=tenant, status='close', bill_date__month=now_month)

            bill_dt = tn_bill.bill_date.date()
            cur_day = bill_dt.day
            cur_mth = bill_dt.month
            cur_yr = bill_dt.year
            cur_th_mth = get_thai_month_name(str(bill_dt))
            cur_th_yr = get_thai_year(str(bill_dt))
            next_dt_mth = datetime.date(cur_yr, cur_mth + 1, 15)
            next_th_m = get_thai_month_name(str(next_dt_mth))

            room_with_acc_cost = tn_bill.room_cost + tn_bill.room_acc_cost + tn_bill.adjust

            paid_str = 'ชำระแล้ว ณ วันที่ {} {} {}'.format(cur_day, cur_th_mth, cur_yr)

            # TEMPORARY UNTIL OVD OF RM204A HAS BEEN COVERED
            rn = tn_bill.room_no
            if rn == '204A':
                bill_total = tn_bill.bill_total - tn_bill.overdue_amount + 1000
            else:
                bill_total = tn_bill.bill_total
            # -------------------------------------------------------------------

            return render(request, 'ams/tenant_bill.html',
                          {'section': 'bill', 'tn_bill': tn_bill, 'room_with_acc_cost': room_with_acc_cost,
                           'bill_total': bill_total, 'cur_th_mth': cur_th_mth, 'next_th_m': next_th_m,
                           'cur_th_yr': cur_th_yr, 'paid_str': paid_str})

        else:

            bill_dt = tn_bill.bill_date.date()
            cur_mth = bill_dt.month
            cur_yr = bill_dt.year
            cur_th_mth = get_thai_month_name(str(bill_dt))
            cur_th_yr = get_thai_year(str(bill_dt))
            next_dt_mth = datetime.date(cur_yr, cur_mth + 1, 15)
            next_th_m = get_thai_month_name(str(next_dt_mth))

            room_with_acc_cost = tn_bill.room_cost + tn_bill.room_acc_cost + tn_bill.adjust
            paid_str = 'รอชำระ'

            # TEMPORARY UNTIL OVD OF RM204A HAS BEEN COVERED
            rn = tn_bill.room_no
            if rn == '204A':
                bill_total = tn_bill.bill_total - tn_bill.overdue_amount + 1000
            else:
                bill_total = tn_bill.bill_total
            # ===============================================

            return render(request, 'ams/tenant_bill.html',
                          {'section': 'bill', 'tn_bill': tn_bill, 'room_with_acc_cost': room_with_acc_cost,
                           'bill_total': bill_total, 'cur_th_mth': cur_th_mth, 'next_th_m': next_th_m,
                           'cur_th_yr': cur_th_yr, 'paid_str': paid_str})
    else:

        # NEW TENANT ******************************************
        return HttpResponseRedirect(reverse_lazy('new_tenant'))


@login_required
def new_tenant(request):
    tenant_name = str(request.user)

    return render(request, 'ams/new_tenant.html', {'section': 'bill', 'tenant_name': tenant_name})
