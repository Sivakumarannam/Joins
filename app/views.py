from django.shortcuts import render
# Create your views here.
from app.models import *
from django.db.models import Q
def equijoins(request):
    EMPO=Emp.objects.select_related('deptno').all()
    EMPO=Emp.objects.select_related('deptno').filter(sal__gt=2000)
    EMPO=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPO=Emp.objects.select_related('deptno').filter(ename='SCOTT')
    EMPO=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EMPO=Emp.objects.select_related('deptno').filter(deptno__loc='DALLAS')
    EMPO=Emp.objects.select_related('deptno').filter(job='ANALYST')
    EMPO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPO=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPO=Emp.objects.select_related('deptno').filter(comm=0)
    EMPO=Emp.objects.select_related('deptno').filter(comm=None)
    EMPO=Emp.objects.select_related('deptno').filter(comm__lt=500)
    EMPO=Emp.objects.select_related('deptno').all()[2:5]
    EMPO=Emp.objects.select_related('deptno').filter(deptno__loc='NEW YORK', hiredate__year=2024)    
    d={'EMPO':EMPO}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    EMO=Emp.objects.select_related('mgr').all()
    EMO=Emp.objects.select_related('mgr').filter(ename='KING')
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE',sal__gt=1500)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT',hiredate__year=2023)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='CLARK',deptno=10)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='FORD',comm__isnull=True,sal=800,hiredate__year=2023)
    EMO=Emp.objects.select_related('mgr').filter(ename='TURNER',mgr__ename='BLAKE',sal=1500,comm__isnull=False)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='FORD',sal__gte=800)
    EMO=Emp.objects.select_related('mgr').filter(ename='JAMES',mgr__ename='BLAKE')
    EMO=Emp.objects.select_related('mgr').filter(mgr__hiredate__year__gte=2024)
    EMO=Emp.objects.select_related('mgr').filter(mgr__deptno=10)
    EMO=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    EMO=Emp.objects.select_related('mgr').exclude(mgr__ename='BLAKE')
    EMO=Emp.objects.select_related('mgr').exclude(mgr__ename='BLAKE',ename='JAMES')
    d={'EMO':EMO}
    return render(request,'selfjoins.html',d)

def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING',mgr__ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') | Q(mgr__ename='SCOTT'))
    emd=Emp.objects.select_related('deptno','mgr').exclude(deptno__dname='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES',deptno__dname='ACCOUNTING',job='ANALYST')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',mgr__ename='KING',sal=2850)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') |Q(deptno__dname='SALES'), Q(mgr__ename='SCOTT') |Q(mgr__ename='KING'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH',sal__gte=1000)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',sal__lte=1000)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') |Q(deptno__dname='KING'),mgr__ename='BLAKE',hiredate__year=2023)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') |Q(deptno__dname='KING'),mgr__ename='BLAKE',hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='ACCOUNTING') |Q(deptno__dname='RESEARCH'), Q(mgr__ename='KING') |Q(mgr__ename='SCOTT'), Q(deptno__loc='NEW YORK') |Q(deptno__loc='DALLAS'), sal__gte=1000)
    emd=Emp.objects.select_related('deptno','mgr').exclude(Q(mgr__ename='BLAKE') |Q(mgr__ename='KING'),deptno__dname='SALES',deptno__loc='CHICAGO',sal__gte=900)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='ACC')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='CH',sal__gte=2000)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname__startswith='RE') |Q(mgr__ename__endswith='ES'), deptno__loc__startswith='DA')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname__startswith='AC') |Q(mgr__ename__endswith='NG'), deptno__loc__startswith='NE',job__endswith='RK')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__loc__startswith='CH') |Q(deptno__loc__endswith='AS'), Q(mgr__ename__endswith='KE') |Q(mgr__ename__startswith='SC'), job__gte=800,hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__loc__startswith='CH') |Q(deptno__loc__endswith='AS'), Q(mgr__ename__endswith='KE') |Q(mgr__ename__startswith='SC'), job__gte=800,hiredate__year=2023)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__loc='DALLAS', sal__gte=100,mgr__ename='KING')
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)

