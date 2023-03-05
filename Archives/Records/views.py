from django.shortcuts import render


# Create your views here.
def index(request):
    names = [["003", "Shtriga"], ["004", "Rakshasa"], 
             ["005", "Djinn"], ["006", "Acheri"],
             ["007", "Changeling"], ["008", "Crocotta"],
             ["009", "Rougarou"], ["010", "Ghoul"],
             ["011", "Wraith"], ["012", "Arachne"],
             ["013", "Kitsune"], ["014", "Vetala"],
             ["015", "Shojo"], ["016", "Aswang"],
             ["017", "Pishtaco"], ["018", "Zana"],
             ["019", "Banshee"], ["020", "Bisaan"],]
    return render(request, 'Records/index.html', {
        'error_message': "You didn't select a choice.",
        'names' : names,
    })

def wendigo(request):
    return render(request, 'Records/wendigo.html', {
        'error_message': "You didn't select a choice.",
    })

def gorgon(request):
    return render(request, 'Records/gorgon.html', {
        'error_message': "You didn't select a choice.",
    })