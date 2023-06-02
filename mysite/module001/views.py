from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from django.utils.safestring import mark_safe
from . import views
from .models import Pages, Tests, Answers

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """
    thispage = 'valueandwaste'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'valueandwaste/intro.html', context)


def page001module001(request):
    """ A view to return page001 """
    thispage = 'page001module001'
    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': 'false',
        'prev_url': 'valueandwaste',
        'prev_page': 'index',
        'prev_page_small': 'index',
        'next_url': 'page002module001',
        'next_page': 'looking for waste',
        'next_page_small': 'looking',
    }

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            return render(request, 'valueandwaste/page001.html', context)

        """ create a Page for this user for this page """
        user_page = Pages(user=request.user,
                          page=thispage,
                          status=1,)
        user_page.save()

    return render(request, 'valueandwaste/page001.html', context)


def page002module001(request):
    """ A view to return page002 """
    thispage = 'page002module001'

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
        'prev_url': 'page001module001',
        'prev_page': 'background',
        'prev_page_small': 'background',
        'next_url': 'page003module001',
        'next_page': 'definition of value and waste',
        'next_page_small': 'definition',
    }
    return render(request, 'valueandwaste/page002.html', context)


def page003module001(request):
    """ A view to return page003 """
    thispage = 'page003module001'

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
        'prev_url': 'page002module001',
        'prev_page': 'looking for waste',
        'prev_page_small': 'looking',
        'next_url': 'page004module001',
        'next_page': 'examples of value',
        'next_page_small': 'value',
    }
    return render(request, 'valueandwaste/page003.html', context)


def page004module001(request):
    """ A view to return page004 """
    thispage = 'page004module001'

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
        'prev_url': 'page003module001',
        'prev_page': 'definition of value and waste',
        'prev_page_small': 'definition',
        'next_url': 'page005module001',
        'next_page': 'examples of waste',
        'next_page_small': 'waste',
    }
    return render(request, 'valueandwaste/page004.html', context)


def page005module001(request):
    """ A view to return page005 """
    thispage = 'page005module001'

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
        'prev_url': 'page004module001',
        'prev_page': 'examples of value',
        'prev_page_small': 'value',
        'next_url': 'page006module001',
        'next_page': 'necessary non-value-add',
        'next_page_small': 'non-value-add',
    }
    return render(request, 'valueandwaste/page005.html', context)


def page006module001(request):
    """ A view to return page006 """
    thispage = 'page006module001'

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
        'prev_url': 'page005module001',
        'prev_page': 'examples of waste',
        'prev_page_small': 'waste',
        'next_url': 'page007module001',
        'next_page': 'the eight wastes',
        'next_page_small': '8 wastes',
    }
    return render(request, 'valueandwaste/page006.html', context)


def page007module001(request):
    """ A view to return page007 """
    thispage = 'page007module001'

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
        'prev_url': 'page006module001',
        'prev_page': 'necessary non-value-add',
        'prev_page_small': 'non-value-add',
        'next_url': 'page008module001',
        'next_page': 'example: making a chair',
        'next_page_small': 'example',
    }
    return render(request, 'valueandwaste/page007.html', context)


def page008module001(request):
    """ A view to return page008 """
    thispage = 'page008module001'

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
        'prev_url': 'page007module001',
        'prev_page': 'the eight wastes',
        'prev_page_small': '8 wastes',
        'next_url': 'testintro',
        'next_page': 'test',
        'next_page_small': 'test',
    }
    return render(request, 'valueandwaste/page008.html', context)


def testintro(request):
    """ A view to return the testintro page """
    thistest = 'testintro'
    nexttest = 'test001module001'
    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'valueandwaste/testintro.html', context)


def nexttest(request):
    """ Navigate to the next test template """
    nexthidden = "true"
    test_already_complete = "false"
    next_page = "submit"

    if request.user.is_authenticated:

        if request.GET:
            if 'test_list' in request.GET:
                test_list = request.GET['test_list']
                test_list_list = test_list.split(',')
                thistest = test_list_list[0]
                next_test = get_object_or_404(Answers,
                                              test=thistest)
                nexttest = next_test.nexttest
                nexttemplate = 'valueandwaste/' + nexttest[:7] + '.html'

        """ check if a Test Result exists for this user for this test """
        tests = Tests.objects.all()
        test_exists = (tests.filter
                       (user=request.user,
                        test=thistest))
        if test_exists:
            test_already_complete = 'true'
            nexthidden = 'false'
            next_page = 'next question'
            thistemplate = 'valueandwaste/' + thistest[:7] + '.html'

        context = {
            'thistest': thistest,
            'nexttest': nexttest,
            'arrows': 'arrows',
            'nexthidden': nexthidden,
            'test_already_complete': test_already_complete,
            'next_url': 'checkanswer',
            'next_page': next_page,
            'next_page_small': next_page,
        }
        return render(request, nexttemplate, context)


def checkanswer(request):
    """ Check the answer to each question against the correct answer """
    nexthidden = "false"
    test_already_complete = "false"
    next_page = "next question"

    if request.user.is_authenticated:

        if request.GET:
            if 'test_list' in request.GET:
                test_list = request.GET['test_list']
                test_list_list = test_list.split(',')
                thistest = test_list_list[0]
                next_test = get_object_or_404(Answers,
                                              test=thistest)
                nexttest = next_test.nexttest
                nexttemplate = 'valueandwaste/' + nexttest[:7] + '.html'

            """ check if a Test Result exists for this user for this test """
            tests = Tests.objects.all()
            test_exists = (tests.filter
                           (user=request.user,
                            test=thistest))
        if test_exists:
            test_already_complete = 'true'
            nexthidden = 'false'
            next_page = 'next question'
            thistemplate = 'valueandwaste/' + thistest[:7] + '.html'

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
            nexthidden = 'true'
            next_page = 'submit'

    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'test_already_complete': test_already_complete,
        'next_url': 'nexttest',
        'next_page': next_page,
        'next_page_small': next_page,
    }
    return render(request, nexttemplate, context)


def testsummary(request):
    """ A view to return testsummary """
    lasttest = 'test010module001'

    if request.user.is_authenticated:

        """ check if a Test Result exists for this user for this test """
        tests = Tests.objects.all()
        test_exists = (tests.filter
                       (user=request.user,
                        test=thistest))
        if test_exists:
            test_already_complete = 'true'
            nexthidden = 'false'
            next_page = 'next question'
        else:
            test_already_complete = 'false'
            nexthidden = 'true'
            next_page = 'submit'

    context = {
        'thistest': thistest,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'test_already_complete': test_already_complete,
        'next_url': 'testintro',
        'next_page': next_page,
        'next_page_small': next_page,
    }
    return render(request, 'valueandwaste/testsummary.html', context)
