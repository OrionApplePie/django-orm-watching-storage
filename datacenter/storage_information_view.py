from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        owner_name = Passcard.objects.get(visit__id=visit.id).owner_name

        non_closed_visits.append(
            {
                'who_entered': owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': Visit.format_duration(visit.get_duration()),
                'is_strange': visit.is_visit_long(),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
