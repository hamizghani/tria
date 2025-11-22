from django.shortcuts import render
from django.http import Http404

# Hardcoded dance data for demonstration
DANCE_LIST = [
    {
        "id": 1,
        "name": "Tari Kecak",
        "description": "Traditional Balinese dance featuring a chant performed by a circle of performers.",
        "gerakan": [
            "Gerakan 1 description",
            "Gerakan 2 description",
            "Gerakan 3 description",
            "Gerakan 4 description",
        ],
        "youtube_id": "e3y85AUfGKo",
    },
    {
        "id": 2,
        "name": "Tari Janger",
        "description": "A lively dance from Bali with dynamic movements and group choreography.",
        "gerakan": [
            "Gerakan 1 description",
            "Gerakan 2 description",
            "Gerakan 3 description",
            "Gerakan 4 description",
        ],
        "youtube_id": "7RcjP7xexPQ",
    },
    # Add at least 8 more traditional Indonesian dances here
]

def dance_list(request):
    return render(request, "dances/dance_list.html", {"dances": DANCE_LIST})

def dance_detail(request, dance_id):
    dance = next((d for d in DANCE_LIST if d["id"] == dance_id), None)
    if dance is None:
        raise Http404("Dance not found")
    return render(request, "dances/dance_detail.html", {"dance": dance})

def dance_tutorial(request, dance_id):
    dance = next((d for d in DANCE_LIST if d["id"] == dance_id), None)
    if dance is None:
        raise Http404("Dance not found")
    return render(request, "dances/dance_tutorial.html", {"dance": dance})

def dance_assessment(request, dance_id):
    dance = next((d for d in DANCE_LIST if d["id"] == dance_id), None)
    if dance is None:
        raise Http404("Dance not found")
    return render(request, "dances/dance_assessment.html", {"dance": dance})

def dance_result(request, dance_id):
    dance = next((d for d in DANCE_LIST if d["id"] == dance_id), None)
    if dance is None:
        raise Http404("Dance not found")
    # Dummy mockup result
    mock_score = 90
    improvement = "Focus on smoother arm movements and posture."
    return render(request, "dances/dance_result.html", {
        "dance": dance,
        "score": mock_score,
        "improvement": improvement,
    })
