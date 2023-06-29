from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from django.utils.safestring import mark_safe
from . import views
from .models import Pages, Tests, Answers

# Create your views here.


def dampandmould(request):
    """ A view to return the intro page """
    thispage = 'dampandmould'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'dampandmould/intro.html', context)


def page001module002(request):
    """ A view to return page001 """
    thispage = 'page001module002'
    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': 'false',
        'prev_url': 'dampandmould',
        'prev_page': 'index',
        'prev_page_small': 'index',
        'next_url': 'page002module002',
        'next_page': 'what is condensation?',
        'next_page_small': 'condensation',
    }

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            return render(request, 'dampandmould/page001.html', context)

        """ create a Page for this user for this page """
        user_page = Pages(user=request.user,
                          page=thispage,
                          status=1,)
        user_page.save()

    return render(request, 'dampandmould/page001.html', context)


def page002module002(request):
    """ A view to return page002 """
    thispage = 'page002module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page001module002',
        'prev_page': 'background',
        'prev_page_small': 'background',
        'next_url': 'page003module002',
        'next_page': 'condensation in the home',
        'next_page_small': 'home condensation',
    }
    return render(request, 'dampandmould/page002.html', context)


def page003module002(request):
    """ A view to return page003 """
    thispage = 'page003module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page002module002',
        'prev_page': 'what is condensation?',
        'prev_page_small': 'condensation',
        'next_url': 'page004module002',
        'next_page': 'sources of condensation',
        'next_page_small': 'sources',
    }
    return render(request, 'dampandmould/page003.html', context)


def page004module002(request):
    """ A view to return page004 """
    thispage = 'page004module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page003module002',
        'prev_page': 'condensation in the home',
        'prev_page_small': 'home condensation',
        'next_url': 'page005module002',
        'next_page': 'ventilation',
        'next_page_small': 'ventilation',
    }
    return render(request, 'dampandmould/page004.html', context)


def page005module002(request):
    """ A view to return page005 """
    thispage = 'page005module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page004module002',
        'prev_page': 'sources of condensation',
        'prev_page_small': 'sources',
        'next_url': 'page006module002',
        'next_page': 'measuring humidity',
        'next_page_small': 'humidity',
    }
    return render(request, 'dampandmould/page005.html', context)


def page006module002(request):
    """ A view to return page006 """
    thispage = 'page006module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            """ specific to this page only """
            nexthidden = 'false'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page005module002',
        'prev_page': 'ventilation',
        'prev_page_small': 'ventilation',
        'next_url': 'page007module002',
        'next_page': 'managing humidity',
        'next_page_small': 'humidity',
    }
    return render(request, 'dampandmould/page006.html', context)


def page007module002(request):
    """ A view to return page007 """
    thispage = 'page007module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page006module002',
        'prev_page': 'measuring humidity',
        'prev_page_small': 'humidity',
        'next_url': 'page008module002',
        'next_page': 'cold surfaces',
        'next_page_small': 'cold surfaces',
    }
    return render(request, 'dampandmould/page007.html', context)


def page008module002(request):
    """ A view to return page008 """
    thispage = 'page008module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page007module002',
        'prev_page': 'managing humidity',
        'prev_page_small': 'humidity',
        'next_url': 'page009module002',
        'next_page': 'damp & mould survey',
        'next_page_small': 'survey',
    }
    return render(request, 'dampandmould/page008.html', context)


def page009module002(request):
    """ A view to return page009 """
    thispage = 'page009module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page008module002',
        'prev_page': 'cold surfaces',
        'prev_page_small': 'cold surfaces',
        'next_url': 'page010module002',
        'next_page': 'treating mould',
        'next_page_small': 'treating',
    }
    return render(request, 'dampandmould/page009.html', context)


def page010module002(request):
    """ A view to return page010 """
    thispage = 'page010module002'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page009module002',
        'prev_page': 'damp & mould survey',
        'prev_page_small': 'survey',
        'next_url': 'damptestintro',
        'next_page': 'test',
        'next_page_small': 'test',
    }
    return render(request, 'dampandmould/page010.html', context)


def damptestintro(request):
    """ A view to return the damptestintro page """
    thistest = 'damptestintro'
    nexttest = 'test001module002'
    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'dampandmould/testintro.html', context)


