from django.shortcuts import render
# Create your views here.
from app.models import *
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

