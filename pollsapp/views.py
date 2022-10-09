from django.shortcuts import render, redirect
from .models import PollTitle, PollChoice

def index(request):
    polls = PollTitle.objects.all()

    return render(request, '../templates/index.html', {'polls': polls})

def addpoll(request):
    if 'addpoll' in request.GET:
        pollname = request.GET['polltitle']
        choice1 = request.GET['answer1']
        choice2 = request.GET['answer2']
        choice3 = request.GET['answer3']
        choice4 = request.GET['answer4']
        addpoll = PollTitle(title=pollname)
        addpoll.save()

        choice1 = PollChoice(choice_polltitle  = addpoll, choice = choice1)
        choice1.save()
        choice2 = PollChoice(choice_polltitle  = addpoll, choice = choice2)
        choice2.save()
        choice3 = PollChoice(choice_polltitle  = addpoll, choice = choice3)
        choice3.save()
        choice4 = PollChoice(choice_polltitle  = addpoll, choice = choice4)
        choice4.save()
        
        return redirect('/')
        
    elif 'cancelpoll' in request.GET:
        return redirect('/')
        
    print('The add poll page is now being displayed.')
    return render(request, '../templates/addpoll.html')

def cancelpoll(request):
    return redirect('/')

def choose(request, pk):
    poll = PollTitle.objects.get(id = pk)
    choice = poll.relatedchoice.all()
    
    return render(request, 'choose.html', {'poll': poll, 'choice': choice})

def details(request, prim):

    detail = PollTitle.objects.get(id = prim)
    choiceset = detail.relatedchoice.all()

    if request.method == 'POST':
        
        mychoice = request.POST.get('yourchoice')
        getchoice = choiceset.get(id = mychoice)
        getchoice.number_of_selection = getchoice.number_of_selection + 1
        getchoice.save()
        

    for c in choiceset:
        print(c.id, ' ',c.choice, ' ', c.number_of_selection)

    return render(request, 'details.html', {'detail': detail, 'choiceset': choiceset})