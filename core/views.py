# -*- coding: utf-8 -*-
from django.shortcuts import render

from core.models import Theme


def get_popular_themes(request):
    """
         Returns the list of themes (id and name), ordered by their success on the channel. 
         For each theme, its score will be given by the sum
         of the scores of all videos that contain that theme.
    """
    themes_q = Theme.objects.all().prefetch_related('video_set__comment_set', 'video_set__thumb_set')
    # 'order_by' score
    themes = sorted(themes_q, key = lambda x: x.score()) 
    context = {'themes': themes}
    return render(request, 'themes/get_popular_themes.html', context)

def index(request):
    """
         Returns the index of project
    """
    return render(request, 'index.html', locals())