def dampcheckanswer(request):
    """ Check the answer to each question against the correct answer """
    nexthidden = 'false'
    test_already_complete = 'false'
    next_url = 'dampnexttest'
    next_page = 'next question'

    if request.user.is_authenticated:

        if request.GET:
            if 'test_list' in request.GET:
                test_list = request.GET['test_list']
                test_list_list = test_list.split(',')
                test_already_complete_flag = test_list_list[2]
                thistest = test_list_list[0]
                next_test = get_object_or_404(Answers,
                                              test=thistest)
                nexttest = next_test.nexttest
                if test_already_complete_flag == 'true':
                    nexttemplate = 'dampandmould/' + nexttest[:7] + '.html'
                else:
                    nexttemplate = 'dampandmould/' + thistest[:7] + '.html'

        """ check if a Test Result exists for this user for this test """
        tests = Tests.objects.all()
        test_exists = (tests.filter
                       (user=request.user,
                        test=thistest))
        if test_exists:
            test_already_complete = 'true'
            if thistest == 'test010':
                next_page = 'test summary'
            else:
                next_page = 'next question'
        else:
            """ get information from testanswer form """
            if request.POST:
                testanswer = request.POST['testanswer']
                """ check if Test Result matches correct answer """
                correct_answer_query = get_object_or_404(Answers,
                                                         test=thistest)
                correct_answer = correct_answer_query.correctanswer
                if testanswer == correct_answer:
                    result = 1
                else:
                    result = 0

                """ create a Test Result for this user for this test """
                user_test = Tests(user=request.user,
                                  test=thistest,
                                  status=1,
                                  answer=testanswer,
                                  result=result)
                user_test.save()
                test_already_complete = 'true'
            nexthidden = 'false'
            if thistest == 'test010':
                next_page = 'test summary'
            else:
                next_page = 'next question'

    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'test_already_complete': test_already_complete,
        'next_url': next_url,
        'next_page': next_page,
        'next_page_small': next_page,
    }
    return render(request, nexttemplate, context)


def dampnexttest(request):
    """ Navigate to the next test """
    nexthidden = 'false'
    test_already_complete = 'false'
    next_url = 'dampcheckanswer'

    if request.user.is_authenticated:

        if request.GET:
            if 'test_list' in request.GET:
                test_list = request.GET['test_list']
                test_list_list = test_list.split(',')
                test_already_complete_flag = test_list_list[2]
                thistest = test_list_list[1]
                next_test = get_object_or_404(Answers,
                                              test=thistest)
                nexttest = next_test.nexttest
                nexttemplate = 'dampandmould/' + thistest[:7] + '.html'

        """ check if a Test Result exists for this user for this test """
        tests = Tests.objects.all()
        test_exists = (tests.filter
                       (user=request.user,
                        test=thistest))
        if test_exists:
            test_already_complete = 'true'
            nexthidden = 'false'
            if thistest == 'test010':
                next_page = 'test summary'
            else:
                next_page = 'next question'
            next_url = 'dampnexttest'
        else:
            test_already_complete = 'false'
            test_already_complete_flag == 'false'
            nexthidden = 'true'
            next_page = 'submit'

        if thistest == 'damptestsummary':
            """ get the Test Result for this user for this module """
            tests = Tests.objects.all()
            test_result = (tests.filter
                           (user=request.user))
            failed_test_result = test_result.filter(test__contains='')
            this_test_result = failed_test_result.exclude(test__contains='fail').order_by('test')
            this_test_count = this_test_result.count()
            test_score = this_test_result.filter(result='1').count()

            context = {
                'this_test_result': this_test_result,
                'this_test_count': this_test_count,
                'test_score': test_score,
            }

            return render(request, 'dampandmould/testsummary.html', context)

    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'test_already_complete': test_already_complete,
        'next_url': next_url,
        'next_page': next_page,
        'next_page_small': next_page,
    }
    return render(request, nexttemplate, context)


def dampretest(request):
    """ A view to reset the incorrect tests and return the retest page """
    thistest = 'testintro'
    nexttest = 'test001'

    if request.user.is_authenticated:

        if request.GET:
            if 'module_list' in request.GET:
                module_list = request.GET['module_list']

                """ create a Failed Test List for this user for this module """
                tests = Tests.objects.all()
                test_result = (tests.filter
                               (user=request.user))
                failed_test_result = test_result.filter(test__contains='')
                this_test_result = failed_test_result.exclude(test__contains='fail')
                this_failed_test_list = this_test_result.filter(result='0').order_by('test')
                for test in this_failed_test_list:
                    test.test = test.test + 'fail'
                    test.save()

    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'noarrows',
        'nexthidden': 'false',
        'this_failed_test_list': this_failed_test_list,
    }

    return render(request, 'dampandmould/testintro.html', context)


def damptestcertificate(request):
    """ A view to return the damptestcertificate page """
    if request.user.is_authenticated:

        if request.GET:
            """ get the Test Result for this user for this module """
            tests = Tests.objects.all()
            test_result = (tests.filter
                           (user=request.user))
            failed_test_result = test_result.filter(test__contains='')
            this_test_result = failed_test_result.exclude(test__contains='fail').order_by('test')
            this_test_count = this_test_result.count()
            test_score = this_test_result.filter(result='1').count()

    context = {
        'this_test_result': this_test_result,
        'this_test_count': this_test_count,
        'test_score': test_score,
    }

    return render(request, 'dampandmould/testcertificate.html', context)
